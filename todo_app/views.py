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

    
