from django.shortcuts import render
from django.template import RequestContext
from .models import *
# Create your views here.


def home(request):
    return render(request, 'index.html')


def teacher(request):
    dic = {'name': request.session['teacher'],
           'code': request.session['code'], 'total': request.session['total']}
    dic['student'] = Student.objects.filter(teacher=request.session['teacher'])
    return render(request, 'admin.html', dic)


def login(request):
    if request.method == "POST":
        name = request.POST['name']
        password = request.POST['password']
        if Staff.objects.filter(name=name).exists():
            temp = Staff.objects.get(name=name)
            if temp.password == password:
                request.session['teacher'] = temp.name
                request.session['code'] = temp.code
                request.session['total'] = temp.noofstudent
                dic = {'name': request.session['teacher'],
                       'code': request.session['code'], 'total': request.session['total']}
                dic['student'] = Student.objects.filter(teacher=temp.name)
                return render(request, 'admin.html', dic)
            else:
                return render(request, 'login.html', {'err': 'Password mismatch'})
        else:
            return render(request, 'login.html', {'err': 'Teacher does not exist'})
    else:
        return render(request, 'login.html')


def student(request):
    if request.method == "POST":
        rollno = request.POST['rollno']
        code = request.POST['Ecode']
        if Student.objects.filter(rollno=rollno).exists():
            request.session['student'] = rollno
            request.session['scode'] = code
            return render(request, 'index.html')
        else:
            return render(request, 'studentLogin.html', {'err': 'Student does not exist'})
    else:
        return render(request, 'studentLogin.html')


def enroll(request):
    tot = Staff.objects.get(
        name=request.session['teacher']).noofstudent
    if request.method == "POST":
        rollno = request.POST['rollno']
        code = request.session['code']
        subject = request.POST['course']
        name = request.POST['name']
        if Student.objects.filter(rollno=rollno, code=code).exists():
            return render(request, 'enrollStudent.html', {'err': 'Student does not exist', 'total': tot})
        else:
            Student.objects.create(rollno=rollno, code=code, name=name,
                                   teacher=request.session['teacher'], mark=0, subject=subject)
            tot += 1
            request.session['total'] += 1
            Staff.objects.filter(name=request.session['teacher']).update(
                noofstudent=tot)
            return render(request, 'enrollStudent.html', {'success': "Student enrolled successful", 'total': tot})
    else:
        return render(request, 'enrollStudent.html', {'total': tot})


def result(request):
    data = Student.objects.filter(teacher=request.session['teacher'])
    return render(request, 'result.html', {'data': data})


def mark(request, i):
    Student.objects.filter(rollno=request.session['student']).update(
        mark=i)
    return render(request, 'studentLogin.html')
