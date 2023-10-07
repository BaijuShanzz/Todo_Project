from django.shortcuts import render


from todo_app.forms import TodoForm

# Create your views here.


def index(request):
    form = TodoForm()
    return render(request,"index.html",{'form': form})

    
