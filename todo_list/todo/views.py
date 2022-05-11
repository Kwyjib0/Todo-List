from django.shortcuts import render, redirect 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy # redirects user to certain part of application (similar to reverse)

from django.contrib.auth.views import LoginView

# mixin to restrict user access if not logged in, otherwise
# done with decorators in function based views or by writing middleware
from django.contrib.auth.mixins import LoginRequiredMixin
# built in form
from django.contrib.auth.forms import UserCreationForm
# logs user in directly once registers
from django.contrib.auth import login

from .models import Task
# below removed after switching to built in views:
# from .forms import TodoForm
# from django.http import HttpResponseRedirect
# from django.urls import reverse

# could use loginview directly but this customizes it
class CustomLoginView(LoginView):
    # no model used
    template_name = 'todo/login.html'
    # include all fields from default form
    fields = '__all__'
    # built in attribute to redirect user if already logged in
    redirect_authenticated_user = True

    # redirect user to list page after logs in
    def get_success_url(self):
        return reverse_lazy('list')

# create user account
class RegisterPage(FormView):
    # no model used
    template_name = 'todo/register.html'
    # use built in user creation form
    form_class = UserCreationForm
    # built in attribute to redirect user if already logged in
    redirect_authenticated_user = True
    # redirect user to list page after registered
    success_url = reverse_lazy('list')

    # check submitted user creation form
    def form_valid(self, form):
        user = form.save()
        # check if user was successfully created
        if user is not None:
            # authenticate user
            login(self.request, user)
        # otherwise continue with registration
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        # block authenticated user from registration page
        # and redirect to task list page
        if self.request.user.is_authenticated:
            return redirect('list')
        return super(RegisterPage, self).get(*args, **kwargs)

# list view is a template for displaying a list of object, often a queryset
# will find proper template w/ model name prefix and _list.html 'task_list.html' by default
# mixin restricting access to logged in users added
class TaskList(LoginRequiredMixin, ListView):
    # requires a model or a queryset
    model = Task
    # change queryset name from default of 'object_list'
    context_object_name = 'tasks'

    # override get_context_data so that only task data specific to the logged 
    # in user are displayed, otherwise we are returning all tasks for every user
    def get_context_data(self, **kwargs):
        # set context value to original, inherit from original item
        context = super().get_context_data(**kwargs)
        # filter for only tasks for this specific user
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        # and filter for uncompleted tasks
        context['count'] = context['tasks'].filter(complete=False)
        # get value by form name, make empty string by default if no search value entered
        search_input = self.request.GET.get('search-area') or ''
        # check if search value entered
        if search_input:
            # check if any task contains search value
            context['tasks'] = context['tasks'].filter(task__startswith=search_input)
        # pass to template
        context['search_input'] = search_input
        return context

# detail view returns info about a specific item / object instance
# will find proper template w/ model name prefix and _detail.html 'task_detail.html' by default
# mixin restricting access to logged in users added
class TaskDetail(LoginRequiredMixin, DetailView):
    # requires a model or a queryset
    model = Task
    # change object name from default of 'object'
    context_object_name = 'task'
    # will look for task_detail.html by default unless change template name here
    template_name = 'todo/task.html'

# create view looks for template w/ model name prefix and _form.html 'task_form.html' by default
# gives a model form to work with, takes models & creates all fields by default
# mixin restricting access to logged in users added
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # specify fields we want to show in the form
    # __all__ lists out all model fields, create list of wanted fields
    fields = ['task', 'description', 'complete']
    # redirect user back to task_list when item is created
    success_url = reverse_lazy('list')

    # override built in form_valid method for create views
    # customize so user is automatically set to logged in user
    # pass in original form view automatically creates
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)



# update view looks for template w/ model name prefix and _form.html 'task_form.html' by default
# gives a model form to work with, takes models & creates all fields by default
# mixin restricting access to logged in users added
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    # specify fields we want to show in the form
    # __all__ lists out all model fields, create list of wanted fields
    fields = ['task', 'description', 'complete']
    # redirect user back to task_list when item is created
    success_url = reverse_lazy('list')

# delete view looks for template w/ model name prefix and _confirm_delete.html 'task_confirm_delete.html' by default
# gives a model form to work with, takes models & creates all fields by default
# mixin restricting access to logged in users added
class TaskDelete(LoginRequiredMixin, DeleteView):
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