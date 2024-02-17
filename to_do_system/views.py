from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from to_do_system.forms import TagForm, TaskForm
from to_do_system.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "to_do_system/tags_list.html"
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "to_do_system/tag_form.html"
    form_class = TagForm
    success_url = reverse_lazy("to_do:home")


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "to_do_system/tag_form.html"
    form_class = TagForm
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
    form_class = TaskForm
    success_url = reverse_lazy("to_do:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "to_do_system/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("to_do:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "to_do_system/task_confirm_delete.html"
    success_url = reverse_lazy("to_do:home")


class TaskCompleteToggleView(generic.UpdateView):
    model = Task
    fields = ["is_done"]
    success_url = reverse_lazy("to_do_system:home")

    def form_valid(self, form):
        task = get_object_or_404(Task, pk=self.kwargs["pk"])
        task.is_done = not task.is_done
        return super().form_valid(form)
