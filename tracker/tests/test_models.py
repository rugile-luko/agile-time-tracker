from datetime import timedelta

from django.test import TestCase, tag
from ..models import Story, Task, Developer, TimeSpent, Sprint


@tag('unit')
class TaskModelTests(TestCase):
    def setUp(self):
        self.story = Story.objects.create(story_name='Test Story', estimated_story_time=timedelta(0, 0))
        self.developer = Developer.objects.create(developer_first_name='Firstname', developer_last_name='Lastname')
        self.sprint = Sprint.objects.create(sprint_name='Sprintname')
        self.task = Task.objects.create(task_name='Test Task', developer=self.developer, time_estimated=timedelta(0, 0),
                                        story=self.story, sprint=self.sprint)
        self.task_time1 = TimeSpent.objects.create(time_spent=timedelta(0, 2), task=self.task)
        self.task_time2 = TimeSpent.objects.create(time_spent=timedelta(0, 4), task=self.task)

    def test_total_task_hours(self):
        self.assertEqual(self.task.total_hours(), timedelta(0, 6))

    def test_representation(self):
        self.assertEqual(str(self.task), "Test Task")


@tag('unit')
class StoryModelTests(TestCase):
    def setUp(self):
        self.story = Story.objects.create(story_name='Test Story', estimated_story_time=timedelta(0, 0))
        self.developer = Developer.objects.create(developer_first_name='Firstname', developer_last_name='Lastname')
        self.sprint = Sprint.objects.create(sprint_name='Sprintname')
        self.task1 = Task.objects.create(task_name='Test Task', developer=self.developer,
                                         time_estimated=timedelta(0, 0),
                                         story=self.story, sprint=self.sprint)
        self.task2 = Task.objects.create(task_name='Test Task2', developer=self.developer,
                                         time_estimated=timedelta(0, 0),
                                         story=self.story, sprint=self.sprint)
        self.task_time1 = TimeSpent.objects.create(time_spent=timedelta(0, 2), task=self.task1)
        self.task_time2 = TimeSpent.objects.create(time_spent=timedelta(0, 4), task=self.task1)
        self.task_time3 = TimeSpent.objects.create(time_spent=timedelta(0, 2), task=self.task2)
        self.task_time4 = TimeSpent.objects.create(time_spent=timedelta(0, 4), task=self.task2)

    def test_total_tasks(self):
        self.assertEqual(self.story.total_tasks(), 2)

    def test_total_tasks_time(self):
        self.assertEqual(self.story.total_tasks_time(), timedelta(0, 12))

    def test_representation(self):
        self.assertEqual(str(self.story), "Test Story")


class SprintModelTests(TestCase):
    def setUp(self):
        self.sprint = Sprint.objects.create(sprint_name='Test Sprint')

    def test_representation(self):
        self.assertEqual(str(self.sprint), "Test Sprint")
