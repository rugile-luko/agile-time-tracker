from django import forms
from django.forms import TextInput
from django.urls import reverse
from . import models
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button


class CreateStory(forms.ModelForm):
    class Meta:
        model = models.Story
        fields = ['story_name', 'estimated_story_time']
        placeholders = {
            "story_name": 'Enter the name of the story',
            "estimated_story_time": 'Enter the estimated time of the story'
        }

    def __init__(self, *args, **kwargs):
        super(CreateStory, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn btn-secondary',
                                     onClick="window.location.href='{}';".format(reverse('home'))))

        for field, placeholder in self.Meta.placeholders.items():
            self.fields[field].widget.attrs['placeholder'] = placeholder


class CreateTask(forms.ModelForm):
    class Meta:
        model = models.Task
        exclude = ['story']
        placeholders = {
            'task_name': 'Enter the name of the task',
            'time_estimated': 'Enter the estimated time for the task'
        }

    def __init__(self, story, *args, **kwargs):
        self.story = story
        super(CreateTask, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))

        for field, placeholder in self.Meta.placeholders.items():
            self.fields[field].widget.attrs['placeholder'] = placeholder


class CreateTimeSpent(forms.ModelForm):
    class Meta:
        model = models.TimeSpent
        exclude = ['task', 'date']
        placeholders = {
            "time_spent": "00:00:00"
        }

    def __init__(self, task, *args, **kwargs):
        self.task = task
        super(CreateTimeSpent, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))

        for field, placeholder in self.Meta.placeholders.items():
            self.fields[field].widget.attrs['placeholder'] = placeholder


class AddDeveloper(forms.ModelForm):
    class Meta:
        model = models.Developer
        fields = '__all__'

        placeholders = {
            'developer_first_name': "Enter first name",
            'developer_last_name': "Enter last name"
        }

    def __init__(self, *args, **kwargs):
        super(AddDeveloper, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn btn-secondary',
                                     onClick="window.location.href='{}';".format(reverse('home'))))

        for field, placeholder in self.Meta.placeholders.items():
            self.fields[field].widget.attrs['placeholder'] = placeholder


class CreateSprint(forms.ModelForm):
    class Meta:
        model = models.Sprint
        fields = '__all__'

        placeholders = {
            'sprint_name': "Enter sprint name"
        }

    def __init__(self, *args, **kwargs):
        super(CreateSprint, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.add_input(Button('cancel', 'Cancel', css_class='btn btn-secondary',
                                     onClick="window.location.href='{}';".format(reverse('home'))))

        for field, placeholder in self.Meta.placeholders.items():
            self.fields[field].widget.attrs['placeholder'] = placeholder
