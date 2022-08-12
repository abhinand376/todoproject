
from django.urls import path
from . import views


# app_name='todoapp'

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.tlistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.tdetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.tupdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.tdeleteview.as_view(), name='cbvdelete'),
]
