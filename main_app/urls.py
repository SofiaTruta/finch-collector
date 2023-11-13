from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.all_finches, name='finches'),
    path('finches/<int:finch_id>/', views.single_finch, name="single_finch")
]
