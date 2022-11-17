from django.contrib import admin
from django.urls import path


from users import views

# urlpatterns = [
#     # path('admin/', admin.site.urls),  
#     path("", views.UserListView.as_view()),
#     path("<pk>", views.UserDetailView.as_view()),
#     path("create/", views.users_create),
# ]
urlpatterns = [
    path("", views.UserListView.as_view(), name="users-list"),
    path("<pk>", views.UserDetailView.as_view(), name="users-detail"),
    path("create/", views.users_create, name="users-create"),
    path("<pk>", views.UserDetailView.as_view(), name="users-detail"),
    path("<pk>/update/", views.users_update, name="users-update"),
    path("<pk>/delete/", views.users_create, name="users-delete-confirmation"),
]

