from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib import messages
from django.utils.dateparse import parse_date
from datetime import date,datetime

def home(request):
    return render(request, 'forms.html')

def view(request):
    al = Employee_detail.objects.all()
    context = {'emp':al}
    return render(request,'render.html',context)

def check(request):
    if request.method == "POST":
        firstl  = request.POST.get('first')
        lastl  = request.POST.get('last')
        namel = firstl + " " + lastl
        dobl = request.POST.get('date')
        addressl = request.POST.get('address')

        expl = request.POST.get('exp')
        deptl = request.POST.get('dept')
        empidl = request.POST.get('empid')
        designl = request.POST.get('design')
        salaryl = request.POST.get('salary')

        checksl = request.POST.get('checks')
        dob = datetime.strptime(dobl, '%d-%m-%Y')
        current_date = datetime.now()
        age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))

        # Conditions to check

        print(namel," ",dobl," ",addressl," ",expl," ",age," ",deptl," ",salaryl," ",designl," ",empidl)

        if int(expl)<=0:
            messages.success(request,"Experiance cannot be zero-0")
            return redirect('/home')
        if len(salaryl) >= 9:
            messages.success(request,"Salary is too high")
            return redirect('/home')
        if int(age) < 18:
            messages.success(request,"Age is too low")
            return redirect('/home')
        if int(expl) > int(age):
            messages.success(request,"Experiance doesn't match the age")
            return redirect('/home')
        
        print("ok done")

        if(checksl == None):
            Employee_detail.objects.create(
                name = namel,
                dob = dobl,
                address = addressl,

                designation = designl,
                empnumber = empidl,
                salary = salaryl,
                experiance = expl,
                department = deptl,

                pastexp = False,
                prevjoin = '-', 
                prevleave = '-',
            )
        else:
            prevl = request.POST.get('date3')
            prevj = request.POST.get('date2')

            prevl1 = datetime.strptime(prevl, '%d-%m-%Y')
            prevj1 = datetime.strptime(prevj, '%d-%m-%Y')

            asjdn = int(prevj1.year) >= int(prevl1.year)
            print(asjdn)
            if (asjdn):
                print("OK")
                messages.success(request,"Previous Experiance is wrong")
                return redirect('/home')
            else:
                Employee_detail.objects.create(
                    name = namel,
                    dob = dobl,
                    address = addressl,
                    designation = designl,
                    empnumber = empidl,
                    salary = salaryl,
                    experiance = expl,
                    department = deptl,
                    pastexp = True,
                    prevjoin = prevj, 
                    prevleave = prevl,
                )
        
    messages.success(request,'Added Successfully!')
    return redirect('/view')