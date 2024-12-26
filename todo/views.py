from django.shortcuts import render,HttpResponse,redirect
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from .forms import SignupForm, LoginForm, TodoForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        data = request.POST
        form = SignupForm(data)
        
        if form.is_valid():
            user = User(username = form.cleaned_data['username'],email = form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            
        return redirect('login_page')
    else:
        form = SignupForm()

    return render(request, 'signup.html',{ 'form' : form })

def login_page(request):
    if request.method == 'POST':
        data = request.POST
        form = LoginForm(data)
        if form.is_valid():
            # print(form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user  = authenticate(request, username = username, password = password)
            print(user)
            if user:
                login(request,user)
                return redirect('todo')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request,"Please check all fields")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form' : form } )

def todo(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        user = request.user
        print(user)
        if user:    
            if form.is_valid():
                todo = Todo(text = form.cleaned_data['text'], user = request.user)
                todo.save()
        else:
            messages.error(request, "Login Required")
            return redirect('login_page')

    else:
        form = TodoForm()
    return render(request, 'todo.html',{'form' : form})
