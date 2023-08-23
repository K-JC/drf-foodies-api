from django.urls import path
from like_comments import views

urlpatterns = [
    path('like_comments', views.LikeComment.as_views()),
  

]
