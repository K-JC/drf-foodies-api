from django.urls import path
from like_comments import views

urlpatterns = [
    path('like_comments', views.LikeComment.as_views()),
    path('like_comments/<int:pk>/', views.LikeCommentDetail.as_views()),

]
