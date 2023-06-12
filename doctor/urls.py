from django.urls import path
from .views import HomeTemplateView, AppointmentTemplateView, ManageAppointmentTemplateView, home
from .import views


urlpatterns = [
    path("appointment/", AppointmentTemplateView.as_view(), name="appointment"),
    path("manage/", ManageAppointmentTemplateView.as_view(), name="manage"),
    path("blog/", views.blog, name="blog"),
    path("", views.home, name="home"),
]

