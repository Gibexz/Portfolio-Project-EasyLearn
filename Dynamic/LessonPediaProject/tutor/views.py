from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib import messages
from django.urls import reverse
from .backends import TutorAuthBackend
from .forms import TutorUpdateForm
from .models import Tutor, Subject, TimeSlot, Certificate, SubjectCategory
from django_countries import countries
import json
from django.db.models import Q
from django.http import JsonResponse
from client.models import Ranking, Review
from django.core.mail import send_mail
from client.models import Client
from app_admin.models import AppAdmin
from .forms import TutorScheduleForm
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.http import require_POST
from generic_apps.models import Contract
from django.utils import timezone
from datetime import timedelta
import random, string


# validate payment
@login_required(login_url='tutor_login')
def validate_payment(request, contract_id):
    contract = get_object_or_404(Contract, pk=contract_id)
    if request.method == 'POST':
        payment_amount = request.POST.get('payment_amount')
        try:
            payment_amount = float(payment_amount)
            if  payment_amount > 0 and payment_amount <= contract.payment_remaining:
                contract.payment_made += payment_amount
                contract.payment_remaining -= payment_amount
                if contract.payment_remaining <= 0:
                    contract.contract_status = 'Settled'
                contract.save()
                return JsonResponse({'status': 'success', 'message': 'Payment successful'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid payment amount'})
        except ValueError:
            return JsonResponse({'status': 'error', 'message': 'Invalid payment amount'})
    return render(request, 'payment_form.html', {'contract': contract})


""" Helper functions to generate random contract code, convert user input to date, etc"""
# generate random contract code
def generate_contract_code():
    ''' Generate a random 8-character code using 5 digits and 3 uppercase letters '''    
    digits_part = ''.join(random.choices(string.digits, k=5))
    alphabets_part = ''.join(random.choices(string.ascii_uppercase, k=3))
    random_code = digits_part + alphabets_part
    return random_code

# convert user input to date
def parse_date(date_str):
    """Parse a date string in the format yyyy-mm-dd to a date object"""
    try:
        print(date_str)
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return None
"""Helper functions ends here"""

# Create contract
@login_required(login_url='client_login')
def create_contract(request, tutor_id):
    tutor = get_object_or_404(Tutor, pk=tutor_id)
    client = get_object_or_404(Client, username=request.user.username)
    if request.method == 'POST':

        subject_id = request.POST.get('subject_id')
        pay_rate = float(request.POST.get('pay_rate'))
        contract_length = int(request.POST.get('contract_length'))
        # create a contract to track the payment
        contract = Contract.objects.create(
            contract_code=generate_contract_code(),
            client=client,
            tutor=tutor,
            subject_id=subject_id,
            pay_rate=pay_rate,
            contract_length=contract_length,
            week_days=request.POST.get('week_days'),
            start_date=parse_date(request.POST.get('start_date')) or timezone.now().date(),
            end_date=timezone.now().date() + timedelta(days=contract_length),
            payment_remaining=pay_rate * contract_length,
        )
        return JsonResponse({'status': 'success', 'message': 'Contract created successfully',
                            'contract_id': contract.contract_code})

    subjects = [tutor.primary_subject] + list(tutor.subjects.all())
    return render(request, 'tutor/create_contract.html', {'tutor': tutor, 'subjects': subjects, 'client': client})

# accept or decline contract
def update_contract_status(request, contract_code):
    contract = get_object_or_404(Contract, contract_code=contract_code)
    if not contract:
        messages.error(request, 'Contract not found')
        return JsonResponse({'status': 'error', 'message': 'Contract not found'}, status=404)
    if request.method == 'POST':
        contract_status = request.POST.get('status')
        if contract_status == 'Accept':
            contract.contract_status = 'Active'
            contract.save()
            messages.success(request, 'Contract accepted successfully.')
            return JsonResponse({'status': 'success', 'message': 'Contract accepted successfully'})
        elif contract_status == 'Decline':
            contract.contract_status = 'Declined'
            contract.save()
            messages.success(request, 'Contract declined successfully.')
            return JsonResponse({'status': 'success', 'message': 'Contract declined successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid contract status'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


# Tutor Create and Update Subjects
@login_required(login_url='tutor_login')
def add_subject(request):
    try:
        tutor = Tutor.objects.get(username=request.user.username)
        all_tutor_subjects = tutor.subjects.all()
    except Tutor.DoesNotExist:
        return redirect('tutor_login')

    if request.method == 'POST':
        subject_name = request.POST.get('subjectName')
        category = request.POST.get('category')
        proficiency = request.POST.get('proficiency')
        teaching_experience = request.POST.get('teachingExperience')

        subject_category = SubjectCategory.objects.filter(name=category).first()
        subject_exists = tutor.subjects.filter(subject_name=subject_name).exists()

        if subject_name and category and proficiency and teaching_experience:
            if subject_exists:
                messages.error(request, 'Subject already exists')
                return JsonResponse({'status': 'error', 'info': 'Subject already exists'})
            else:
                tutor.subjects.create(
                    subject_name=subject_name,
                    category=subject_category,
                    proficiency=proficiency,
                    teaching_experience=teaching_experience,
                )
                tutor.save()
                Subject.update_tutor_count()
                messages.success(request, 'Subject added successfully.')
                tutor_subjects = [
                    [subject.subject_name, subject.proficiency] for subject in all_tutor_subjects
                ]

                return JsonResponse(
                    {
                        'status': 'success',
                        'tutor_subjects': tutor_subjects,
                        'primary_subject': tutor.primary_subject,
                    }
                )
        else:
            messages.error(request, 'Please fill all fields')
            return JsonResponse({'status': 'error', 'info': 'Invalid form'})

    return JsonResponse({'status': 'error', 'redirect_url': reverse('tutor_dashboard')})

@require_POST
@login_required(login_url='tutor_login')
def update_subject(request, subject_id):
    if not isinstance(request.user, Tutor):
        error_message = "Are you a tutor?"
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})

    tutor = get_object_or_404(Tutor, username=request.user.username)
    subject = get_object_or_404(tutor.subjects, pk=subject_id)
    if subject is None:
        return JsonResponse({'status': 'error', 'message': 'Subject not found'}, status=404)
    if tutor.primary_subject == subject:
        tutor.primary_subject = form_data.get('subjectName')
        tutor.save()
    form_data = request.POST
    subject.subject_name = form_data.get('subjectName', subject.subject_name)
    subject.category = SubjectCategory.objects.filter(name=form_data.get('category')).first()
    subject.proficiency = form_data.get('proficiency')
    subject.teaching_experience = form_data.get('teachingExperience')
    subject.related_subjects = form_data.get('relatedSubjects')

    try:
        subject.save()
        Subject.update_tutor_count()
        print('subject saved')
        print('subject name', subject.subject_name)
        all_tutor_subjects = tutor.subjects.all()
        tutor_subjects = [
                    [subject.subject_name, subject.proficiency] for subject in all_tutor_subjects
                ]
        return JsonResponse({'status': 'success', 'tutor_subjects': tutor_subjects, 'primary_subject': tutor.primary_subject})
    except Exception as e:
        print(e)
        return JsonResponse(
            {'status': 'error', 'error': f'Error updating subject: {str(e)}'},
            status=500,
        )

# Delete Tutor Subjects
@login_required(login_url='tutor_login')
def delete_subject(request, subject_id):
    """Delete a subject"""
    if not isinstance(request.user, Tutor):
        error_message = "Only tutors are allowed here, are you a tutor?"
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})

    tutor = get_object_or_404(Tutor, username=request.user.username)
    subject = get_object_or_404(Subject, pk=subject_id)
    all_tutor_subjects = tutor.subjects.all()


    if subject is not None:
        tutor.subjects.remove(subject)
        messages.success(request, 'Subject deleted successfully.')
        tutor_subjects = [
                    [subject.subject_name, subject.proficiency] for subject in all_tutor_subjects
                ]
        return JsonResponse({'status': 'success', 'tutor_subjects': tutor_subjects,
                              'primary_subject': tutor.primary_subject})
    else:
        return JsonResponse({'status': 'error', 'message': 'Subject not found'}, status=404)
    
    
