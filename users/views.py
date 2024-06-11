from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
    # else:
    #     form = UserRegisterForm()
def register(request):
    if request.user.is_authenticated:
        return redirect('blog:blog-home')
    else:
        form = UserRegisterForm()
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Acccount successfully created !')
            return redirect('login')


    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        prof_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            messages.success(request, f'Account has been updated !')
            return redirect('profile')
        
    user_form = UserUpdateForm(instance=request.user)
    prof_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'users/profile.html', context)
