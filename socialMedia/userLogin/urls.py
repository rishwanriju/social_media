from django.urls import path
from . import views



urlpatterns = [
    path('',views.login_page.as_view(),name='login'),
    path('register/',views.Register.as_view(),name='register'),
    # path('posts/',views.PostList.as_view(),name='Posts'),
    path('postdetails/',views.PostDetail.as_view(),name='PostDetail'),
    path('edit/<int:pk>/',views.PostUpdate.as_view(),name='Edit'),
    path('delete/<int:pk>/',views.PostDelete.as_view(),name='Delete'),
    path('posts/',views.PostCreate.as_view(),name='Posts'),
    path('likes/<int:id>/',views.P_likes.as_view()),
    path('comments/<int:id>/',views.p_comment.as_view())

]