# Extra tutor fields update
def more_update(request):
    """Update more fields in tutor table"""
    if not isinstance(request.user, Tutor):
        error_message = "Are you a tutor?"
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})
    tutor = get_object_or_404(Tutor, username=request.user.username)
    if request.method == 'POST':
        try:
            tutor.phone_number = request.POST.get('phone_number')
            tutor.lga_resident = request.POST.get('lga_resident')
            tutor.residential_address = request.POST.get('residential_address')
            tutor.state_of_origin = request.POST.get('state_of_origin')
            tutor.state_of_residence = request.POST.get('state_of_residence')
            tutor.primary_subject = request.POST.get('primary_subject')
            tutor.highest_qualification = request.POST.get('highest_qualification')
            tutor.availability = request.POST.get('availability')
            tutor.average_session_duration = request.POST.get('average_session_duration')
            tutor.open_to_work = request.POST.get('open_to_work')
            tutor.price_per_hour = request.POST.get('price_per_hour')
            tutor.negotiable = request.POST.get('negotiable')
            tutor.bio = request.POST.get('bio')
            tutor.save()
            messages.success(request, 'Profile updated successfully.')
        except Exception as e:
            print(e)
            messages.error(request, 'Failed to update profile. Please try again.')
        return redirect('tutor_dashboard')
    return redirect ('tutor_dashboard')

