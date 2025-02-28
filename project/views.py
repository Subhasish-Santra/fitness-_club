from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from project.models import Registration
from django.contrib import messages
from .models import Registration
import sqlite3
import json
from django.views.decorators.csrf import csrf_exempt

def test(request):
    return HttpResponse("Hello World!")

def index(request):
    return render(request, 'index.html')

def Contact(request):
    return render(request, 'contact.html')


def logdata(request):
    request.method = 'POST'
    u=logdata()
    u.name= request.POST.get['name']
    u.age= request.POST.get['age']
    u.gender= request.POST.get['gender']
    u.email= request.POST.get['email']
    u.password= request.POST.get['password']
    u.save()
    return render(request, 'registration.html')

def signin(request):
    return render(request, 'signin.html')

def sign(request):
    e=request.GET['A1']
    p=request.GET['A2']
    if logdata.objects.filter(email=e,password=p):
        return render(request, 'registration.html')
    else:
        return render(request, 'signin.html')
def display(request):
    data=logdata.objects.all()
    return render(request, 'display.html',{'data':data})
def delete(request,id):
    u= logdata.objects.get(id=id)
    u.delete()
    return redirect('/display')
def editdata(request,id):
    d=logdata.objects.get(id=id)
    return render(request,'editdata.html',{'x':d})
def edit(request,id):
    d=logdata.objects.POST(id=id)
    d.name=request.POST['a1']
    d.DOB=request.POST['a2']
    d.email=request.POST['a3']
    d.contact=request.POST['a4']
    d.gender=request.POST['gender']
    d.country=request.POST['country']
    d.password=request.POST['a5']
    d.save()
    return redirect('../display')
def logout(request):
    return render(request, 'logout.html')
def index(request):
    return render(request, 'index.html')

def index_2(request):
    return render(request, 'index_2.html')

def success(request):
    return render(request, 'success.html')
from django.http import HttpResponseBadRequest

def reg(request):
    contact = request.GET.get('a4')
    if not contact or not contact.isdigit():
        return HttpResponseBadRequest("Invalid contact number")
    
    # Your existing logic here
    
    return render(request, 'success.html')

def subscription(request):
    return render(request, 'subscription.html')

def explore(request):
    return render(request, 'explore.html')
def payment(request):
    return render(request, 'payment.html')

def register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            # Hash the password using Django's built-in method (this is handled automatically in the form, so no need to do it manually here)
            form.save()

            # Success message
            messages.success(request, 'Registration Successful! Welcome to our Fitness Program.')

            return redirect('index_2')  # Redirect to the desired page after successful registration
        else:
            # If the form is not valid, render the form with errors
            return render(request, 'registration.html', {'form': form})

    else:
        form = Registration()

    return render(request, 'registration.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')

def success_view(request):
    return redirect('index_2')

def save_registration(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        age = data.get('age')
        email = data.get('email')
        gender = data.get('gender')
        address = data.get('address')

        # Save data to database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO registrations (name, age, email, gender, address)
            VALUES (?, ?, ?, ?, ?)
        ''', (name, age, email, gender, address))
        conn.commit()
        conn.close()

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

def registration(request):
    return render(request, 'registration.html')

@csrf_exempt
def save_registration(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        age = data.get('age')
        email = data.get('email')
        gender = data.get('gender')
        address = data.get('address')
        password = data.get('password')

        if name and age and email and gender and address and password:
            Registration.objects.create(
                name=name,
                age=age,
                email=email,
                gender=gender,
                address=address,
                password=password
            )
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Missing fields'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})