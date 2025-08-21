from django.shortcuts import render
from django.http import HttpResponse
from .models import Person,Role,Department
from datetime import datetime
from django.db.models import Q

# Create your views here.

def myname(request):
    return HttpResponse("my name is harthik :) ")

def home(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Person.objects.all()
    return render(request,'all_emp.html',{'emps': emps})


# def add_emp(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         dept = request.POST['dept']
#         bonus = int(request.POST['bonus'])
#         salary = int(request.POST['salary'])
#         role = request.POST['role']
#         phone = int (request.POST['phone'])
#         new_emp = Person(first_name = first_name,last_name = last_name, dept_id = dept, bonus = bonus, salary = salary, role_id = role,phone = phone, hire_date = datetime.now())
#         new_emp.save()
#         return HttpResponse('employee added sucessfully :) ')
#     elif request.method == 'GET':
#         return render(request,'add_emp.html')
#     else:
#         HttpResponse("an exception occured error ")

def add_emp(request):
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            dept = request.POST['dept']
            role = request.POST['role']
            salary = int(request.POST['salary'])
            bonus = int(request.POST['bonus'])
            phone = int(request.POST['phone'])

            # Create and save new employee
            new_emp = Person(
                first_name=first_name,
                last_name=last_name,
                dept_id=dept,        # ✅ ForeignKey by ID
                role_id=role,        # ✅ ForeignKey by ID
                salary=salary,
                bonus=bonus,
                phone=phone,
                hire_date=datetime.now()
            )
            new_emp.save()
            return HttpResponse('Employee added successfully 😊')

        except Exception as e:
            return HttpResponse(f"An error occurred: {str(e)}")

    elif request.method == 'GET':
        # Pass departments and roles to the form
        departments = Department.objects.all()
        roles = Role.objects.all()
        return render(request, 'add_emp.html', {
            'departments': departments,
            'roles': roles
        })

    else:
        return HttpResponse("Invalid request method ❌")



def remove_emp(request,emp_id = 0):
    if emp_id:
        try:
            id_that_removed = Person.objects.get(id = emp_id)
            id_that_removed.delete()
            return HttpResponse("employee removed sucessfully ")
        except:
            return HttpResponse("please enter valid id ")



    emps = Person.objects.all()

    return render(request,'remove_emp.html',{'emps':emps})

def filter_emp(request):
    if request.method == 'POST':
            name = request.POST['name']
            dept = request.POST['dept']
            role = request.POST['role']

            emps = Person.objects.all()

            if name:
                    emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))

            if dept:
                    emps = emps.filter(dept_id=dept)

            if role:
                    emps = emps.filter(role_id=role)

            return render(request, 'all_emp.html', {'emps':emps})

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')