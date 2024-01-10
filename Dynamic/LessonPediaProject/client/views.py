from django.contrib.auth import login, logout, update_session_auth_hash
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .backends import EmailClientBackend as ClientBackend
from django.contrib import messages
from .form import UserProfileRegistrationForm
from .models import Client, Cart, Tutor, Ranking, Review, Transaction
from generic_apps.models import Contract
from decimal import Decimal
from django.http import HttpResponse, JsonResponse
import json
import re

def logout_required(view_func):
    """Decorator to require the user to be logged out to access a view."""
    def _wrapped_view(request):
        if request.user.is_authenticated and "client" in request.path:
            messages.error(request, f"{request.user} is already Signed in, please Sign Out!")
            return redirect('landing_page') 
        return view_func(request) 
    return _wrapped_view

@logout_required
def client_login(request):
    """client Login logic"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        if 'client' in request.path:
            clientAuth = ClientBackend()
            user = clientAuth.authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_active == 1:
                    if user.deactivateByClient == 1:
                        login(request, user, backend='client.backends.EmailClientBackend')
                        next_param = request.POST.get('next', request.GET.get('next'))
                        if next_param:
                            return redirect(next_param)
                        else:
                            return redirect("landing_page")
                    else:
                        messages.error(request, "This account has been deactivated by User")
                else:
                    messages.error(request, "This account has been suspended by Admin")
            else:
                messages.error(request, "Invalid User Credentials for client")
                return render(request, 'client/login.html') 
              
    return render(request, 'client/login.html')

@login_required(login_url='client_signIn')
def client_logout(request):
    """Logout active user"""
    logout(request)
    return redirect('landing_page')

@login_required(login_url='client_signIn')
def user_profile_registration(request):
    """Profile registration page"""
    current_user = request.user
    user_profile = Client.objects.get(username=current_user)
    if request.method == "POST":
        form = UserProfileRegistrationForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect("validate_user", whoami=request.user)
        else:
            print(form.errors)
            return HttpResponse("Invalid form")
    else:
        form = UserProfileRegistrationForm()
        return render(request, 'client/profilePageUpdate.html', {"form": form, "activeUser": request.user})

@login_required(login_url='client_signIn')
def render_dashboard(request, whoami, tutorId=None):
    """validate user and render dashboard
    or redirect user to register profile page"""

    user = Client.objects.get(username=whoami)
    address = user.residential_address

    if address:
        getAllTutors = Cart.objects.filter(client_id=request.user).all()
        countTutors = getAllTutors.filter(client_id=request.user.id).count()
        pendingRequest = Contract.objects.filter(contract_status="Pending").count()
        activeRequest = Contract.objects.filter(contract_status="Active").count()
        declinedRequest = Contract.objects.filter(contract_status="Declined").count()
        allReviews = Review.objects.filter(client=request.user.id).all()

        aggregate = pendingRequest + activeRequest + declinedRequest
        notEngaged = countTutors - aggregate

        # Pagination
        # page = request.GET.get('page', 1)
        # paginator = Paginator(getAllTutors, 3) 
        # try:
        #     tutors = paginator.page(page)
        # except PageNotAnInteger:
        #     tutors = paginator.page(1)
        # except EmptyPage:
        #     tutors = paginator.page(paginator.num_pages)

        # Hangle ajax dataw54eryt
        get_ajax_data = request.GET.get('tutorId')
        if get_ajax_data:
            """return object of selected tutor"""
            rank = Ranking.objects.filter(tutor_id=get_ajax_data, client=request.user).first()
            rankByUser = rank.rank_number if rank else 0
            return JsonResponse({'rank': rankByUser})

        return render(request, 'client/client_dashboard.html', {'tutors': getAllTutors, 'totalTutors': countTutors, 'reviews': allReviews, 'pendingStatus': pendingRequest, 'activeStatus': activeRequest, 'notEngagedStatus': notEngaged, 'declinedStatus': declinedRequest})
    else:
        return redirect('user_profile')


@login_required(login_url="client_signIn")
def search_algorithm(request, keyword):
    """Return all tutors that matches the keyword"""
    user = Client.objects.get(username=request.user)
    address = user.residential_address
    if address:
        filtered_keyword = Cart.objects.filter(Q(target_tutor__first_name__icontains=keyword) | Q(target_tutor__last_name__icontains=keyword), client=request.user).all()
        getAllTutors = Cart.objects.filter(client_id=request.user.id).all()
        countTutors = getAllTutors.filter(client_id=request.user.id).count()
        
        return render(request, 'client/client_dashboard.html', {'tutors': filtered_keyword, 'totalTutors': countTutors})
  
    return redirect('validate_user', whoami=request.user)

@login_required(login_url='/landing_page/')
def ClientProfileUpdate(request):
    """User profile update from dashboard"""
    activeUser = request.user
    if request.method == "POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        phoneNumbs = request.POST.get('phoneNumber')
        residentAddress = request.POST.get('address')
        state_Residence = request.POST.get('state')
        national = request.POST.get('nationality')
        eduLevel = request.POST.get('eduLevel')
        specifics = request.POST.get('specifics')
        channel = request.POST.get('channel')
        tutorGender = request.POST.get('tutorGender')
        
        if firstName:
            activeUser.first_name = firstName
        if lastName:
            activeUser.last_name = lastName
        if phoneNumbs:
            activeUser.phone_number = phoneNumbs
        if residentAddress:
            activeUser.residential_address = state_Residence
        if national:
            activeUser.nationality = national
        if eduLevel:
            activeUser.educational_level = eduLevel
        if specifics:
            activeUser.specific_educational_level = specifics
        if channel:
            activeUser.prefered_channel = channel
        if tutorGender:
            activeUser.prefered_tutor_gender = tutorGender

        if firstName or lastName or phoneNumbs or residentAddress or national or eduLevel or specifics or channel or tutorGender:
            messages.success(request, "User Profile Succesfully Updated")
            activeUser.save()
        else:
            messages.error(request, "No field was Updated")
        return redirect("validate_user", whoami=request.user)

@login_required(login_url='/landing_page/')
def ClientChangePassword(request):
    """Change User Password"""
    activeUser = request.user
    if request.method == 'POST':
        old_password = request.POST.get('oldPassword')
        new_password = request.POST.get('newPassword')
        confirm_new_password = request.POST.get('confirmNewPassword')
        form = PasswordChangeForm(activeUser, {'old_password': old_password, 'new_password1': new_password, 'new_password2': confirm_new_password})
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password Successfully Updated")
            return redirect("validate_user", whoami=request.user)
        elif form.errors:
            try:
                for field, errors in form.errors.items():
                    form = PasswordChangeForm(activeUser)
                    messages.error(request, f"{field.title()}: {errors[0]}")
                    #break
                    return render(request, 'client/client_dashboard.html')
            except Exception:
                return HttpResponse("An error occurred. Please try again later.")
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'client/client_dashboard.html')

@login_required(login_url='/landing_page/')
def deactivate_account(request):
    """deactivate account as requested by user"""
    activeUser = request.user
    activeUser.deactivateByClient = False
    activeUser.save()
    return redirect("logoutUser")

@login_required(login_url='client_signIn')
def profilePictureUpdate(request):
    """Update user profile picture"""
    activeUser = request.user
    if request.method == "POST":
        profilePicture = request.FILES.get('profilePicture')
        if profilePicture:
            get_previous_picture = activeUser.profile_picture
            if get_previous_picture:
                get_previous_picture.delete()
            activeUser.profile_picture = profilePicture
            activeUser.save()
            messages.success(request, "Profile Picture Succesfully Updated")
        else:
            messages.error(request, "No file was Uploaded")
        return redirect("validate_user", whoami=request.user)

@login_required(login_url='client_signIn')
def addTutor_2_cart(request, tutorId):
    """Add selected tutor to user Dashboard"""
    getThisTutor = get_object_or_404(Tutor, id=tutorId)
    inspectTutor = Cart.objects.filter(target_tutor=getThisTutor, client=request.user).all()
    for ids in inspectTutor:
        if ids.target_tutor.id == tutorId:
            messages.error(request, "Tutor already added to cart")
            return redirect('validate_user', whoami=request.user)
    obtained = Cart(
        target_tutor=getThisTutor,
        client = request.user,
    )
    obtained.save()
    messages.success(request, "Tutor successfully added to cart")
   
    return redirect('validate_user', whoami=request.user)

@login_required(login_url='client_signIn')
def removeTutorFromCart(request, tutorId):
    """Remove selected tutor from user Dashboard"""
    getTutor = Cart.objects.filter(target_tutor_id=tutorId, client=request.user).first()
    deleteContract = Contract.objects.filter(tutor=tutorId, client=request.user).first()
    if deleteContract:
        deleteContract.delete()
    if getTutor:
        getTutor.delete()
        messages.success(request, "Tutor successfully removed from cart")
        return redirect('validate_user', whoami=request.user)
    messages.error(request, "Tutor not found in cart")
    return redirect('validate_user', whoami=request.user)

@login_required(login_url="client_signIn")
def tutors_ranking(request, tutorId, rankValue):
    """Rank tutor based on their performance and client satisfaction"""
    getTutor = get_object_or_404(Tutor, id=tutorId)
    queryRanks = Ranking.objects.filter(tutor=getTutor, client=request.user).first()
    if queryRanks:
        queryRanks.rank_number = rankValue
        queryRanks.save()
        messages.success(request, "Ranking successfully updated")
        return redirect('validate_user', whoami=request.user)
    rank = Ranking(
        rank_number=rankValue,
        tutor=getTutor,
        client=request.user,
    )
    try:
        rank.save()
        messages.success(request, "Ranking added successfully")
        return redirect('validate_user', whoami=request.user)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@login_required(login_url="client_signIn")    
def review_tutor_ajax(request, tutorId):
    """Review active tutor"""
    queryTutor = Tutor.objects.get(pk=tutorId)
    AvgRank = Ranking().rankAverage(tutorId)
    data = {
        'Temail': queryTutor.email,
        'TfirstName': queryTutor.first_name,
        'TlastName': queryTutor.last_name,
        'Tqualification': queryTutor.highest_qualification,
        'Trank': AvgRank['avg_rank'],
        'dp': queryTutor.profile_picture.url,
        'id': tutorId
    }
    return JsonResponse({'Rtutor': data})

@login_required(login_url="client_signIn")
def submit_review(request, tutorId):
    """Submit Review based on active user"""
    tutor = get_object_or_404(Tutor, pk=tutorId)
    client = request.user
    if request.method == "POST":
        subject = request.POST.get('subject')
        body = request.POST.get('reviewContent')
        storage = Review(
            review_subject=subject,
            review_text=body,
            client=client,
            tutor=tutor
        )
        storage.save()
        messages.success(request, "Review was successfull")
    return redirect('validate_user', whoami=request.user)

@login_required(login_url="client_signIn")
def edit_review(request, tutorId):
    """Edit Review based on active user"""
    tutor = get_object_or_404(Tutor, pk=tutorId)
    checkForUpdate = Review.objects.filter(client=request.user, tutor=tutor).first()
    client = request.user
    if request.method == "POST":
        subject = request.POST.get('subject')
        body = request.POST.get('reviewContent')
        if subject == None or body == None or body == checkForUpdate.review_text and subject == checkForUpdate.review_subject:
            messages.error(request, "No changes was made")
            return redirect('validate_user', whoami=request.user)
        storage = Review.objects.filter(client=client, tutor=tutor).first()
        storage.review_subject = subject
        storage.review_text = body
        storage.save()
        messages.success(request, "Review was successfull")
    return redirect('validate_user', whoami=request.user)

@login_required(login_url="client_signIn")
def contract_information(request):
    """return an API for contract"""
    userCart = Cart.objects.filter(client=request.user).all()
    data = {}
    for content in userCart:
        contractData = Contract.objects.filter(tutor=content.target_tutor.id).all()
        for value in contractData:
            storage = {
                value.tutor.id : {
                    "status": value.contract_status,
                    "amount": value.contract_amount,
                    "contractId": value.contract_code,
                    "endDate": value.end_date,
                    "paid": value.payment_made,
                    "amountRemaining": value.payment_remaining,
                    "paymentMade": value.payment_made,
                }
            }
            data.update(storage)

    return JsonResponse(data)

@login_required(login_url="client_signIn")
def transaction_information(request):
    """returns an API for transaction"""
    usercart = Cart.objects.filter(client=request.user).all()
    transactionData = {}

    for content in usercart:
        transactionData[content.target_tutor.id] = {}
        transaction_info = Transaction.objects.filter(tutor=content.target_tutor.id).all()

        for value in transaction_info:
            storage = {
                "referenceId": value.referenceNumber,
                "transactionId": value.tnx_id,
                "transactionStatus": value.tnx_status,
                "transactionMessage": value.tnx_message,
            }
            transactionData[content.target_tutor.id][value.tnx_id] = storage

    return JsonResponse(transactionData)

@login_required(login_url="client_signIn")
def paystackGateway(request, tutorId):
    """Payment gateway Logics with Paystack"""
    tutorContract = Contract.objects.filter(tutor=tutorId).first()
    tutorDetails = Tutor.objects.filter(id=tutorId).first()
    return render(request, "client/paystack.html", {"tutor": tutorDetails, "contract": tutorContract})

@login_required(login_url="client_signIn")
def transactionDetails_storage(request, tutorId):
    """Update basic information after payment"""
    amount = None
    if request.method == 'POST':
        contract_id = request.POST.get("contractId")
        amount = request.POST.get("amount")
        payment_type = request.POST.get("paymentType")
        reference_id = request.POST.get("referenceId")
        transaction_status = request.POST.get("transactionStatus")
        transaction_message = request.POST.get("transactionMessage")
        transaction_id = request.POST.get("transactionId")
        tutor = Tutor.objects.filter(id=tutorId).first()

        contractUpdate = Contract.objects.filter(contract_code=contract_id).first()
        contractUpdate.payment_made = contractUpdate.payment_made + Decimal(amount)
        contractUpdate.save()

        storeTransactionDetails = Transaction(
            referenceNumber=reference_id,
            tnx_id=transaction_id,
            tnx_status=transaction_status,
            tnx_amount=amount,
            client=request.user,
            tutor=tutor,
            tnx_message=transaction_message
        )
        storeTransactionDetails.save()

    return JsonResponse({'data': amount})
 