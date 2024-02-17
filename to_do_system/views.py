from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from to_do_system.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "to_do_system/tags_list.html"
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "to_do_system/tag_form.html"
    fields = ["name"]
    success_url = reverse_lazy("to_do:home")


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "to_do_system/tag_form.html"
    fields = ["name"]
    success_url = reverse_lazy("to_do:home")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "to_do_system/tag_confirm_delete.html"
    success_url = reverse_lazy("to_do:home")


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "to_do_system/tasks_list.html"
    paginate_by = 10


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "to_do_system/task_form.html"
    fields = ["content", "created_datetime",
              "deadline_datetime", "is_done",
              "tags"]
    success_url = reverse_lazy("to_do:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "to_do_system/task_form.html"
    fields = ["content", "created_datetime",
              "deadline_datetime", "is_done",
              "tags"]
    success_url = reverse_lazy("to_do:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "to_do_system/task_confirm_delete.html"
    success_url = reverse_lazy("to_do:home")


class TaskCompleteToggleView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs["pk"])
        task.is_done = not task.is_done
        task.save()
        return redirect("to_do:home")
