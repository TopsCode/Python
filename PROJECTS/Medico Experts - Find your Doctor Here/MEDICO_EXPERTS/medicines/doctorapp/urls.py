"""medicines URL Configuration

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
from django.urls import path,include
from doctorapp import views

urlpatterns = [
   path('', views.index1, name='index1'),
   #path('login/', views.login, name='login'),
   path('view-patients', views.view_patients, name='view-patients'),
   path('doctor_profile', views.doctor_profile, name='doctor_profile'),
   path('patient_profile', views.patient_profile, name='patient_profile'),
   path('update_profile', views.update_profile, name='update_profile'), 
   path('logout', views.logout, name='logout'), 
   path('all_doc', views.all_doc, name='all_doc'),
   path('appointment', views.appointment, name='appointment'), 
   path('appo_data', views.appo_data, name='appo_data'), 
   path('pprofile', views.pprofile, name='pprofile'), 
   path('mark_availability',views.mark_availability,name="mark_availability"),
   path('store-all-availabilities',views.store_all_availabilities,name="store-all-availabilities"),
   #path('viewavalability',views.viewavalability,name="viewavalability"),
   path(r'^viewavalability/(?P<pk>\d+)/$', views.viewavalability, name='viewavalability'),
   path('Book_appo', views.Book_appo, name='Book_appo'), 
   path('all_appo', views.all_appo, name='all_appo'), 
   path('send_mail2', views.send_mail2, name='send_mail2'), 
   path('chatvalue', views.chatvalue, name='chatvalue'), 
   path(r'^chatbot/(?P<pk>\d+)/$',views.chatbot,name="chatbot"),
   path('sendmessage',views.sendmessage,name="sendmessage"),
   path('dchat', views.dchat, name='dchat'), 
   path('pupdate_profile',views.pupdate_profile, name='pupdate_profile'), 
   path('dsendmessage',views.dsendmessage, name='dsendmessage'), 
   path(r'^dchatbot/(?P<pk>\d+)/$',views.dchatbot, name='dchatbot'), 
   
   
]

