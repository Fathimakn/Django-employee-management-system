
from django.urls import path
from . import views
urlpatterns = [

    path('',views.home,name='home'),
    path('add/',views.add,name='add'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('login/',views.login,name='login' ),
    path('logout/',views.logout,name='logout'),
    path('register/', views.register, name='register'),

]
