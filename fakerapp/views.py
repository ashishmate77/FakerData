from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import EmpData
import faker
fake=faker.Faker()

# Create your views here.

def inserting_data(request):
    for i in range(100):
        first_name=fake.first_name()
        last_name=fake.last_name()
        email=fake.email()
        salary=fake.random_element(elements=(15000,20000,30000,40000))
        job=fake.random_element(elements=('HR','MANAGER','SE','PM'))
        location=fake.random_element(elements=('Hyd','Pune','Mumbai'))

        data=EmpData(

            first_name=first_name,
            last_name=last_name,
            email=email,
            salary=salary,
            job=job,
            location=location

        )
        data.save()
    return redirect('/')


def fetching_data(request):
    Emp=EmpData.objects.all()
    return render(request,'emphtml.html',{'Emp':Emp})
