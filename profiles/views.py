from re import I
from django.shortcuts import redirect, render
from .serializers import Profile_Serializer
from rest_framework.response import Response
from .models import Profile
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from core.models import Service, UserDetail
from .forms import ProfileForm
from django.contrib import messages

@login_required
@api_view(['GET'])
def user_profile(request):
    qs = Profile.objects.filter(user = request.user)
    if qs.exists:
        qs = qs[0]
        serializer = Profile_Serializer(qs)
        return Response(serializer.data,status=200)
    return Response({'message':'there is no profile exists'},status=200)
    


@login_required
@api_view(['GET'])
def client_dashboard(request):
    qs = UserDetail.objects.filter(user=request.user)
    if qs.exists:
        context = {
            'items':qs,
        }
        return render(request,'dashboard.html',context)
    else:
        return redirect('/')


@login_required
def edit_dash(request):
    user = request.user 
    my_profile = user.profile
    form = ProfileForm(request.POST or None,request.FILES or None ,instance=my_profile)
    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        object  = form.save(commit=False)
        object.save()
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        object.user.save()
        messages.success(request,"your profile successfully updated ")
        return redirect('profiles:dashboard')
    context = {
        'form' :form
    }
    return render(request,'edit.html',context)


