from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, UserTypeForm
def index(request):
    return render(request,'base.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        user_type_form = UserTypeForm(request.POST)
        if form.is_valid() and user_type_form.is_valid():
            user = form.save()
            profile = user_type_form.save(commit=False)
            profile.user = user
            profile.is_doctor = user_type_form.cleaned_data['is_doctor']
            profile.save()

            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
        user_type_form = UserTypeForm()

    return render(request, 'signup.html', {'form': form, 'user_type_form': user_type_form})
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Add error handling for invalid login
            return render(request, 'signin.html', {'error_message': 'Invalid login credentials'})
    return render(request, 'signin.html')

@login_required
def dashboard(request):
    user_type = request.user.userprofile.is_doctor
    user_profile = request.user.userprofile

    context = {
        'user_type': 'Doctor' if user_type else 'Patient',
        'user_profile': user_profile,
        
    }

    if user_type:
        # Render doctor dashboard
        return render(request, 'doctor.html', context)
    else:
        # Render patient dashboard
        return render(request, 'patient.html', context)
