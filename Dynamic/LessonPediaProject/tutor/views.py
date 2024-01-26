from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib import messages
from django.urls import reverse
from .backends import TutorAuthBackend
from .forms import TutorUpdateForm
from .models import Tutor, Subject, TimeSlot, Certificate, SubjectCategory, PasswordResetToken
from django.db.models import Q
from django.http import JsonResponse
from client.models import Client, Ranking, Review
from django.core.mail import send_mail
from client.models import Client, Review
from app_admin.models import AppAdmin
from .forms import TutorScheduleForm
from django.views.decorators.http import require_POST
from generic_apps.models import Contract, TutorReportAbuse
from django.utils import timezone
from datetime import timedelta
import random, string
from django.db import IntegrityError, transaction

"""Logic for Lessonpedia Tutor App"""

# Tutor reports
@login_required(login_url='tutor_login')
def report_abuse(request):
    if request.method == 'POST':
        tutor = get_object_or_404(Tutor, id=request.user.id)
        report_subject = request.POST.get('report_subject')
        client_id = request.POST.get('client_id')
        message = request.POST.get('message')

        if report_subject == 'Others':
            subject = request.POST.get('subject')
        else:
            subject = report_subject

        client = get_object_or_404(Client, pk=client_id)
        report = TutorReportAbuse.objects.create(
            tutor=tutor,
            target_client_id=client,
            subject=subject,
            message=message,
        )
        report.save()

        messages.success(request, 'Report submitted successfully.')
        return redirect('tutor_dashboard')
    return redirect('tutor_dashboard')


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
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        return None
"""Helper functions ends here"""


# Terminate contract
@require_POST
@login_required(login_url='tutor_login')
def terminate_contract(request):
    """Terminate a contract from tutor dashboard"""
    if not isinstance(request.user, Tutor):
        error_message = "Are you a tutor?"
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})
    contract_code = request.POST.get('contract_code')
    statement = request.POST.get('statement')
    reason = request.POST.get('remark')
    remark = f"{reason} \n\n {statement}"
    contract = get_object_or_404(Contract, contract_code=contract_code)
    if contract is not None:
        if contract.contract_status == 'Terminated':
            messages.error(request, 'Contract already terminated.')
            return redirect('tutor_dashboard')
        if len(remark) < 10:#HTML should handle this but just in case
            messages.error(request, 'Please enter a remark of at least 10 characters.')
            return redirect('tutor_dashboard')
        contract.remark = remark
        contract.contract_status = 'Terminated'
        contract.save()
        messages.success(request, 'Contract terminated successfully.')
        return redirect('tutor_dashboard')
    else:
        messages.error(request, 'Contract termination failed.')
        return redirect('tutor_dashboard')



# Create contract
@login_required(login_url='client_login')
def create_contract(request, tutor_id):
    tutor = get_object_or_404(Tutor, pk=tutor_id)
    subjects = list(tutor.subjects.all())

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
        return redirect('validate_user', whoami=request.user)

        # return JsonResponse({'status': 'success', 'message': 'Contract created successfully',
        #                     'contract_id': contract.contract_code})
    return render(request, 'tutor/create_contract.html', {'tutor': tutor, 'subjects': subjects, 'client': client})

