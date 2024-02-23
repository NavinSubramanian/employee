from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.contrib import messages

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
        print(checksl)
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
            Employee_detail.objects.create(
                name = namel,
                dob = dobl,
                address = addressl,

                designation = designl,
                empnumber = empidl,
                salary = salaryl,
                experiance = expl,
                department = deptl,

                pastexp = checksl,
                prevjoin = prevj, 
                prevleave = prevl,
            )
        
    messages.success(request,'Added Successfully!')
    return redirect('/view')