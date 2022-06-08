from django.urls import path

# from blogging.views import stub_view
# from blogging.views import list_view
# from blogging.views import detail_view
# from . import views
from blogging.views import PostListView, PostDetailView

# app_name = 'blogging'
urlpatterns = [
    path("", PostListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="blog_detail"),
    # path('', list_view, name="blog_index"),
    # path('', stub_view, name="blog_index"),
    # path('posts/<int:post_id>/',detail_view,name="blog_detail"),
]
