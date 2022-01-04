from . import views
from django.urls import path


urlpatterns = [
    path("", views.Homepage.as_view(), name="home"),
    path("dashboard/", views.Dashboard.as_view(), name="dashboard"),
    path("dashboard/create/machine/", views.CreateMachine.as_view(), name="create-machine"),
    path("dashboard/edit/machine/<int:pk>", views.EditMachine.as_view(), name="edit-machine"),
    path("dashboard/delete/machine/<int:pk>", views.delete_machine, name="delete-machine"),
]