from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from Detail.models import Detail


# Create your views here.
def home(request):
    detail_data=Detail.objects.all()
    data={
        'title':'Home Page',
        'heading':'Welcome to Django Home Page...',
        "data":detail_data
    }
    return render(request,'index.html',data)

def about(request):
    return HttpResponse("<h1>This is About us page..</h1>")

def contact(request):
    return HttpResponse("<h1>This is Contact us page..</h1>")

def get_data(request,id):
    return HttpResponse(id)

def save_data(request):
    if request.method=='POST':
        nm=request.POST['name']
        addr=request.POST['addr']
        reg=Detail(name=nm,address=addr)
        reg.save()

        return redirect('/')

def delete_detail(request,id):
    delete=Detail.objects.get(id=id)
    delete.delete()
    return redirect('/')


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


def update_detail(request,id):
    get_data=Detail.objects.get(id=id)
    name=request.POST['name']
    address=request.POST['addr']
    get_data.name=name
    get_data.address=address
    get_data.save()
    return redirect('/')




   
