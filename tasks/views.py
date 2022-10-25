from django.shortcuts import render, redirect
from tasks.forms import TaskForm, Task
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(False)
            task.owner = request.user
            task.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)


@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "show_task": tasks,
    }
    return render(request, "tasks/list.html", context)
