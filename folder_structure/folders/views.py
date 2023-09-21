from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Folder
from .forms import CreateUserForm
 


def register_page(request):
    if request.method == "POST":
        form = CreateUserForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = CreateUserForm()
            return render(request, 'folders/register.html', {'form': form})
    else:
        form = CreateUserForm()
        return render(request,'folders/register.html',{'form':form})


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Success')
            return redirect('home')
        else:
            messages.warning(request,'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request,'login.html')



def logout_page(request):
    logout(request)
    messages.success(request,'Logout Successful')
    return redirect('login')
    

@login_required
def folder_create(request, parent_id=None):
    parent_folder = None
    if parent_id:
        parent_folder = Folder.objects.get(pk=parent_id)

    if request.method == 'POST':
        folder_name = request.POST['folder_name']
        folder = Folder(name=folder_name, owner=request.user, parent=parent_folder)
        folder.save()
        return redirect('folder_list')

    return render(request, 'folders/folder_create.html', {'parent_folder': parent_folder})

@login_required
def folder_list(request):
    user_folders = Folder.objects.filter(owner=request.user, parent=None)
    return render(request, 'folders/folder_list.html', {'user_folders': user_folders})
