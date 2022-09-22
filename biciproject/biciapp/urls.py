from django.urls import path
from . import views

urlpatterns = [
    path('add', views.newCustomer, name='newCustomer'),
    path('get', views.getCustomers, name='getCustomers'),
    path('getOneCustomer/<int:id>', views.getOneCustomer, name='getOneCustomer'),
    path('updateCustomer/<int:id>', views.updateCustomer, name='updateCustomer'),
    path('deleteCustomer/<int:id>', views.deleteCustomer, name='deleteCustomer'),
    path('addBike', views.newBike, name='addBike'),
    path('getAllBikes', views.getAllBikes, name='getAllBikes'),
    path('getOneBike/<int:id>', views.getOneBike, name='getOneBike'),
    path('updateBike/<int:id>', views.updateBike, name='updateBike'),
    path('deleteBike/<int:id>', views.deleteBike, name='deleteBike'),
]