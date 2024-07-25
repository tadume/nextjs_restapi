from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import TaskViewSet, PostListView, PostRetrieveView, TaskListView, TaskRetrieveView, CreateUserView

router = routers.DefaultRouter()
router.register("tasks", TaskViewSet, basename="tasks")

urlpatterns = [
    path("list-post/", PostListView.as_view(), name="list_post"),
    path("detail-post/<str:pk>", PostRetrieveView.as_view(), name="detail_post"),
    path("list-task/", TaskListView.as_view(), name="list_task"),
    path("detail-task/<str:pk>", TaskRetrieveView.as_view(), name="detail_task"),
    path("register/", CreateUserView.as_view(), name="register"),
    path("auth/", include('djoser.urls.jwt')),
    path('', include(router.urls)),
]