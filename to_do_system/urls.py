from django.urls import path

from to_do_system.views import (TaskListView,
                                TagListView,
                                TaskCreateView,
                                TaskUpdateView,
                                TaskDeleteView,
                                TagCreateView,
                                TagUpdateView,
                                TagDeleteView,
                                TaskCompleteToggleView)

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("add_task/", TaskCreateView.as_view(), name="add-task"),
    path("update_task/<int:pk>/", TaskUpdateView.as_view(), name="update-task"),
    path("delete_task/<int:pk>/", TaskDeleteView.as_view(), name="delete-task"),
    path("add_tag/", TagCreateView.as_view(), name="add-tag"),
    path("update_tag/<int:pk>/", TagUpdateView.as_view(), name="update-tag"),
    path("delete_tag/<int:pk>/", TagDeleteView.as_view(), name="delete-tag"),
    path("complete_toggle/<int:pk>/", TaskCompleteToggleView.as_view(), name="complete-toggle"),

]

app_name = "to_do_system"
