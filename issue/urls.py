from . import views
from django.urls import path


urlpatterns = [
    path("", views.Homepage.as_view(), name="home"),
    path("dashboard/", views.Dashboard.as_view(), name="dashboard"),
    path("search-machines/", views.SearchMachines.as_view(), name="search-machines"),
    path("dashboard/create/machine/", views.CreateMachine.as_view(), name="create-machine"),
    path("dashboard/edit/machine/<int:pk>", views.EditMachine.as_view(), name="edit-machine"),
    path("dashboard/delete/machine/<int:pk>", views.delete_machine, name="delete-machine"),
    path("dashboard/machine/details/<slug:slug>/", views.MachineDetail.as_view(), name="machine-details"),
    path("open/issues/", views.IssueList.as_view(), name="open-issues"),
    path("dashboard/delete/issue/<int:pk>", views.delete_issue, name="delete-issue"),
    path("search-issues/", views.SearchIssues.as_view(), name="search-issues"),
    path("user/profile/all-users/", views.ViewAllUsers.as_view(), name="all-users"),
    path("user/profile/edit/staff/status/<int:pk>", views.EditStaffStatus.as_view(), name="edit-staff-status"),
    path("user/edit/profile/", views.UserEditProfile.as_view(), name="edit-profile"),
    path("user/profile/delete/<int:pk>", views.delete_user_profile, name="delete_user_profile"),
]
