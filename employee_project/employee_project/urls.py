"""
URL configuration for employee_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from employee_register.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("list/", employee_list, name="employee_list"),
    path("delete/<int:id>/", employee_delete, name="employee_delete"),
    path("", loginPage, name="login_page"),
    path("registerPage/", registerPage, name="register_page"),
    path("<int:id>/", employee_form, name="employee_update"),
    path("employeeForm/", employee_form, name="employee_insert"),
    path("logout/", logout_page, name="logout_page")
]