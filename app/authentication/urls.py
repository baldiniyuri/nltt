from django.urls import path
from .views import UsersRegisterView, UserAuthenticatedView, LoginView, LogoutView

urlpatterns = [
    path('register/', UsersRegisterView.as_view()),
    path('delete-account/<int:user_id>/', UserAuthenticatedView.as_view()),
    path('get-user-data/<int:user_id>/', UserAuthenticatedView.as_view()),
    path('profile/<int:user_id>/', UserAuthenticatedView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/<int:user_id>/', LogoutView.as_view()),

]
