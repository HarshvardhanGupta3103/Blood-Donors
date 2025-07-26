from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
from .models import DonorRegistration
from django.contrib.auth.hashers import make_password, check_password
from datetime import date, timedelta
from django.db.models import Q


def index(request):
    return render(request, 'index.html')


def search(request):
    return render(request, 'search.html')


def about_us(request):
    return render(request, "About_us.html")


def contact_us(request):
    return render(request, "contact_us.html")




def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        birth_date = request.POST.get('birth_date')
        blood_group = request.POST.get('blood_group')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        occupation = request.POST.get('occupation')
        home_address = request.POST.get('home_address')
        last_donate_date = request.POST.get('last_donate_date')
        any_disease = request.POST.get('any_disease')
        allergies = request.POST.get('allergies')
        heart_condition = request.POST.get('heart_condition')
        bleeding_disorder = request.POST.get('bleeding_disorder')
        hiv_hcv = request.POST.get('hiv_hcv')
        aadhar_card = request.FILES.get('aadhar_card')
        username = request.POST.get('username')
        password = make_password(request.POST.get('password'))  # Hash the password

        # Check if username already exists
        if DonorRegistration.objects.filter(username=username).exists():
            return render(request, 'registration.html', {'error': "Username already exists."})

        # Handle empty date fields properly
        if not last_donate_date or last_donate_date.strip() == '':
             return render(request, 'registration.html', {'error': "last_donate_date is required."})
        
        # Validate birth_date
        if not birth_date or birth_date.strip() == '':
            return render(request, 'registration.html', {'error': "Birth date is required."})
            
        try:
            # Save new donor
            DonorRegistration.objects.create(
                name=name,
                gender=gender,
                birth_date=birth_date,
                blood_group=blood_group,
                phone_number=phone_number,
                email=email,
                occupation=occupation,
                home_address=home_address,
                last_donate_date=last_donate_date,
                any_disease=any_disease or 'no',
                allergies=allergies or 'no',
                heart_condition=heart_condition or 'no',
                bleeding_disorder=bleeding_disorder or 'no',
                hiv_hcv=hiv_hcv or 'no',
                aadhar_card=aadhar_card,
                password=password,
                username=username
            )
        except Exception as e:
            return render(request, 'registration.html', {'error': f"Registration failed: {str(e)}"})

        return render(request, "login.html", {'msg': "Registered successfully!"})

    return render(request, "registration.html")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = DonorRegistration.objects.get(username=username)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                return render (request,'index.html',{'msg': "login successfully "})
            else:
                return render(request, 'login.html', {'error': "Invalid username or password."})
        except DonorRegistration.DoesNotExist:
            return render(request, 'login.html', {'error': "Invalid username or password."})
    
    return render(request, 'login.html')


def user_logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['username']
    return redirect('home')


def account(request):
    if 'user_id' not in request.session:
        return redirect('user_login')
    
    try:
        user = DonorRegistration.objects.get(id=request.session['user_id'])
        return render(request, 'account.html', {'user': user})
    except DonorRegistration.DoesNotExist:
        return redirect('user_login')


# def showdata(request):
#     if 'user_id' not in request.session:
#         return redirect('user_login')
    
#     try:
#         user = DonorRegistration.objects.get(id=request.session['user_id'])
#         return render(request, 'account.html', {'user': user})
#     except DonorRegistration.DoesNotExist:
#         return redirect('user_login')


def edit_profile(request):
    if 'user_id' not in request.session:
        return redirect('user_login')
    
    try:
        user = DonorRegistration.objects.get(id=request.session['user_id'])
    except DonorRegistration.DoesNotExist:
        return redirect('user_login')
    
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.gender = request.POST.get('gender')
        user.birth_date = request.POST.get('birth_date')
        user.blood_group = request.POST.get('blood_group')
        user.phone_number = request.POST.get('phone_number')
        user.email = request.POST.get('email')
        user.occupation = request.POST.get('occupation')
        user.home_address = request.POST.get('home_address')
        last_donate_date = request.POST.get('last_donate_date')
        user.last_donate_date = last_donate_date if last_donate_date and last_donate_date.strip() else None
        user.any_disease = request.POST.get('any_disease') or 'no'
        user.allergies = request.POST.get('allergies') or 'no'
        user.heart_condition = request.POST.get('heart_condition') or 'no'
        user.bleeding_disorder = request.POST.get('bleeding_disorder') or 'no'
        user.hiv_hcv = request.POST.get('hiv_hcv') or 'no'

        if request.FILES.get('aadhar_card'):
            user.aadhar_card = request.FILES['aadhar_card']

        try:
            user.save()
            return redirect('account')
        except Exception as e:
            return render(request, 'edit.html', {'user': user, 'error': f"Update failed: {str(e)}"})

    return render(request, 'edit.html', {'user': user})


