from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.all_finches, name='finches'),
    path('finches/<int:finch_id>/', views.single_finch, name="single_finch"),
    path('finches/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name='finch_update'),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name='finch_delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('finches/<int:finch_id>/connect_snack/<int:snack_id>', views.connect_snack, name='connect_snack'),
    path('finches/<int:finch_id>/remove_snack/<int:snack_id>', views.remove_snack, name='remove_snack'),
    path('snacks/', views.SnackList.as_view(), name='snacks_list'),
    path('snacks/<int:pk>', views.SnackDetail.as_view(), name='snack_details'),
    path('snacks/create', views.SnackCreate.as_view(), name='snack_create'),
    path('snacks/<int:pk>/delete', views.SnackDelete.as_view(), name='snack_delete')
]
