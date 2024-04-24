from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from next_app.forms import Admin_User_Form,Common_User_Form,Admin_User_AddForm,Common_User_AddForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from next_app.models import Admin_User,Common_User
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request,'gradesApp/index.html')

@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    return render(request,'gradesApp/register.html')

def registerStudent(request):
    registered=False
    if request.method=='POST':
        var_adminForm=Admin_User_Form(request.POST)
        var_adminAddForm=Admin_User_AddForm(request.POST)
        if var_adminForm.is_valid()and var_adminAddForm.is_valid():
            adminprimary=var_adminForm.save()
            adminprimary.set_password(adminprimary.password)
            adminprimary.save()
            adminAdd=var_studentAddForm.save(commit=False)
            studentAdd.admin_user=studentprimary
            studentAdd.save()
            registered=True
    else:
        var_studentForm=Admin_User_Form()
        var_studentAddForm=Admin_User_AddForm()
    data={
        'var_studentForm':var_studentForm,
        'var_studentAddForm':var_studentAddForm,
        'registered':registered
        }
    return render(request,'gradesApp/registerStudent.html',data)


def registerTeacher(request):
    registered=False
    if request.method=='POST':
        var_teacherForm=Common_User_Form(request.POST)
        var_teacherAddForm=Common_User_AddForm(request.POST)
        if var_teacherForm.is_valid()and var_teacherAddForm.is_valid():
            teacherprimary=var_teacherForm.save()
            teacherprimary.set_password(teacherprimary.password)
            teacherprimary.save()
            teacherAdd=var_teacherAddForm.save(commit=False)
            teacherAdd.common_user=teacherprimary
            teacherAdd.save()
            registered=True
    else:
        var_teacherForm=Common_User_Form()
        var_teacherAddForm=Common_User_AddForm()
    data={
        'var_teacherForm':var_teacherForm,
        'var_teacherAddForm':var_teacherAddForm,
        'registered':registered}
    return render(request,'gradesApp/registerTeacher.html',data)
    
def userLogin(request):
    invalidlogin=False
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin=True
            return redirect('/gradesApp/login/')
    else:
        return render(request,'gradesApp/login.html',{'invalidlogin':invalidlogin})


# from django.shortcuts import render, redirect
# from .models import Admin_User, Common_User
# from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    print("request",request.user)
    try:
        current=Admin_User.objects.get(admin_user=request.user)
        print("current",current)
        is_admin_user = True
    except Admin_User.DoesNotExist:
        current=Common_User.objects.get(common_user=request.user)
        print("current",current)
        is_admin_user = False

    if is_admin_user:
        return redirect('/studentDash/')
    else:
        return redirect('/teacherDash/')
    return render(request,'gradesApp/dashboard.html')




from django.shortcuts import render, redirect
from .models import Admin_User, Common_User
from django.contrib.auth.decorators import login_required


# @login_required
# def dashboard(request):
#     print("request", request.user)
#     try:
#         # Try to fetch the Admin_User object for the current user
#         current = Admin_User.objects.get(admin_user=request.user)
#         is_admin_user = True
#     except Admin_User.DoesNotExist:
#         # If Admin_User object is not found, try fetching Common_User object
#         try:
#             current = Common_User.objects.get(common_user=request.user)
#             is_admin_user = False
#         except Common_User.DoesNotExist:
#             # If neither Admin_User nor Common_User object is found, handle the situation here
#             # For example, you might want to redirect to a page showing an error message
#             return render(request, 'gradesApp/error.html')

    # if is_admin_user:
    #     return redirect('/studentDash/')
    # else:
    #     return redirect('/teacherDash/')




def studentDash(request):
    return render(request,'gradesApp/studentDash.html')

def teacherDash(request):
    return render(request,'gradesApp/teacherDash.html')