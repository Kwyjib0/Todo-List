from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy # redirects user to certain part of application (similar to reverse)
from .models import Task
from .forms import TodoForm
from django.http import HttpResponseRedirect
from django.urls import reverse


# list view is a template for displaying a list of object, often a queryset
# will find proper template w/ model name prefix and _list.html 'task_list.html' by default
class TaskList(ListView):
    # requires a model or a queryset
    model = Task
    # change queryset name from default of 'object_list'
    context_object_name = 'tasks'

# detail view returns info about a specific item / object instance
# will find proper template w/ model name prefix and _detail.html 'task_detail.html' by default
class TaskDetail(DetailView):
    # requires a model or a queryset
    model = Task
    # change object name from default of 'object'
    context_object_name = 'task'
    # will look for task_detail.html by default unless change template name here
    template_name = 'todo/task.html'

# create view looks for template w/ model name prefix and _form.html 'task_form.html' by default
# gives a model form to work with, takes models & creates all fields by default
class TaskCreate(CreateView):
    model = Task
    # specify fields we want to show in the form
    # __all__ lists out all model fields
    fields = '__all__'
    # redirect user back to task_list when item is created
    success_url = reverse_lazy('list')

# update view looks for template w/ model name prefix and _form.html 'task_form.html' by default
# gives a model form to work with, takes models & creates all fields by default
class TaskUpdate(UpdateView):
    model = Task
    # specify fields we want to show in the form
    # __all__ lists out all model fields
    fields = '__all__'
    # redirect user back to task_list when item is created
    success_url = reverse_lazy('list')

# delete view looks for template w/ model name prefix and _confirm_delete.html 'task_confirm_delete.html' by default
# gives a model form to work with, takes models & creates all fields by default
class TaskDelete(DeleteView):
    model = Task
    # change object name from default of 'object'
    context_object_name = 'task'
    # # specify fields we want to show in the form
    # # __all__ lists out all model fields
    # fields = '__all__'
    # redirect user back to task_list when item is created
    success_url = reverse_lazy('list')



'''
**** function based views for original build ***
# todo list homepage
def todo_list(request):
    if request.method == 'GET':
        tasks = Todo.objects.all().order_by('-task_id')
        form = TodoForm()
        return render(request=request,
                      template_name = 'list.html',
                      context = {'tasks':tasks, 'form':form})
    
    # when user submits form
    if request.method == 'POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            Todo.objects.create(task=task)
        # "redirect" to the todo homepage   
        return HttpResponseRedirect(reverse('todo'))


def task(request, task_id):
    if request.method == 'GET':
        todo = Todo.objects.get(pk=task_id)
        form = TodoForm(initial = {'task':todo.task})
        return render(request = request,
                      template_name = 'detail.html',
                      context = {
                          'form':form,
                          'task_id': task_id
                      })
    
    if request.method == 'POST':
        if 'save' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                task=form.cleaned_data['task']
                Todo.objects.filter(pk=task_id).update(task=task)
        elif 'delete' in request.POST:
            Todo.objects.filter(pk=task_id).delete()
        return HttpResponseRedirect(reverse('todo'))
'''