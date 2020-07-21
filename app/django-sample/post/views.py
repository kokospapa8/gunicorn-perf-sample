# -*- coding: utf-8 -*-
from rest_framework import generics, permissions
from .serializers import PostSerializer
from .models import Post


class PostCreateListView(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_show=True)