# accept or decline contract
def update_contract_status(request, contract_code):
    contract = get_object_or_404(Contract, contract_code=contract_code)
    if not isinstance(request.user, Tutor):
        return JsonResponse({'status': 'error', 'message': 'You are not authorized to perform this action'}, status=403)

    if not contract:
        messages.error(request, 'Contract not found')
        return JsonResponse({'status': 'error', 'message': 'Contract not found'}, status=404)

    
    if request.method == 'POST':
        def get_data():

            tutor = get_object_or_404(Tutor, id=request.user.id)
            tutor.active_contracts_count = Contract.objects.filter(tutor=tutor, contract_status='Active').count()
            tutor.settled_contracts_count = Contract.objects.filter(tutor=tutor, contract_status='Settled').count()
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
            return {

                'status': 'success',
                'pending_contracts_count': tutor.pending_contract_count,
                'active_contracts_count': tutor.active_contracts_count,
                'settled_contracts_count': tutor.settled_contracts_count,
                'pending_contracts': [{'client_name': contract.client.get_full_name(),
                                        'subject_name': contract.subject.subject_name,
                                        'week_days': contract.week_days,
                                        'contract_length': contract.contract_length,
                                        'pay_rate': contract.pay_rate,
                                        'start_date': contract.start_date.strftime("%d-%m-%Y"),
                                        'contract_code': contract.contract_code,
                                        'contract_status': contract.contract_status} for contract in pending_contracts],
                'settled_contracts': [{'client_name': contract.client.get_full_name(),
                                        'subject_name': contract.subject.subject_name,
                                        'contract_length': contract.contract_length,
                                        'pay_rate': contract.pay_rate,
                                        'contract_code': contract.contract_code,
                                        'start_date': contract.start_date.strftime("%d-%m-%Y"),
                                        'end_date': contract.end_date.strftime("%d-%m-%Y")} for contract in settled_contracts], 
                'active_contracts': [{'contract_code': contract.contract_code,
                                        'client_name': contract.client.get_full_name(),
                                        'subject_name': contract.subject.subject_name,
                                        'start_date': contract.start_date.strftime("%d-%m-%Y"),
                                        'end_date': contract.end_date.strftime("%d-%m-%Y"),
                                        'week_days': contract.week_days,
                                        'contract_status': contract.contract_status} for contract in active_contracts],
                'contract_history': [{'client_name': contract.client.get_full_name(),
                                        'subject_name': contract.subject.subject_name,
                                        'start_date': contract.start_date.strftime("%d-%m-%Y"),
                                        'end_date': contract.end_date.strftime("%d-%m-%Y"),
                                        'contract_code': contract.contract_code,
                                        'week_days': contract.week_days,
                                        'contract_status': contract.contract_status} for contract in contract_history],
                'received_payments': tutor.received_payments,
            }
    

        contract_status = request.POST.get('status')
        if contract_status == 'Accept':
            contract.contract_status = 'Active'
            contract.save()

            messages.success(request, 'Contract accepted successfully.')
            return JsonResponse(get_data())
        elif contract_status == 'Decline':
            contract.contract_status = 'Declined'
            contract.save()
            messages.success(request, 'Contract declined successfully.')
            return JsonResponse(get_data())

        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid contract status'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})


# Tutor Create and Update Subjects
@login_required(login_url='tutor_login')
def add_subject(request):
    """Add a subject to the tutor's profile"""
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
        subject_exists = Subject.objects.filter(subject_name=subject_name).exists()

        if subject_name and category and proficiency and teaching_experience:
            try:
                with transaction.atomic():
                    if subject_exists:
                        # Subject already exists, associate it with the tutor
                        existing_subject = Subject.objects.get(subject_name=subject_name)
                        tutor.subjects.add(existing_subject)
                        tutor.save()
                    else:
                        # Subject does not exist, create it and associate it with the tutor
                        new_subject = tutor.subjects.create(
                            subject_name=subject_name,
                            category=subject_category,
                            proficiency=proficiency,
                            teaching_experience=teaching_experience,
                        )
                        tutor.save()
                        Subject.update_tutor_count()

                all_tutor_subjects = tutor.subjects.all()
                tutor_subjects = [
                    [subject.id, subject.subject_name, subject.proficiency] for subject in all_tutor_subjects
                ]

                messages.success(request, 'Subject added successfully.')
                return JsonResponse(
                    {
                        'status': 'success',
                        'tutor_subjects': tutor_subjects,
                        'primary_subject': tutor.primary_subject,
                    }
                )
            except IntegrityError:
                # Handle IntegrityError if needed, currently no specific handling for it
                messages.error(request, 'An error occurred while processing your request.')
                return JsonResponse({'status': 'error', 'info': 'An error occurred'})
        else:
            messages.error(request, 'Please fill all fields')
            return JsonResponse({'status': 'error', 'info': 'Invalid form'})

    return JsonResponse({'status': 'error', 'redirect_url': reverse('tutor_dashboard')})


