from django.urls import path
from .views import post_create_form_view, post_delete_view, post_detail_view, post_list_view, post_update_view

app_name = 'posts'

urlpatterns = [
    path('', post_list_view, name="post-list"),
    path('create/', post_create_form_view, name='post-create'),
    path('<int:id>/', post_detail_view, name='post-detail'),
    path('edit/<int:id>/', post_update_view, name='post-update'),
    path('delete/<int:id>/', post_delete_view, name="post-delete"),
]