@login_required(login_url='tutor_login')
def change_password(request):
    """update tutor password"""
    if not isinstance(request.user, Tutor):
        error_message = 'You are not authorized to view this page'
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})
    if request.method == 'POST':
        tutor = request.user
        old_password = request.POST.get('password')
        new_password1 = request.POST.get('password1')
        new_password2 = request.POST.get('password2')

        if not tutor.check_password(old_password) :
            messages.error(request, 'Incorrect old password. Please try again.')
            return redirect('tutor_dashboard')

        if new_password1 != new_password2:
            messages.error(request, 'New passwords do not match. Please confirm your new password.')
            return redirect('tutor_dashboard')

        tutor.set_password(new_password1)
        tutor.save()

        update_session_auth_hash(request, tutor)
        messages.success(request, 'Password changed successfully.')
        return redirect('tutor_dashboard')
    return redirect('tutor_dashboard')

# Tutors documents upload
@login_required(login_url='tutor_login')
def upload_docs(request):
    if request.method == 'POST':
        tutor = get_object_or_404(Tutor, username=request.user.username)

        profile_pic = request.FILES.get('profilePic')
        if profile_pic:
            if tutor.profile_picture:
                tutor.profile_picture.delete()
            tutor.profile_picture = profile_pic
            tutor.save()

        cv_file = request.FILES.get('cv')
        if cv_file:
            if tutor.cv_id:
                tutor.cv_id.delete()
            tutor.cv_id = cv_file
            tutor.save()

        high_cert_file = request.FILES.get('highCert')
        if high_cert_file:
            if tutor.highest_qualification_cert:
                tutor.highest_qualification_cert.delete()
            tutor.highest_qualification_cert = high_cert_file
            tutor.save()


        other_certs_files = request.FILES.getlist('otherCerts')
        for other_cert_file in other_certs_files:
            # Create a new Certificate instance
            certificate = Certificate(
                tutor=tutor,
                certificate_file=other_cert_file,
                certificate_name=request.POST.get('certificate_name'), 
                issuing_authority=request.POST.get('issuing_authority'),
                date_of_issuance=datetime.strptime(request.POST.get('date_of_issuance'), '%Y-%m-%d') 
            )
            certificate.save()
        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


# Remove schedule from tutor dashboard
@login_required(login_url='tutor_login')
def delete_schedule(request, schedule_id):
    """Delete Tutor Schedule"""
    if not isinstance(request.user, Tutor):
        error_message = "You are not authorized to perform this operation"
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})

    schedule = get_object_or_404(TimeSlot, pk=schedule_id)
    if schedule is not None:
        schedule.delete()
        messages.success(request, 'Schedule Deleted Successfully')
        return JsonResponse({'status': 'success', 'redirect_url': reverse('tutor_dashboard')})
    else:
        messages.error(request, 'Schedule Deletion Failed')
        return JsonResponse({'status': 'error'})

