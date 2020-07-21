from django.conf.urls import include

from django.urls import path

from .views import (
    PostCreateListView
)

urlpatterns = [
    path("", PostCreateListView.as_view(), name="posts")

]