# Update Tutor Subjects
@require_POST
@login_required(login_url='tutor_login')
def update_subject(request, subject_id):
    if not isinstance(request.user, Tutor):
        error_message = "Are you a tutor?"
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})

    tutor = get_object_or_404(Tutor, username=request.user.username)
    subject = get_object_or_404(tutor.subjects, pk=subject_id) or tutor.primary_subject
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
        all_tutor_subjects = tutor.subjects.all()
        tutor_subjects = [ tutor.primary_subject ] + [
                    [subject.id, subject.subject_name, subject.proficiency] for subject in all_tutor_subjects
                ]
        return JsonResponse({'status': 'success', 'tutor_subjects': tutor_subjects, 'primary_subject': tutor.primary_subject})
    except Exception as e:
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


    if subject is not None:
        tutor.subjects.remove(subject)
        messages.success(request, 'Subject deleted successfully.')
        
        
        all_tutor_subjects = tutor.subjects.all()
        Subject.update_tutor_count()

        tutor_subjects = [
                    [subject.id, subject.subject_name, subject.proficiency] for subject in all_tutor_subjects
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
            messages.error(request, 'Failed to update profile. Please try again.')
        return redirect('tutor_dashboard')
    return redirect ('tutor_dashboard')


# change password
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


# Tutor Dashboard
@login_required(login_url='tutor_login')
def tutor_dashboard(request):
    if not isinstance(request.user, Tutor):
        error_message = 'Are you a tutor?'
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})
    
    tutor = Tutor.objects.get(id=request.user.id)
    reports = TutorReportAbuse.objects.filter(tutor=tutor).order_by('-created_at')
    contracts = Contract.objects.filter(tutor=tutor).order_by('-created_at')
    clients = set(contract.client for contract in contracts)

    subject_categories = SubjectCategory.objects.all()
    tutor_subjects = tutor.subjects.all().order_by('subject_name')

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
                    'id': schedule.id
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
                            'active_contracts': active_contracts, 'settled_contracts': settled_contracts,
                            'reports': reports, 'clients': clients})


# Tutor Login
def tutor_login(request):
    """Tutor Login"""
    if 'tutor' in request.path:
        if request.method == 'POST':
            username_or_email = request.POST.get('username_or_email').strip()
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
                tutor_exists = Tutor.objects.filter(email=username_or_email).exists()
                if tutor_exists:
                    messages.error(request, 'Incorrect Password, Please try again')
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
    categories = SubjectCategory.objects.all()
    
    if tutor is not None:
        if request.method == 'POST':
            date_of_birth = parse_date(request.POST.get('dob') or None)
            subject_name = request.POST.get('subjectName').strip()
            category = request.POST.get('category')
            proficiency = request.POST.get('proficiency')
            teaching_experience = request.POST.get('teachingExperience')
            subject_category = SubjectCategory.objects.filter(name=category).first()

            if subject_name and category and proficiency and teaching_experience:
                try:
                    with transaction.atomic():
                        subject, created = Subject.objects.get_or_create(
                            subject_name=subject_name,
                            defaults={
                                'category': subject_category,
                                'proficiency': proficiency,
                                'teaching_experience': teaching_experience,
                            }
                        )

                        if not created:
                            # Subject with the same name already exists, associate it with the tutor
                            try:

                                existing_subject = tutor.subjects.get(subject_name=subject_name)
                                existing_subject.category = subject_category
                                existing_subject.proficiency = proficiency
                                existing_subject.teaching_experience = teaching_experience
                                existing_subject.save()

                                # Update tutor count
                                Subject.update_tutor_count()
                            except Subject.DoesNotExist:
                                tutor.subjects.add(subject)
                                tutor.primary_subject = subject_name
                                tutor.date_of_birth = date_of_birth
                                tutor.save()
                                Subject.update_tutor_count()

                        else:
                            # Subject does not exist, create it and associate it with the tutor
                            tutor.subjects.add(subject)
                            tutor.primary_subject = subject_name
                            tutor.date_of_birth = date_of_birth
                            tutor.save()
                            Subject.update_tutor_count()
                except IntegrityError:
                    messages.error(request, 'Subject with the same name already exists')
                    return render(request, 'tutor/tutor_profile.html', context={'tutor': tutor, 'categories': categories})
            else:
                messages.error(request, 'Please fill all fields')
                return render(request, 'tutor/tutor_profile.html', context={'tutor': tutor, 'categories': categories})

            form = TutorUpdateForm(request.POST, request.FILES, instance=tutor)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile Updated Successfully')
                return redirect('tutor_dashboard')
            else:
                messages.error(request, 'Profile Update Failed')
                return render(request, 'tutor/tutor_profile.html', context={'form': form, 'tutor': tutor, 'categories': categories})
        else:
            form = TutorUpdateForm(instance=tutor)
            return render(request, 'tutor/tutor_profile.html', context={'form': form, 'tutor': tutor, 'categories': categories})
    else:
        messages.error(request, 'Tutor not found for the given username')
        return redirect('tutor_login')


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
        if not ranks:
            ranks = 1
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
    if query is not None:
        tutors = Tutor.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) |Q(primary_subject__icontains=query) |  Q(subjects__subject_name__icontains=query)
        ).distinct()
        tutor_list = [ tutor.to_dict() for tutor in tutors]
        subjects = Subject.objects.filter(subject_name__icontains=query)
        subject_list = [{'subject_name': subject.subject_name} for subject in subjects]

        response_data = {'tutors': tutor_list, 'query': query, 'subjects': subject_list}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'No query provided'})


