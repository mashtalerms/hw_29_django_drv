from django.urls import path
from users.views import UserListView, UserRetrieveView, UserUpdateView, UserDestroyView, UserCreateView

urlpatterns = [
    path('user/', UserListView.as_view()),
    path('user/create/', UserCreateView.as_view()),
    path('user/<int:pk>/', UserRetrieveView.as_view()),
    path('user/<int:pk>/update/', UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', UserDestroyView.as_view()),
]
