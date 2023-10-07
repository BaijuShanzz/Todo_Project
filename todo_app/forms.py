from django import forms

from todo_app.models import todolist


class TodoForm(forms.ModelForm):
    class Meta:
        model = todolist
        fields = '__all__'