# Tutor public profile
@login_required(login_url='client_signIn')
def tutor_detail(request, tutor_id):
    """Displays Tutor Public Profile"""
    if not isinstance(request.user, Client):
        error_message = 'Are you logged in as a learner?'
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})
    tutors_count = Tutor.objects.all().count()
    user = request.user
    subjects = Subject.objects.all()
    tutors = Tutor.objects.all()
    reviews = Review.objects.filter(tutor=tutor_id).order_by('-created_at')
    AvgRank = Ranking().rankAverage(tutor_id)
    tutor = get_object_or_404(Tutor, id=tutor_id)
    context ={'tutor': tutor, 'user': user, 'subjects': subjects, 'reviews': reviews, 'tutor_count': tutors_count, 'tutors': tutors, 'rank': AvgRank['avg_rank']}
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
    quiz_count = tutor.quiz_count 

    if request.method == 'POST':
        quiz_result = float(request.POST.get('quiz_result'))

        if tutor.quiz_count >= 2:
            messages.error(request, 'You have already taken the quiz twice')
        else:
            tutor.quiz_count += 1
            tutor.save()


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


# Genereate password reset token
def generate_password_reset_token():
    """Generate password reset token"""
    first_digit = random.choice(string.digits[1:])
    rest_of_digits = ''.join(random.choices(string.digits, k=5))
    token = first_digit + rest_of_digits
    return int(token)


# Forgot Password
def forgot_password(request):
    """Forgot Password"""
    if request.method == 'POST':
        sender = request.POST.get('sender')
        recipient = request.POST.get('email').strip()
        subject = "Password Reset Code"
        token = generate_password_reset_token()
        tutor = get_object_or_404(Tutor, email=recipient)
        if tutor:
            # Use get_or_create to create a new PasswordResetToken if it doesn't exist
            password_reset_token, created = PasswordResetToken.objects.get_or_create(user=tutor)
            password_reset_token.token = token
            password_reset_token.created_at = timezone.now()  # Update the created_at field
            password_reset_token.save()

            message = f"Your password reset code is {token} (expires in one hour).\n\nPlease do not share this code with anyone\nIf you didn't request this pin, we recommend you change your Lessonpedia password.\n\nRegards,\nLessonpedia Team"
            try:
                send_mail(subject, message, sender, [recipient])
                response_data = {'success': True}
            except Exception as e:
                response_data = {'success': False, 'error_message': str(e)}
            return JsonResponse(response_data)
        else:
            messages.error(request, 'User does not exist')
            return JsonResponse({'success': False, 'error_message': 'User does not exist'})
    return render(request, 'tutor/tutor_login.html', context={'tutor_email': recipient})


#confirm password reset token
def confirm_password_reset_token(request):
    """Confirm password reset token"""
    if request.method == 'POST':
        token = request.POST.get('token')
        user_email = request.POST.get('tutor_email')
        user = get_object_or_404(Tutor, email=user_email)
        
        try:
            password_reset_token = PasswordResetToken.objects.get(user=user)
        except PasswordResetToken.DoesNotExist:
            return JsonResponse({'success': False, 'error_message': 'Token not found'})

        # Check if the provided token matches and is not expired
        if token == password_reset_token.token and not password_reset_token.is_expired():
            # Token is valid, you can proceed with the next steps
            return JsonResponse({'success': True})
        else:
            messages.error(request, 'Invalid or expired token')
            return JsonResponse({'success': False, 'error_message': 'Invalid or expired token'})

    return JsonResponse({'success': False})


# reset password
def reset_password(request):
    """Reset Password"""
    if request.method == 'POST':
        password = request.POST.get('newPassword')
        confirm_password = request.POST.get('confirmPassword')
        email = request.POST.get('tutor_email').strip()
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return JsonResponse({'success': False, 'error_message': 'Passwords do not match'})
        try:
            tutor = get_object_or_404(Tutor, email=email)
            tutor.set_password(password)
            tutor.save()
            messages.success(request, 'Password reset successful, Please Login')
            return JsonResponse({'success': True, 'redirect_url': reverse('tutor_login')})
        except Tutor.DoesNotExist:
            messages.error(request, 'User does not exist')
            return JsonResponse({'success': False, 'error_message': 'User does not exist'})
    return render(request, 'tutor/tutor_login.html')


# Tutor Logout   
def tutor_logout(request):
    logout(request)
    messages.success(request, "You're Logged Out")
    return redirect('tutor_login') 