# def searchDta(request):
#     if request.method == 'POST':
#         blood_group = request.POST.get('blood_group')
#         home_address = request.POST.get('home_address')
        
#         # Validate input
#         if not blood_group or not home_address:
#             error_msg = "Please provide both blood group and location."
#             return render(request, 'search.html', {'donors': None, 'error': error_msg})
        
#         today = date.today()
#         eighteen_years_ago = date(today.year - 18, today.month, today.day)
#         ten_days_ago = today - timedelta(days=10)

#         try:
#             donors = DonorRegistration.objects.filter(
#                 blood_group__iexact=blood_group,
#                 home_address__icontains=home_address,
#                 birth_date__lte=eighteen_years_ago
#             ).filter(
#                 # Include first-time donors (null) OR those who donated 10+ days ago
#                 Q(last_donate_date__isnull=True) | Q(last_donate_date__lte=ten_days_ago)
#             ).filter(
#                 Q(any_disease__iexact='no') | Q(any_disease__iexact='none') | Q(any_disease__isnull=True) | Q(any_disease='')
#             ).filter(
#                 Q(allergies__iexact='no') | Q(allergies__iexact='none') | Q(allergies__isnull=True) | Q(allergies='')
#             ).filter(
#                 Q(heart_condition__iexact='no') | Q(heart_condition__iexact='none') | Q(heart_condition__isnull=True) | Q(heart_condition='')
#             ).filter(
#                 Q(bleeding_disorder__iexact='no') | Q(bleeding_disorder__iexact='none') | Q(bleeding_disorder__isnull=True) | Q(bleeding_disorder='')
#             ).filter(
#                 Q(hiv_hcv__iexact='no') | Q(hiv_hcv__iexact='none') | Q(hiv_hcv__isnull=True) | Q(hiv_hcv='')
#             ).values('name', 'phone_number', 'blood_group', 'home_address')

#             if donors:
#                 return render(request, 'search.html', {'donors': donors})
#             else:
#                 message = f"No eligible donors found for {blood_group} blood group in {home_address} area. Please try a different location or contact us for assistance."
#                 return render(request, 'search.html', {'donors': None, 'message': message})
        
#         except Exception as e:
#             error_msg = f"Search failed: {str(e)}"
#             return render(request, 'search.html', {'donors': None, 'error': error_msg})
    
#     return render(request, 'search.html', {'donors': None})


def searchDta(request):
    if request.method == 'POST':
        blood_group = request.POST.get('blood_group')
        home_address = request.POST.get('home_address')
        
        # Validate input
        if not blood_group or not home_address:
            error_msg = "Please provide both blood group and location."
            return render(request, 'search.html', {'donors': None, 'error': error_msg})
        
        today = date.today()
        eighteen_years_ago = date(today.year - 18, today.month, today.day)
        ten_days_ago = today - timedelta(days=10)

        try:
            donors = DonorRegistration.objects.filter(
                blood_group__iexact=blood_group,
                home_address__icontains=home_address,
                birth_date__lte=eighteen_years_ago
            ).filter(
                Q(last_donate_date__isnull=True) | Q(last_donate_date__lte=ten_days_ago)
            ).filter(
                Q(any_disease__iexact='no') | Q(any_disease__iexact='none') | Q(any_disease__isnull=True) | Q(any_disease='')
            ).filter(
                Q(allergies__iexact='no') | Q(allergies__iexact='none') | Q(allergies__isnull=True) | Q(allergies='')
            ).filter(
                Q(heart_condition__iexact='no') | Q(heart_condition__iexact='none') | Q(heart_condition__isnull=True) | Q(heart_condition='')
            ).filter(
                Q(bleeding_disorder__iexact='no') | Q(bleeding_disorder__iexact='none') | Q(bleeding_disorder__isnull=True) | Q(bleeding_disorder='')
            ).filter(
                Q(hiv_hcv__iexact='no') | Q(hiv_hcv__iexact='none') | Q(hiv_hcv__isnull=True) | Q(hiv_hcv='')
            ).values('name', 'phone_number', 'blood_group', 'home_address')

            if donors:
                return render(request, 'search.html', {'donors': donors})
            else:
                message = f"No eligible donors found for {blood_group} blood group in {home_address} area. Please try a different location or contact us for assistance."
                return render(request, 'search.html', {'donors': None, 'message': message})

        except Exception as e:
            error_msg = f"Search failed: {str(e)}"
            return render(request, 'search.html', {'donors': None, 'error': error_msg})
    
    # For non-POST requests, simply render the search form with no results
    return render(request, 'search.html', {'donors': None})