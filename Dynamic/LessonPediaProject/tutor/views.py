from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from .backends import TutorAuthBackend
from .profile_update_form import TutorUpdateForm
from .models import Tutor, Subject
from django_countries import countries
import json
from django.db.models import Q
from django.http import JsonResponse
from client.models import Ranking, Review
from django.core.mail import send_mail
from client.models import Client
from app_admin.models import AppAdmin




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
                else:
                    return redirect('tutor_login')
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
    



# Email an Admin
def admin_support(request):
    """Email an Admin"""
    if request.method == 'POST':
        sender = request.POST.get('sender')
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        try:
            send_mail(subject, message, sender, [recipient])
            messages.success(request, 'Email Sent Successfully')
        except Exception as e:
            messages.error(request, 'Email Sending Failed')
            print('error sending email')
        return redirect('tutor_login')
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


# Tutor Dashboard
@login_required(login_url='tutor_login')
def tutor_dashboard(request):
    """Displays Tutor Dashboard"""
    if not isinstance(request.user, Tutor):
        error_message = 'Are you a tutor?'
        return render(request, 'tutor/access_denied.html', context={'error_message': error_message})
    tutor = Tutor.objects.filter(username=request.user.username).first()
    return render(request, 'tutor/tutor_dashboard.html', context={'tutor': tutor})


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
        quiz_result = (request.POST.get('quiz_result'))
        quiz_result= float(quiz_result)

        if tutor.quiz_count >= 2:
            messages.error(request, 'You have already taken the quiz twice')
        else:
            tutor.quiz_count += 1
            tutor.save()

            if quiz_result > tutor.quiz_result:
                print('quiz_result', quiz_result)
                print('tutor.quiz_result', tutor.quiz_result)
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
