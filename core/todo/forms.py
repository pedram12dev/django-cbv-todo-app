from django import forms
from .models import Task

# Reordering Form and View


class TaskUpdateForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "enter the title",
            }
        ),
    )

    class Meta:
        model = Task
        fields = ("title",)