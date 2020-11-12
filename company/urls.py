from django.urls import path

from company.views import List, Details, Delete

app_name = 'company'

urlpatterns = [
    path('', List.as_view(), name='list'),
    path('details/<int:pk>', Details.as_view(), name='details'),
    path('delete/<int:pk>', Delete.as_view(), name='delete'),
]
