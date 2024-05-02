from django.urls import path # type: ignore

from demo import views

urlpatterns = [
    path('index/', views.helloword) 
    #Not views.helloword() because, Django 
    #just want the reference of the function to call not the call. With brackets
    #it seems like we are the one who call the function and it is not the case.
]
