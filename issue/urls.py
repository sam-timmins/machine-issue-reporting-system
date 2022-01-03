from . import views
from django.urls import path


urlpatterns = [
    path("", views.Homepage.as_view(), name="home"),
    path("dashboard/", views.Dashboard.as_view(), name="dashboard"),
]