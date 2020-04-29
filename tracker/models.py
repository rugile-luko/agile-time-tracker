import datetime

from django.db import models


class Developer(models.Model):
    developer_first_name = models.CharField(max_length=100, verbose_name='First Name')
    developer_last_name = models.CharField(max_length=100, verbose_name='Last Name')

    def __str__(self):
        return '%s %s' % (self.developer_first_name, self.developer_last_name)


class Sprint(models.Model):
    sprint_name = models.CharField(max_length=100)

    def __str__(self):
        return self.sprint_name


class Story(models.Model):
    story_name = models.CharField(max_length=100, verbose_name='Story Title')
    estimated_story_time = models.DurationField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Stories"
        ordering = ['-date_added']

    def total_tasks(self):
        return Task.objects.filter(story=self).count()

    def total_tasks_time(self):
        total_tasks_time = datetime.timedelta(0, 0)
        for task in Task.objects.filter(story=self):
            total_tasks_time += task.total_hours()
        return total_tasks_time

    def __str__(self):
        return self.story_name


class Task(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    time_estimated = models.DurationField()
    datetime_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-datetime_added']

    def total_hours(self):
        total_hours = datetime.timedelta(0, 0)
        for time in TimeSpent.objects.filter(task=self):
            total_hours += time.time_spent
        return total_hours

    def __str__(self):
        return self.task_name


class TimeSpent(models.Model):
    time_spent = models.DurationField()
    date = models.DateField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
