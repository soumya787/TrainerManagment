from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.cache import never_cache

from Trainerapp.models import City, Course, Trainer_Reg, Trainer_Batch_Assign

@never_cache
def reg_fun(request):
    city_data=City.objects.values()
    course_data=Course.objects.values()
    data={
        'city': city_data,
        'course': course_data,
        'data1':''
    }
    return render(request,'register.html',data)

@never_cache
def reg_data_fun(request):
    uname = request.POST['txtName']
    uage = request.POST['txtAge']
    uphno = request.POST['txtPhNo']
    upassword = request.POST['txtPass']
    uemail = request.POST['txtEmail']
    ucity = request.POST['ddlCity']
    ucourse = request.POST['ddlCourse']
    usertype = request.POST['rdUsrType']
    if usertype == 'Admin':
        u1=User.objects.create_superuser(username=uname,password=upassword,email=uemail)
        u1.save()
        return redirect('log')
    elif usertype == 'Trainer':
        t1=Trainer_Reg()
        t1.Tname=uname
        t1.Tage=uage
        t1.TPhno=uphno
        t1.Temail=uemail
        t1.Tpassword=upassword
        t1.Tcity=City.objects.get(city_name=ucity)       #returned object of city_name is assigned to ucity
        t1.Tcourse=Course.objects.get(course_name=ucourse)
        t1.save()
        return redirect('log')
    else:
        return redirect('register',{'data1':'Enter Valid Data'})

@never_cache
def log_fun(request):
    return render(request,'login.html',{'data2':''})

@never_cache
def log_read_fun(request):
    user_name=request.POST['txtName']
    user_password=request.POST['txtPass']
    myuser=authenticate(username=user_name,password=user_password)
    if myuser is not None:
        if myuser.is_superuser:
            u1=User.objects.get(username=user_name)
            request.session['myuser']=u1.id  #based on the id we are getting a details
            return render(request,'admin//admin_home.html',{'data':u1.username})
    elif Trainer_Reg.objects.filter(Tname=user_name,Tpassword=user_password).exists():
        t1 = Trainer_Reg.objects.get(Tname=user_name)
        request.session['trainer'] = t1.id
        return render(request,'trainer//trainer_home.html',{'data':t1.Tname})
    else:
        return render(request,'login.html',{'data2':'credential is not matching!!!'})


# --------------------------------
# Admin Page functions 
#-------------------------------------
@never_cache
def admin_home_fun(request):
    u1=User.objects.get(id=request.session['myuser']) 
    return render(request,'admin//Admin_home.html',{'data':u1.username})

@never_cache
def trainer_details(request):
    t1=Trainer_Reg.objects.all()
    return render(request,'admin//trainer_details.html',{'data3':t1})

@never_cache
def batch_data_fun(request):
    b1=Trainer_Reg.objects.values()#trainer details
    cc1=Course.objects.values() #course details
    return render(request,'admin//BatchAssign.html',{'data':b1,'data2':cc1})

import pywhatkit as pwt
from datetime import datetime

@never_cache
def batch_assign_fun(request):
    t1 = Trainer_Batch_Assign()
    t1.Tr_name = Trainer_Reg.objects.get(Tname= request.POST['ddlName'])
    t1.BatchNo = request.POST['numBatch']
    t1.Date = request.POST['datetime']
    t1.Tr_Course = Course.objects.get(course_name=request.POST['ddlcourse'])
    t1.save()

    c1 = Course.objects.get(course_name=request.POST['ddlcourse'])
    t = Trainer_Reg.objects.get(Tname=request.POST['ddlName'])
    s = f'{t1.BatchNo} and course {c1.course_name} starts from {t1.Date}'
    s1 = f'+91{t.TPhno}'

    now = datetime.now()
    hour = int(now.strftime("%H"))
    min = int(now.strftime('%M'))

    pwt.sendwhatmsg(s1, f"Hii {t.Tname} You are having new batch No {s}", hour, min + 1)

    return redirect('batchdetails')

@never_cache
def batch_details(request):
    b2=Trainer_Batch_Assign.objects.all()
    return render(request,'admin//BatchDetails.html',{'data3':b2})

@never_cache
def delete_fun(request, x):
    t1 = Trainer_Batch_Assign.objects.get(id=x)
    t1.delete()
    return redirect('batchdetails')

@never_cache
def update_fun(request,id):
    t1 = Trainer_Batch_Assign.objects.get(id=id)
    b1=Trainer_Reg.objects.values()#trainer details
    cc1=Course.objects.values() #course details
    print(t1.Date)
    if request.method == 'POST':
        t1.Tr_name = Trainer_Reg.objects.get(Tname=request.POST['ddlName'])
        t1.BatchNo = request.POST['numBatch']
        t1.Tr_Course = Course.objects.get(course_name=request.POST['ddlcourse'])
        t1.Date = request.POST['datetime']
        t1.save()
        return redirect('batchdetails')
    return render(request,'admin//update.html',{'data':b1,'data2':cc1,'data3':t1})

@never_cache
def logout_fun(request):
    logout(request)
    return redirect('log')

# ----------------------------
# Trainer Functions
# ----------------------------
@never_cache
def trainer_home_fun(request):
    return render(request,'trainer//trainer_home.html')

@never_cache
def trainer_data_fun(request):
    tt1=Trainer_Batch_Assign.objects.filter(Tr_name=request.session['trainer'])
    return render(request,'trainer//trainer_batch_details.html',{'data4':tt1})