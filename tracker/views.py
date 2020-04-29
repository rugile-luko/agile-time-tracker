from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from . import models, forms


def home(request):
    stories = models.Story.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(stories, 8)

    try:
        stories = paginator.page(page)
    except PageNotAnInteger:
        stories = paginator.page(1)
    except EmptyPage:
        stories = paginator.page(paginator.num_pages)

    context = {
        'stories': stories
    }

    return render(request, 'home.html', context)


def create_story(request):
    if request.method == 'POST':
        form = forms.CreateStory(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The story was added successfully!')
            return redirect('home')
    else:
        form = forms.CreateStory()

    context = {'form': form}

    return render(request, 'create_story.html', context)


def story_view(request, pk):
    story = get_object_or_404(models.Story, pk=pk)
    tasks = models.Task.objects.all().filter(story=story)

    page = request.GET.get('page', 1)
    paginator = Paginator(tasks, 8)

    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    context = {
        "story": story,
        "tasks": tasks
    }

    return render(request, 'story_view.html', context)


def create_task(request, pk):
    story = get_object_or_404(models.Story, pk=pk)
    if request.method == 'POST':
        form = forms.CreateTask(story, request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.story = story
            new_form.save()
            messages.success(request, 'The task was added successfully!')
            return redirect('story_view', pk=pk)
    else:
        form = forms.CreateTask(story)

    context = {
        'form': form,
        'story': story
    }

    return render(request, 'create_task.html', context)


def task_view(request, pk, task_pk):
    task = get_object_or_404(models.Task, story__pk=pk, pk=task_pk)
    hours_spent = models.TimeSpent.objects.all().filter(task=task)

    context = {
        "task": task,
        "hours_spent": hours_spent
    }

    return render(request, "task_view.html", context)


def create_time(request, pk, task_pk):
    task = get_object_or_404(models.Task, story=pk, pk=task_pk)
    if request.method == 'POST':
        form = forms.CreateTimeSpent(task, request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.task = task
            new_form.save()
            messages.success(request, 'The time was added successfully!')
            return redirect('task_view', pk=pk, task_pk=task_pk)
    else:
        form = forms.CreateTimeSpent(task)

    context = {
        "task": task,
        "form": form
    }

    return render(request, "create_time_spent.html", context)


def add_developer(request):
    if request.method == 'POST':
        form = forms.AddDeveloper(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The developer was added successfully!')
            return redirect('home')

    else:
        form = forms.AddDeveloper()

    context = {
        "form": form
    }

    return render(request, 'add_developer.html', context)


def create_sprint(request):
    if request.method == 'POST':
        form = forms.CreateSprint(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'The sprint was added successfully!')
            return redirect('home')

    else:
        form = forms.CreateSprint()

    context = {"form": form}

    return render(request, 'create_sprint.html', context)
