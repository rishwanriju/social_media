from django.urls import path
from . import views




urlpatterns = [
    path('',views.login_page.as_view(),name='login'),
    path('register/',views.Register.as_view(),name='register'),
    path('posts/',views.PostList.as_view(),name='Posts'),
    path('postdetails/',views.PostDetail.as_view(),name='PostDetail'),
    path('edit/<int:pk>/',views.PostUpdate.as_view(),name='Edit')
]