@login_required(login_url='tutor_login')
def tutor_dashboard(request):
    if not isinstance(request.user, Tutor):
        error_message = 'Are you a tutor?'
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})
    
    tutor = Tutor.objects.filter(username=request.user.username).first()
    subject_categories = SubjectCategory.objects.all()
    tutor_subjects = tutor.subjects.all()

    tutor.active_contract_count = Contract.objects.filter(tutor=tutor, contract_status='Active').count()
    tutor.settled_contract_count = Contract.objects.filter(tutor=tutor, contract_status='Settled').count()
    tutor.pending_contract_count = Contract.objects.filter(tutor=tutor, contract_status='Pending').count()
    tutor.declined_contract_count = Contract.objects.filter(tutor=tutor, contract_status='Declined').count()
    tutor.terminated_contract_count = Contract.objects.filter(tutor=tutor, contract_status='Terminated').count()
    tutor.received_payments = sum([contract.payment_made for contract in tutor.contracts.all()])
    tutor.total_payment = sum([contract.contract_amount for contract in tutor.contracts.all()])
    tutor.save()

    pending_contracts = Contract.objects.filter(tutor=tutor, contract_status='Pending').order_by('created_at')
    settled_contracts = Contract.objects.filter(tutor=tutor, contract_status='Settled').order_by('created_at')
    active_contracts = Contract.objects.filter(tutor=tutor, contract_status='Active').order_by('created_at')
    contract_history = Contract.objects.filter(
        tutor=tutor,
        contract_status__in=['Settled', 'Active', 'Terminated'],
    ).order_by('-created_at')

    if request.method == 'POST':
        form = TutorScheduleForm(request.POST)
        if form.is_valid():
            timeslot = form.save(commit=False)
            timeslot.tutor = tutor
            timeslot.save()
            messages.success(request, 'Schedule updated successfully.')

            tutor_schedule = TimeSlot.objects.filter(tutor=tutor)
            schedule_data = [
                {
                    'day': schedule.day.name,
                    'from_hour': schedule.from_hour.name,
                    'to_hour': schedule.to_hour.name,
                }
                for schedule in tutor_schedule
            ]
            return JsonResponse({'status': 'success', 'schedule_data': schedule_data})
        else:
            messages.error(request, 'Error updating schedule. Please check the form.')
            return JsonResponse({'status': 'error'})
    else:
        form = TutorScheduleForm()
        tutor_schedule = TimeSlot.objects.filter(tutor=tutor)

    return render(request, 'tutor/tutor_dashboard.html',
                   context={'tutor': tutor, 'form': form, 'tutor_schedule': tutor_schedule,
                            'subject_categories': subject_categories, 'tutor_subjects': tutor_subjects,
                            'pending_contracts': pending_contracts, 'contract_history': contract_history,
                            'active_contracts': active_contracts, 'settled_contracts': settled_contracts})

# Tutor Login
def tutor_login(request):
    """Tutor Login"""
    if 'tutor' in request.path:
        if request.method == 'POST':
            username_or_email = request.POST.get('username_or_email')
            password = request.POST.get('password')
            tutor = TutorAuthBackend().authenticate(request, username_or_email=username_or_email, password=password)
            if tutor:
                if tutor.is_suspended == False and tutor.is_blocked == False:
                    login(request, tutor, backend='tutor.backends.TutorAuthBackend')
                    messages.success(request, "You're Logged In")
                    if tutor.institution:
                        return redirect('tutor_dashboard')
                    return redirect ('tutor_profile')

                elif tutor.is_suspended == True:
                    messages.error(request, 'This account is suspended by user, please contact support')
                    return redirect('admin_support')
                elif tutor.is_blocked == True:
                    messages.error(request, 'This account is blocked by admin, please contact support')
                    return redirect('admin_support')
            else:
                tutor_exists = Tutor.objects.filter(username=request.user.username).exists()
                if tutor_exists:
                    messages.error(request, 'Incorrect Password')
                else:
                    messages.error(request, 'User Not Found')
                return render(request, 'tutor/tutor_login.html', context={'username_or_email': request.user.username})
        else:
            return render(request, 'tutor/tutor_login.html')
    error_message = "Are you a tutor?"
    return render(request, 'tutor/access_denied.html', context={'error_message': error_message})


