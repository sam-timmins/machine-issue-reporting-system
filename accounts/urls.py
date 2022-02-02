from . import views
from django.urls import path


urlpatterns = [
    path('login/', views.LoginViewCustom.as_view(), name='login'),
    path('signup/', views.SignUpViewCustom.as_view(), name='signup'),
    path("user/profile/all-users/", views.ViewAllUsers.as_view(), name="all-users"),
    path("user/profile/edit/staff/status/<int:pk>", views.EditStaffStatus.as_view(), name="edit-staff-status"),
    path("user/edit/profile/", views.UserEditProfile.as_view(), name="edit-profile"),
    path("user/profile/delete/<int:pk>", views.delete_user_profile, name="delete_user_profile"),
    path("user/profile/search", views.SearchUsers.as_view(), name="search-users"),
]