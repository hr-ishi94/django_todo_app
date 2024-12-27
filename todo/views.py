from django.shortcuts import render,HttpResponse,redirect
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

from .forms import SignupForm, LoginForm, TodoForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        data = request.POST
        form = SignupForm(data)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            pass1 = form.cleaned_data['password']
            pass2 = form.cleaned_data['confirm_password']
            print(username, email)
            existing_user = User.objects.filter(Q(username=username) | Q(email=email))
            if existing_user.exists():
                messages.error(request, "User with the same username or email already exists!")
                return render(request, 'signup.html', {'form': form}) 
            
            if pass1 != pass2:
                messages.error(request,"Passwords didn't match!")
                return render(request, 'signup.html', {'form': form}) 

            
            
            user = User(username = username,email = form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request,"Account has been created!")
            
            return redirect('login_page')
        else:
            messages.error(request, "Invalid form submission. Please correct the errors below.")
            return render(request, 'signup.html', {'form': form})        
        
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

@login_required(login_url='login_page')
def todo(request):
    form = TodoForm(request.POST)
    user = request.user
    if request.method == "POST":
        if user.is_authenticated:    
            if form.is_valid():
                todo = Todo(text = form.cleaned_data['text'], user = request.user)
                todo.save()
        else:
            messages.error(request, "Login Required")
            return redirect('login_page')

        return redirect('todo')
    
    todos = Todo.objects.all() if user.is_authenticated else []
    form = TodoForm()
    return render(request,'todo.html',{'todos':todos, 'form':form})


def edit_todo(request,pk):
    if request.method == 'POST':
        text = request.POST.get('text')
        todo = Todo.objects.get(pk = pk)
        todo.text = text
        todo.save()
        print(f"Updated date: {todo.updated_date}")
        return redirect('todo')
    
def delete_todo(request,pk):
    try:
        todo = Todo.objects.get(pk = pk)
        todo.delete()
        return redirect('todo')
    except ValueError as e:
       raise Exception("Todo not found")
        
def signout(request):
    logout(request)
    return redirect('login_page')

