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

        user_detail = UserDetail(
            username = username,
            email = email,
            mobile_number = mobile_number,
            message = message,
            ref_code = ref_code
        )
        user_detail.save()
        messages.success(request,'Your data successfully recivied')
        return redirect('/')
    else:
        messages.warning(request,'Your data successfully recivied')
        return redirect('/')




def client_dashboard(request):
    service = Service.objects.all()
    

