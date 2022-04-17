from django.urls import path
from . import views

app_name = "post"

urlpatterns = [
    path("", views.index, name="hello"),
    path("topic_list/", views.topic_list_view, name="topic_list"),
    path("topic/<int:topic_id>/", views.topic_detail_view, name="topic_detail"),
    path("topic_comment/", views.add_comment_to_topic_view, name="add_comment_to_topic")
]
