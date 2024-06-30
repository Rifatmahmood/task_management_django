from django import forms
from .models import TaskModel
from category.models import TaskCategory


class TaskForm(forms.ModelForm):
    categories = forms.ModelMultipleChoiceField(
        queryset=TaskCategory.objects.all(),
        required=False,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = TaskModel
        fields = [
            "taskTitle",
            "taskDescription",
            "categories",
            "task_assign_date",
            "is_completed",
        ]
        widgets = {
            "task_assign_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
