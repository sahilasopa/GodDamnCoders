from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from JobsPortal.models import BaseUser


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login_page.html', {'error': 'Invalid Credentials'})
    return render(request, "login_page.html")


def register(request):
    first_name = request.POST.get("first_name")
    last_name = request.POST.get("last_name")
    username = request.POST.get("username")
    email = request.POST.get("email")
    password = request.POST.get("password")
    password_confirm = request.POST.get("confirm_password")
    company_name = request.POST.get("company_name")
    company_description = request.POST.get("company_description")
    country = request.POST.get("country")
    if request.method == 'POST':
        if password == password_confirm:
            try:
                BaseUser.objects.get(username=username)
                return render(request, 'registeration_page.html', {'error': 'Username Taken'})

            except BaseUser.DoesNotExist:
                try:
                    User.objects.get(email=email)
                    return render(request, 'registeration_page.html', {'error': 'Email Already Taken'})

                except User.DoesNotExist:
                    user = User.objects.create_user(username=username,
                                                    password=password,
                                                    email=email)
                users = BaseUser(user=user, first_name=first_name, last_name=last_name, email=email, username=username,
                                 company_name=company_name, country=country, description=company_description)
                users.save()
                auth.login(request, user)
                return redirect('/')
        else:
            return render(request, 'registeration_page.html', {"error": "Password doesn't match"})
    else:
        return render(request, 'registeration_page.html')


def create_jobs(request):
    if request.method == "POST":
        title = request.POST.get("job-title")
        job_type = request.POST.get("job-type")
        skills = request.POST.getlist("skills")
        location = request.POST.get("location")
        is_remote = request.POST.get("remote")
        description = request.POST.get("description")
        website = request.POST.get("website")
        print(title)
        print(job_type)
        print(skills)
        print(location)
        print(is_remote)
        print(description)
        print(website)
    return render(request, "Create_Job_File.html")
