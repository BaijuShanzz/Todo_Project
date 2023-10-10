from django.shortcuts import redirect, render


from todo_app.forms import TodoForm
from todo_app.models import todolist

# Create your views here.


def index(request):
    form = TodoForm()
   
    # submiting data
    if request.method == 'POST':
        form = TodoForm(request.POST)
        # checking validation
        if form.is_valid():
            # save value on data base
            form.save()
            # redirect page
            return redirect('index')
    # fetching data from database
    todos = todolist.objects.all()
    
    return render(request,"index.html",{'form': form, 'todos':todos})


def update(request, todo_id):
    todo = todolist.objects.get(id=todo_id)
    form = TodoForm(instance=todo)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,'update.html',{'form': form})


def delete(request,todo_id):
    if request.method == "POST":
        todolist.objects.get(id=todo_id).delete()
        return redirect('index')




    
