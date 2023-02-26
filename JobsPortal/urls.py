from django.urls import path

from JobsPortal import views as jobs

urlpatterns = [
    path('login', jobs.login, name="login"),
    path('register', jobs.register, name="register"),
    path('create', jobs.create_jobs, name="create"),
]
