from django.urls import path
from Blog.views import AboutView,PostListView,PostDetailView,CreatePostView,UpdatePostView,DeletePostView,DraftListView,add_comment_to_post,comment_approve,comment_delete,post_publish
urlpatterns=[
    path('',AboutView.as_view(),name="about"),
    path('list/',PostListView.as_view(),name="list"),
    path('detail/<int:pk>/',PostDetailView.as_view(),name="detail"),
    path('create/',CreatePostView.as_view(),name="create_post"),
    path('update/<int:pk>/',UpdatePostView.as_view(),name="update"),
    path('delete/<int:pk>/remove',DeletePostView.as_view(),name="delete"),
    path('draft/',DraftListView.as_view(),name="draft"),
    path('post/<int:pk>/comment',add_comment_to_post,name="comment"),
    path('post/<int:pk>/publish',post_publish,name="publish"),
    path('comment/<int:pk>/delete',comment_delete,name="comment_delete"),
    path('comment/<int:pk>/approve',comment_approve,name="comment_approve"),
]
