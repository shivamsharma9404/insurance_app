from django.contrib import admin
from django.urls import path
from .views import createInsurance,InsuranceDetail,InsuranceList
from rest_framework_swagger.views import get_swagger_view
from django.conf.urls import url
from rest_framework import routers
from django.http import HttpResponseRedirect

schema_view = get_swagger_view(title='API name')
'''
router = routers.DefaultRouter()
router.register(r'Insurances',createInsurance.)
'''



urlpatterns = [

    url(r'^docs/$', schema_view, name="schema_view"), #swagger -- rest api
    path('postinsurance/', createInsurance.as_view()),
    path('getinsu/', InsuranceList.as_view()),
    path('getinsu/<int:pk>',InsuranceDetail.as_view())

   ]



#pip install django-rest-swagger