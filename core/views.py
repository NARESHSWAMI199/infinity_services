from django.db.models.base import Model
from django.shortcuts import redirect, render,get_object_or_404
from .models import Service,UserDetail
from django.contrib import messages



# Create your views here.
def home(request):
    objects  = Service.objects.all()
    context = { 'objects' : objects }
    return render(request,"index.html",context)

def detail_view(request,id):
    # this is added for only show nav serrvices
    objects  = Service.objects.all()
    object  = get_object_or_404(Service,pk=id)
    context  = {'object': object,
    'objects' : objects  }
    return render(request,'detail.html',context)

    


def client_detail(request):
    if request.method =="POST":
        username = request.POST['username']
        email = request.POST['email']
        mobile_number = request.POST['mob_number']
        message = request.POST['message']
        ref_code = request.POST['ref_code']
        work = request.POST['work']

        qs = Service.objects.filter(title = work)
        if qs.exists:
            object = qs.first()
            user_detail = UserDetail(
                user = request.user,
                username = username,
                email = email,
                mobile_number = mobile_number,
                message = message,
                ref_code = ref_code,
            )
            user_detail.save()
            user_detail.work.add(object)
            user_detail.save()
            messages.success(request,'Your data successfully recivied')
            return redirect('/')
        else:
            messages.warning(request,'something went wrong check any field not empty')
            return redirect('/')





    

