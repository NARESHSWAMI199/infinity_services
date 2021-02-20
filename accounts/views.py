from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.




def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request,user)
        messages.success(request,'welcome in infinity service. you have succesfully logged in')
        return redirect('/')
    context= {
        'form':form,
        'title': 'Login',
        'btn_label' : 'Submit'
    }
    return render(request,'login.html',context)





def registor_view(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2']:
            try:
                user =User.objects.get (username = request.POST['username'])
                return render (request,"singup.html",{'error':'user name already taken'})
            except:
                user =User.objects.create_user (username = request.POST['username'] , password =request.POST['password1'])
                auth.login(request,user)
                messages.success(request,'Thanks for use infinity services. you have logout successfully')
                return redirect('/')
        else:
            return render(request,'singup.html',{'error':"please confirm your password  are don't matched"})

    else:
        return render (request,"singup.html")



# def registor_view(request):
#     # this is a Model form
#     form = UserCreationForm(request.POST or None)
#     if form.is_valid():
#         user = form.cleaned_data('username')
#         password = form.cleaned_data('password2')
#         object = form.save(commit=False)
#         object.save()
   
#         messages.success(request,'welcome in infinity service. you have succesfully singup now go for login')
#         return redirect('/')
        
#     context= {
#         'form':form,
#         'title': 'Signup',
#         'btn_label' : 'Save'
#     }

    return render(request,'singup.html',context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(request,'Thanks for use infinity services. you have logout successfully')
        return redirect('/')
    
    context= {
        'title': 'Sign Out',
        'btn_label':'Logout'
    }
    return render(request,'login.html',context)