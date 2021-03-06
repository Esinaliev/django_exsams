from django.urls import path
from basketapp.views import basket, basket_add, basket_remove, basket_delete

app_name = 'basketapp'

urlpatterns = [
    path('', basket, name='view'),
    path('add/<int:pk>/', basket_add, name='add'),
    path('remove/<int:pk>/', basket_remove, name='remove'),
    path('delete/<int:pk>/', basket_delete, name='delete'),
]
