"""ntuhcorelab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from .views import PersonUpdate, PIUpdate, StaffUpdate, CardUpdate, PersonDelete, PICreate, StaffCreate, CardCreate, PersonCreate
from . import views

app_name = 'database'
urlpatterns = [
    # HOME
    path('', views.home, name='home'),

    # SEARCH
    path('search', views.search, name='search'),

    # BROWSE
    path('browse', views.browse, name='browse'),
    path('browse/pi', views.browse_PI, name='browse_PI'),
    path('browse/staff', views.browse_staff, name='browse_staff'),
    path('browse/card', views.browse_card, name='browse_card'),

    # DETAIL
    path('detail/<str:uid>/', views.detail, name='people_detail'),

    # CREATE
    # path('create',views.create_person, name='create_person'),
    path('create', PersonCreate.as_view(), name='create_person'),
    path('create_pi', PICreate.as_view(), name='create_pi'),
    path('create_staff', StaffCreate.as_view(), name='create_staff'),
    path('create_card', CardCreate.as_view(), name='create_card'),
    path('create/success', views.success, name='success'),

    # UPDATE
    # path('update/<str:uid>/',PersonUpdate.as_view(), name='update_person'),
    path('update/<str:uid>/', views.PersonUpdate, name='update_person'),
    path('update_pi/<str:uid>/', views.PIUpdate, name='update_pi'),
    path('update_staff/<str:uid>/', views.StaffUpdate, name='update_staff'),
    path('update_card/<str:uid>/', views.CardUpdate, name='update_card'),

    # DELETE
    path('delete/<str:uid>/', PersonDelete.as_view(), name='delete_person'),

    #DOWNLOAD
    path('download/', views.backupall, name='backupall'),

    #LOG
    path('log', views.log, name="log"),
]
