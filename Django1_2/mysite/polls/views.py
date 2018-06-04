from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EmployeeForm
from .models import Question
from .models import Employee
from django.views import View
from django.http import JsonResponse
import json
from django.views.generic.edit import CreateView

# Create your views here.

class ListView(View):
    def get(self, request):
        latest_employee_list = Employee.objects.all()
        template = loader.get_template('polls/poll-list.html')
        context = {
            'latest_employee_list': latest_employee_list,
        }
        print (latest_employee_list)
        return HttpResponse(template.render(context, request))


class ListViewAjax(View):
    def get(self, request):
        latest_employee_list = Employee.objects.all()
        template = loader.get_template('polls/employee-list-ajax.html')
        context = {
            'latest_employee_list': latest_employee_list,
        }
        print (latest_employee_list)
        return HttpResponse(template.render(context, request))

def list(request):
    #latest_employee_list = Employee.objects.order_by('-hire_date')[:5]
    latest_employee_list = Employee.objects.all()
    template = loader.get_template('polls/poll-list.html')
    context = {
        'latest_employee_list': latest_employee_list,
    }
    print (latest_employee_list)
    return HttpResponse(template.render(context, request))


def deleteEmpAjax(request):
    employeeId = request.GET.get('employee_id')
    print ("Ajax Delete Request -- EmployeeID " + employeeId)
    e = Employee.objects.get(id=employeeId)
    e.delete()
    data = {"successCode": 1337}
    return JsonResponse(data)

def createEmpAjax(request):
    employeeName = request.GET.get('employee_name')
    jobTitle= request.GET.get('job_title')
    hireDate = request.GET.get('hire_date')
    print ("Ajax create Request -- EmployeeName " + employeeName)
    e = Employee(employee_name= employeeName, job_title=jobTitle , hire_date=hireDate)
    e.save()
    empId = e.pk
    e2 = Employee.objects.get(id=empId)
    hireDate = e2.hire_date

    data = {"successCode": 1337,
            "empName": employeeName,
            "jobTitle": jobTitle,
            "hireDate": hireDate,
            "empId": empId
    }
    return JsonResponse(data)


def editEmpAjax(request):
    employeeId = request.GET.get('employee_id')
    employeeName = request.GET.get('employee_name')
    jobTitle= request.GET.get('job_title')
    hireDate = request.GET.get('hire_date')
    print ("Ajax create Request -- EmployeeId " + employeeId + " Name: " + employeeName + " Job title: " + jobTitle )
    e = Employee.objects.get(id=employeeId)
    e.employee_name = employeeName
    e.job_title = jobTitle
    e.hire_date = hireDate
    e.save()
    data = {
        "successCode": 1337,
        "empId": employeeId,
        "empName":employeeName,
        "jobTitle":jobTitle,
        "hireDate":hireDate
    }
    return JsonResponse(data)


def detail(request, employee_id):
    e = Employee.objects.get(id=employee_id)
    return render(request, 'polls/poll-detail.html',{'employee_id':employee_id, 'employee_name': e.employee_name, 'job_title':e.job_title, 'hire_date':e.hire_date})


def delete(request, employee_id):
    print ("delete called")
    q = Employee.objects.get(id=employee_id)
    q.delete()
    # if request is not post, initialize an empty form
    if request.method == 'POST':
        return HttpResponseRedirect('/polls/list')
    
    #return render(request, 'polls/create-poll.html', {'form': form})
    return  HttpResponseRedirect('/polls/list')

def polls(request):
    return render(request, 'polls/home.html')


def update(request, employee_id):
    print ("Employee ID " + employee_id)
    e = Employee.objects.get(id=employee_id)
    data = {'employee_name': e.employee_name,'job_title':e.job_title , 'hire_date': e.hire_date}
    form = EmployeeForm(initial=data)
    
    if request.method == 'POST':
        form = EmployeeForm(request.POST)

        print ("post req")
        if form.is_valid():
            employee_name_ = request.POST.get('employee_name')
            job_title_ = request.POST.get('job_title')
            hire_date_ = request.POST.get('hire_date')
            
            print ("Date Retrieval: " + employee_name_ + " and " + hire_date_)
            e.employee_name=employee_name_
            e.job_title=job_title_
            e.hire_date=hire_date_           
            e.save()
            return HttpResponseRedirect('/polls/list')

    return render(request, 'polls/update-poll.html', {'form': form,'employee_id':employee_id})


def create(request):
    form_class = EmployeeForm
    # if request is not post, initialize an empty form
    form = form_class(request.POST or None)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        print ("post req")
        if form.is_valid():
            employee_name_ = request.POST.get('employee_name')
            job_title_ = request.POST.get('job_title')
            hire_date_ = request.POST.get('hire_date')

            print ("Date Retrieval: " +employee_name_+ " and " + hire_date_)
            e = Employee(employee_name=employee_name_, job_title=job_title_ , hire_date=hire_date_)
            e.save()
            return HttpResponseRedirect('/polls/list')

    return render(request, 'polls/create-poll.html', {'form': form})


def vote(request, employee_id): 
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': 'data',
    }
    return HttpResponse(template.render(context, request))