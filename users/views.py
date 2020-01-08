from django.shortcuts import render, redirect
from .forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username    = form.cleaned_data.get('username')
            messages.success(request,f'{username} Registered')
            return redirect('users-login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', { 'form':form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')