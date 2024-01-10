from django.urls import path
from .views import signup,signin, dashboard,index

urlpatterns = [
    path('',index,name = 'base'),
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('signin/', signin, name='signin'),
]