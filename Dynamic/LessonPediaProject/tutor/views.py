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
from client.models import Ranking
from client.models import Review




# Tutor Login
def tutor_login(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')
        tutor = TutorAuthBackend().authenticate(request, username_or_email=username_or_email, password=password)
        if tutor:
            if 'tutor' in request.path:
                login(request, tutor, backend='tutor.backends.TutorAuthBackend')
                messages.success(request, "You're Logged In")
                if tutor.institution:
                    return redirect('tutor_dashboard')
                return redirect ('tutor_profile')

        else:
            tutor_exists = Tutor.objects.filter(username=username_or_email).exists()
            if tutor_exists:
                messages.error(request, 'Incorrect Password')
            else:
                messages.error(request, 'User Not Found')

            return render(request, 'tutor/tutor_login.html', context={'username_or_email': username_or_email})

    else:
        return render(request, 'tutor/tutor_login.html')
    


# Tutor Profile Update
# TODO: Update Result choices to accept choices other than first_class // Done

@login_required(login_url='tutor_login')
def tutor_profile(request):
    """profile update form"""
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
    tutor = Tutor.objects.filter(username=request.user.username).first()
    return render(request, 'tutor/tutor_dashboard.html', context={'tutor': tutor})


@login_required(login_url='client_signIn')
def view_tutors(request):
    """Displays all tutors"""
    subjects = Subject.objects.all()
    tutors = Tutor.objects.all()
    user = request.user
    return render(request, 'tutor/view_tutors.html', context={'tutors': tutors, 'subjects': subjects, 'user': user})


@login_required(login_url='client_signIn')
def search_tutors(request):
    """Search for tutors based on query"""
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
def tutor_detail(request, tutor_id):
    """Displays Tutor Public Profile"""
    user = request.user
    subjects = Subject.objects.all()
    tutors = Tutor.objects.all()
    reviews = Review.objects.filter(tutor=tutor_id).order_by('-created_at') 
    tutor = get_object_or_404(Tutor, id=tutor_id)
    context ={'tutor': tutor, 'user': user, 'subjects': subjects, 'reviews': reviews, 'tutors': tutors}
    return render(request, 'tutor/tutor_detail.html', context=context)




@login_required(login_url='client_signIn')
def submit_rank(request, tutor_id):
    if request.method == 'POST':
        tutor = Tutor.objects.get(pk=tutor_id)
        rank_number = int(request.POST.get('rank'))
        # Check if the client has already ranked this tutor
        existing_rank = Ranking.objects.filter(tutor=tutor, client=request.user).first()
        if existing_rank:
            existing_rank.rank_number = rank_number
            existing_rank.save()
        else:
            Ranking.objects.create(tutor=tutor, client=request.user, rank_number=rank_number)

        # Update the tutor's average rank
        tutor.update_rank(rank_number)

    return redirect('tutor_detail', tutor_id=tutor_id)


@login_required(login_url='client_signIn')
def submit_review(request, tutor_id):
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

        # Update the tutor's average rank

    return redirect('tutor_detail', tutor_id=tutor_id)

# Tutor Logout   
def tutor_logout(request):
    logout(request)
    messages.success(request, "You're Logged Out")
    return redirect('tutor_login') 

