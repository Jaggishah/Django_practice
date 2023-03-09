from django.urls import path

from . import views

urlpatterns =[
    # path("<int:id>",views.index,name="index"),
    path("<int:id>",views.home,name="home"),
    path('create/',views.create,name="create"),
]