# Email an Admin
def admin_support(request):
    """Email an Admin"""
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            send_mail(
                subject,
                message,
                'sender@example.com', 
                ['developers.lessonpedia@gmail.com'],
                fail_silently=False,
            )
            return JsonResponse({'success': True})
        except Exception as e:
            print('Error sending email:', str(e))
            return JsonResponse({'success': False, 'error_message': str(e)})

    return render(request, 'tutor/admin_support.html')

# block tutor
@login_required(login_url='admin_login')
def block_tutor(request, tutor_id):
    """Block Tutor Account"""
    if not isinstance(request.user, AppAdmin):
        error_message = 'You lack the authorization to perform this action'
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})
    tutor = Tutor.objects.get(pk=tutor_id)
    if tutor is not None:
        tutor.is_blocked = True
        tutor.save()
        messages.success(request, 'Account Blocked Successfully')
        return redirect('admin_dashboard')
    else:
        messages.error(request, 'Account Blocking Failed')
        return redirect('admin_dashboard')


# Tutor Profile Update
# TODO: Update Result choices to accept choices other than first_class // Done

@login_required(login_url='tutor_login')
def tutor_profile(request):
    """profile update form"""
    if not isinstance(request.user, Tutor):
        error_message = "Are you a tutor?"
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})
    tutor = Tutor.objects.get(username=request.user.username)
    
    country_list = [('Select Country', 'Select Country'), ('NG', 'Nigeria')]
    others = [(code, name) for code, name in countries]
    country_list.extend(others)
    country_list_json = json.dumps(country_list)

    if tutor is not None:
        if request.method == 'POST':
            form = TutorUpdateForm(request.POST, request.FILES, instance=tutor)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile Updated Successfully')
                return redirect('tutor_dashboard')
            else:
                messages.error(request, 'Profile Update Failed')
                return render(request, 'tutor/tutor_profile.html', context={'form': form, 'tutor': tutor, 'country_list': country_list_json, 'form_errors': form.errors})
        else:
            form = TutorUpdateForm(instance=tutor)
            return render(request, 'tutor/tutor_profile.html',  context={'form': form, 'tutor': tutor, 'country_list': country_list_json, 'form_errors': form.errors})
    else:
        messages.error(request, 'Tutor not found for the given username')
        return redirect('tutor_login')



@login_required(login_url='client_signIn')
@login_required(login_url='client_signIn')
def view_tutors(request):
    """Displays all tutors"""
    if not isinstance(request.user, Client):
        error_message = 'Are you logged in as a learner?'
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})
    subjects = Subject.objects.all()
    tutors = Tutor.objects.all()
    for x in tutors: 
        ranks = Ranking().rankAverage(x.id)['avg_rank']
        x.rank = ranks
        x.save()
    user = request.user
    return render(request, 'tutor/view_tutors.html', context={'tutors': tutors, 'subjects': subjects, 'user': user})

@login_required(login_url='client_signIn')
def search_tutors(request):
    """Search for tutors based on query"""
    if not isinstance(request.user, Client):
        error_message = 'Are you logged in as a learner?'
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})
    
    query = request.GET.get('query', None)
    print('query', query)
    if query is not None:
        tutors = Tutor.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(subjects__subject_name__icontains=query)
        ).distinct()
        tutor_list = [ tutor.to_dict() for tutor in tutors]
        print(tutor_list)
        subjects = Subject.objects.filter(subject_name__icontains=query)
        subject_list = [{'subject_name': subject.subject_name} for subject in subjects]
        print(subject_list)

        response_data = {'tutors': tutor_list, 'query': query, 'subjects': subject_list}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'No query provided'})


# Tutor public profile
@login_required(login_url='client_signIn')
@login_required(login_url='client_signIn')
def tutor_detail(request, tutor_id):
    """Displays Tutor Public Profile"""
    if not isinstance(request.user, Client):
        error_message = 'Are you logged in as a learner?'
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})
    user = request.user
    subjects = Subject.objects.all()
    tutors = Tutor.objects.all()
    reviews = Review.objects.filter(tutor=tutor_id).order_by('-created_at')
    AvgRank = Ranking().rankAverage(tutor_id)
    tutor = get_object_or_404(Tutor, id=tutor_id)
    context ={'tutor': tutor, 'user': user, 'subjects': subjects, 'reviews': reviews, 'tutors': tutors, 'rank': AvgRank['avg_rank']}
    return render(request, 'tutor/tutor_detail.html', context=context)


