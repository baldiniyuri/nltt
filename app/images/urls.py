from django.urls import path
from images.views import ImagesView


urlpatterns = [
    path('images/', ImagesView.as_view()),
    path('images/<int:user_id>/', ImagesView.as_view()),
]