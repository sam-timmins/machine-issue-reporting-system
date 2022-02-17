from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("issue.urls"), name="issue_urls"),
    path("", include("accounts.urls"), name="accounts_urls"),
    path("", include("home.urls"), name="home_urls"),
    path('account/', include('allauth.urls')),
]
