from email.policy import default
import re
from traceback import print_tb
from unicodedata import name
from django.shortcuts import render,redirect

from django.template import RequestContext

from django.http import HttpResponse,HttpResponseRedirect
from Detail.models import Detail
from login.models import login as NewUser
from django.contrib.auth import authenticate,login
from django.views.decorators.cache import cache_control


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def home(request):
    if 'name' in request.session:
        name=request.session['name']
        email=request.session['email']
        detail_data=Detail.objects.all()
        data={
            'title':'Home Page',
            'heading':'Welcome to Django Home Page...',
            "data":detail_data,
            'name':name,
            'email':email
        }
        return render(request,'index.html',data)
    else:
        return redirect('/login/')


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def about(request):
    return HttpResponse("<h1>This is About us page..</h1>")


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def contact(request):
    return HttpResponse("<h1>This is Contact us page..</h1>")


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def get_data(request,id):
    return HttpResponse(id)


@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def save_data(request):
    if request.method=='POST':
        nm=request.POST['name']
        addr=request.POST['addr']
        reg=Detail(name=nm,address=addr)
        reg.save()

        return redirect('/')
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def delete_detail(request,id):
    delete=Detail.objects.get(id=id)
    delete.delete()
    return redirect('/')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def edit_detail(request,id):
    single_data=Detail.objects.get(id=id)
    detail_data=Detail.objects.all()
    data={
        'title':'Home Page',
        'heading':'Welcome to Home Page...',
        'single_data':single_data,
        "data":detail_data
    }
    return render(request,'index.html',data)

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def update_detail(request,id):
    get_data=Detail.objects.get(id=id)
    name=request.POST['name']
    address=request.POST['addr']
    get_data.name=name
    get_data.address=address
    get_data.save()
    return redirect('/')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def login(request):
    if 'name' not in request.session:
        status=""
        return render(request,'login.html',{'status':status})
    else:
        return redirect('/')
        

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def logout(request):
    if 'name' in request.session:
        for key in list(request.session.keys()):
            del request.session[key]
        status="You are Loged Out.."
        
        return redirect('/login/')
    else:
        return redirect('/')

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def login_store(request):
  if 'name'  in request.session:
    return redirect('/')
  else:
    if request.method=="POST":
          email=request.POST['email']
          password=request.POST['password']
          try:
                user = NewUser.objects.get(email=email)
              
          except Exception as e:
                user= None
         
          if user is not None:
         
             if user.password==password:
                 request.session['name']=user.name
                 request.session['email']=user.email
                 return redirect('/')
             else:
                status="passeord Not Correct.."
                return render(request,'login.html',{'status':status})
          else:
             status="invalid Details.."
             return render(request,'login.html',{'status':status})
   
     
@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def register(request):
    if 'name'  in request.session:
        return redirect('/')
    else:
        status='';
        return render(request,'register.html',{"status":status})

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def store_register(request):
   if 'name'  in request.session:
        return redirect('/')
   else:
    if request.method=='POST':
        u_name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        c_password=request.POST.get('c_password')
 
        if password==c_password:
            create_data=NewUser(name=u_name,email=email,password=password)
            create_data.save()
            if create_data:
                status="Restration Successfull"
                return redirect('/login/')
        else:
            
                status="Password and Confirm password must be same..."
                return render(request,'register.html',{"status":status})


      
    else:
        status='Please Enter Details...'
        return render(request,'register.html',{"status":status})

@cache_control(no_cache=True, must_revalidate=True,no_store=True)
def session_set(request):
    request.session['name']='ASHISH'
    return render(request,'session_set.html')

def session_get(request):
    name=request.session.get('name', default='Guest')
    return render(request,'session_get.html',{'name':name})


def session_delete(request):
    if 'name' in request.session:
     del request.session['name']
    return render(request,'session_delete.html')



# HTTP Error 400
def bad_request(request, exception):
   context = {}
   return render(request,'404.html', context)



   
