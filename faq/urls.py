from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('faqs1/',views.faqs,name="faqs1"),
    path('faqs2/',views.faqs,name="faqs2"),
    path('faqs/',views.faqs,name="faqs"),
]