@login_required(login_url='client_signIn')
def email_tutor(request, tutor_id):
    if not isinstance(request.user, Client):
        error_message = 'Are you logged in as a learner?'
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})
    
    if request.method == 'POST':
        sender = request.POST.get('sender')
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        senderInfo = request.POST.get('senderInfo')
        received_msg = request.POST.get('message')
        if senderInfo is not None:
            message = f"{received_msg}\n\n{senderInfo}"
        else:
            message = received_msg
        try:
            send_mail(subject, message, sender, [recipient])
            response_data = {'success': True}
        except Exception as e:
            response_data = {'success': False, 'error_message': str(e)}
            print('error sending email')

        return JsonResponse(response_data)
    return redirect('view_tutors')

@login_required(login_url='client_signIn')
def submit_review(request, tutor_id):
    if not isinstance(request.user, Client):
        error_message = 'Are you logged in as a learner?'
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})
    if request.method == 'POST':
        tutor = Tutor.objects.get(pk=tutor_id)
        review_text = request.POST.get('review_text')
        # Check if the client has already ranked this tutor
        existing_review = Review.objects.filter(tutor=tutor, client=request.user).first()
        if existing_review:
            existing_review.review_text = review_text
            existing_review.save()
        else:
            Review.objects.create(tutor=tutor, client=request.user, review_text=review_text)

    return redirect('tutor_detail', tutor_id=tutor_id)



@login_required(login_url='tutor_login')
def quiz_guide(request):
    """Displays Tutor Quiz and Results"""
    if not isinstance(request.user, Tutor):
        messages.error(request, 'You are not authorized to view this page')
        error_message = 'You must be logged in as a Tutor'
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})
    tutor = Tutor.objects.get(username=request.user.username)
    if tutor.quiz_count > 1:
        error_message = 'You have already taken the assessment twice'
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message, 'quiz_count': tutor.quiz_count})
    
    return render(request, 'tutor/quiz_guide.html')


@login_required(login_url='tutor_login')
def tutor_quiz(request):
    if not isinstance(request.user, Tutor):
        error_message = "Are you a tutor?"
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})

    tutor = Tutor.objects.get(username=request.user.username)
    print(tutor.quiz_count)
    quiz_count = tutor.quiz_count 

    if request.method == 'POST':
        quiz_result = float(request.POST.get('quiz_result'))

        if tutor.quiz_count >= 2:
            messages.error(request, 'You have already taken the quiz twice')
        else:
            tutor.quiz_count += 1
            tutor.save()

            print('quiz_result', quiz_result)
            print('type quiz_res',type(quiz_result))
            print('tutor.quiz_result', tutor.quiz_result)
            print('type tutor.quiz_result', type(tutor.quiz_result))

            if quiz_result > tutor.quiz_result:
                tutor.quiz_result = quiz_result
                tutor.save()
                messages.success(request, 'Quiz Submitted Successfully')
            else:
                messages.success(request, 'Your previous score is higher than this one')

        return redirect('tutor_dashboard')

    elif quiz_count >= 2:
        error_message = 'You have already taken the assessment twice'
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})

    return render(request, 'tutor/tutor_quiz.html', context={'quiz_count': quiz_count})


# Deactivate Tutor Account
@login_required(login_url='tutor_login')
def suspend_tutor(request, tutor_id):
    """Suspend Tutor Account"""
    if not isinstance(request.user, Tutor) and not isinstance(request.user, AppAdmin):
        error_message = 'You lack the authorization to perform this action'
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})
    if request.method == 'POST':
        tutor = Tutor.objects.get(id=tutor_id)
        password = request.POST.get('password')
        if tutor is not None:
            if not tutor.check_password(password):
                messages.error(request, 'Incorrect Password')
                return redirect('tutor_dashboard')
            tutor.is_suspended = True
            tutor.save()
            logout(request)
            messages.success(request, 'Account Suspended Successfully')
            return redirect('tutor_login')
        else:
            messages.error(request, 'Account Suspension Failed')
            return redirect('tutor_dashboard')
    return redirect('tutor_dashboard')

# Tutor Logout   
def tutor_logout(request):
    logout(request)
    messages.success(request, "You're Logged Out")
    return redirect('tutor_login') 

