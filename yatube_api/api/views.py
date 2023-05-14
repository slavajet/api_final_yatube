from django.shortcuts import get_object_or_404
from posts.models import Follow, Group, Post, User
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .permissions import OwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer, UserSerializer)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление API для просмотра групп."""
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    """Представление API для постов."""
    pagination_class = LimitOffsetPagination
    permission_classes = (OwnerOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Создание нового поста и указание автора поста."""
        serializer.save(author=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """Представление API для пользователей."""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """Представление API для комментариев к постам."""
    permission_classes = (OwnerOrReadOnly,)
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        """Создание нового комментария, указание автора комментария и поста."""
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        """Возвращает только комментарии к определенному посту."""
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return post.comments.all()


class FollowViewSet(CreateModelMixin, ListModelMixin, viewsets.GenericViewSet):
    """
    Представление API для подписок.
    - CreateModelMixin предоставляет функциональность создания новой подписки.
    - ListModelMixin предоставляет функциональность получения списка подписок.
    - GenericViewSet предоставляет предопределенные действия CRUD для моделей.
    """
    filter_backends = (SearchFilter,)
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)
    queryset = Follow.objects.all()
    search_fields = ('following__username', 'user__username',)
    serializer_class = FollowSerializer

    def get_queryset(self):
        """Возвращает все подписки пользователя, сделавшего запрос."""
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Создание новой подписки и указание пользователя."""
        serializer.save(user=self.request.user)
