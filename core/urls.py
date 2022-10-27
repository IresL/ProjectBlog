from django.urls import path
from core.views import PostEditView, home_view, post_detail_view, post_delete_view, post_create_view, PostCreateView,post_edit_view

app_name = 'core'

urlpatterns = [
    path('',home_view, name = 'home'),
    path('post/<int:pk>/', post_detail_view, name = 'post-detail'),
    path('post/delete/', post_delete_view, name = 'post-delete'),
    # path('post/create/', post_create_view, name = 'post-create'),
    path('post/create/', PostCreateView.as_view(), name = 'post-create'),
    #path('post/<int:pk>/edit/', post_edit_view, name = 'create-edit'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name = 'post_edit'),
    ]