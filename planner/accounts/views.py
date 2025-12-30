from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('tasks')
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')
        
    context = {'form' : form}
    return render(request, 'accounts/signup.html', context=context)



class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    success_message = "Welcome back! You have successfully logged in."

class CustomLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
             messages.success(request, "You have been logged out successfully.")
        return super().dispatch(request, *args, **kwargs)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')