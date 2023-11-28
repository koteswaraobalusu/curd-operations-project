from django.shortcuts import render,redirect
from .models import student
# Create your views here.
def mainpage(request):
    if request.method=="GET":
        data=student.objects.all()
        return render(request,'mainpage.html',{'data':data})
def createaccount(request):
    if request.method=="GET":
        return render(request,'createaccount.html')
    else:
        student(
        image=request.FILES.get('photo'),
        fname=request.POST.get('fname'),
        lname=request.POST.get('lname'),
        emailid=request.POST.get('email'),
        phone=request.POST.get('phone'),
        qualification=request.POST.get('qual'),
        location=request.POST.get('loc'),
        description=request.POST.get('about')
        ).save()
        return redirect('mainpage')
def update(request,id):
    if request.method=="GET":
        data=student.objects.get(id=id)
        return render(request,'update.html',{'data':data})
def update_data(request,id):
    data=student.objects.get(id=id)
    data.image=request.FILES.get('photo')
    data.fname=request.POST.get('fname')
    data.lname=request.POST.get('lname')
    data.emailid=request.POST.get('email')
    data.phone=request.POST.get('phone')
    data.qualification=request.POST.get('qual')
    data.location=request.POST.get('loc')
    data.description=request.POST.get('about')
    data.save()
    return redirect('mainpage')
def delete(request,id):
    data=student.objects.get(id=id)
    data.delete()
    return redirect('mainpage')
