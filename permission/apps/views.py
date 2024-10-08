from django.shortcuts import render, redirect
from .forms import Signupform,Loginform
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def index(request):
    return render(request,'index.html')
def signup(request):
    if request.method == 'POST':
        form = Signupform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/logins')
    else:
        form= Signupform()
    return render(request, 'signup.html', {'form': form})


  def logins(request):
    if request.method=='POST':
        form=Loginform(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                return redirect('index')

        form=Loginform()
    return render(request,'login.html',{'form':form})


def logouts(request):
    logout(request)
    return redirect('/signup')

