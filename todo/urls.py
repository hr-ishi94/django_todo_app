from django.urls import path
from . import views



urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/',views.login_page, name='login_page'),
    path('todo/',views.todo, name='todo'),
    path('edit_todo/<int:pk>/',views.edit_todo, name ='edit_todo'),
    path('delete_todo/<int:pk>/',views.delete_todo, name ='delete_todo'),
    path('signout/',views.signout, name ='signout'),
]
