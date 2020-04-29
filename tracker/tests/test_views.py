from datetime import timedelta

from django.test import TestCase, tag
from django.urls import reverse, resolve
from ..views import home, story_view, task_view
from ..models import Story, Task, Developer, TimeSpent, Sprint
from ..forms import CreateStory, CreateTask, CreateTimeSpent, AddDeveloper, CreateSprint


@tag('unit')
class HomeTests(TestCase):
    def setUp(self):
        self.url = reverse('home')

    def test_home_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_page_not_an_integer(self):
        url = self.url + "?page=a"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_empty_page(self):
        url = self.url + "?page=100"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


@tag('unit')
class NewStoryTests(TestCase):
    def setUp(self):
        self.url = reverse('create_story')

    def test_contains_form(self):
        response = self.client.get(self.url)
        form = response.context.get('form')
        self.assertIsInstance(form, CreateStory)

    def test_csrf(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_story_valid_data(self):
        data = {
            'story_name': 'Test title',
            'estimated_story_time': timedelta(0, 0)
        }
        response = self.client.post(self.url, data)
        self.assertTrue(Story.objects.exists())

    def test_new_story_invalid_data(self):
        response = self.client.post(self.url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

    def test_new_story_invalid_data_empty_fields(self):
        data = {
            'story_name': '',
            'estimated_story_time': ''
        }
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Story.objects.exists())


@tag('unit')
class StoryViewTests(TestCase):
    def setUp(self):
        self.url = reverse('story_view', kwargs={'pk': 1})
        Story.objects.create(story_name='Test Story', estimated_story_time=timedelta(0, 0))

    def test_story_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_story_url_resolves_story_view(self):
        view = resolve(self.url)
        self.assertEquals(view.func, story_view)

    def test_story_page_not_an_integer(self):
        url = self.url + "?page=a"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_empty_page(self):
        url = self.url + "?page=100"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


@tag('unit')
class NewTaskTests(TestCase):
    def setUp(self):
        self.url = reverse('create_task', kwargs={"pk": 1})
        self.story = Story.objects.create(story_name='Test Story', estimated_story_time=timedelta(0, 0))
        self.developer = Developer.objects.create(developer_first_name='Firstname', developer_last_name='Lastname')
        self.sprint = Sprint.objects.create(sprint_name='Sprintname')

    def test_contains_form(self):
        response = self.client.get(self.url)
        form = response.context.get('form')
        self.assertIsInstance(form, CreateTask)

    def test_csrf(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_task_valid_data(self):
        data = {
            'story': self.story.pk,
            'task_name': 'Test title',
            'developer': self.developer.pk,
            'sprint': self.sprint.pk,
            'time_estimated': timedelta(0, 0)
        }
        response = self.client.post(self.url, data)
        self.assertTrue(Task.objects.exists())

    def test_new_task_invalid_data(self):
        response = self.client.post(self.url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

    def test_new_task_invalid_data_empty_fields(self):
        data = {
            'task_name': '',
            'developer': '',
            'sprint': '',
            'time_estimated': ''
        }
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Task.objects.exists())


@tag('unit')
class TaskViewTests(TestCase):
    def setUp(self):
        self.url = reverse('task_view', kwargs={'pk': 1, 'task_pk': 1})
        self.story = Story.objects.create(story_name='Test Story', estimated_story_time=timedelta(0, 0))
        self.developer = Developer.objects.create(developer_first_name='Firstname', developer_last_name='Lastname')
        self.sprint = Sprint.objects.create(sprint_name='Sprintname')
        Task.objects.create(task_name='Test Task', developer=self.developer, time_estimated=timedelta(0, 0),
                            story=self.story, sprint=self.sprint)

    def test_task_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200)

    def test_task_url_resolves_task_view(self):
        view = resolve(self.url)
        self.assertEquals(view.func, task_view)


@tag('unit')
class NewTimeTests(TestCase):
    def setUp(self):
        self.url = reverse('create_time', kwargs={"pk": 1, "task_pk": 1})
        self.story = Story.objects.create(story_name='Test Story', estimated_story_time=timedelta(0, 0))
        self.developer = Developer.objects.create(developer_first_name='Firstname', developer_last_name='Lastname')
        self.sprint = Sprint.objects.create(sprint_name='Sprintname')
        self.task = Task.objects.create(task_name='Test Task', developer=self.developer, time_estimated=timedelta(0, 0),
                                        story=self.story, sprint=self.sprint)

    def test_contains_form(self):
        response = self.client.get(self.url)
        form = response.context.get('form')
        self.assertIsInstance(form, CreateTimeSpent)

    def test_csrf(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_task_valid_data(self):
        data = {
            'time_spent': timedelta(0, 0),
            'task': self.task
        }
        response = self.client.post(self.url, data)
        self.assertTrue(TimeSpent.objects.exists())

    def test_new_task_invalid_data(self):
        response = self.client.post(self.url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

    def test_new_task_invalid_data_empty_fields(self):
        data = {
            'time_spent': '',
            'task': ''
        }
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(TimeSpent.objects.exists())


@tag('unit')
class NewDeveloperTests(TestCase):
    def setUp(self):
        self.url = reverse('add_developer')

    def test_contains_form(self):
        response = self.client.get(self.url)
        form = response.context.get('form')
        self.assertIsInstance(form, AddDeveloper)

    def test_csrf(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_developer_valid_data(self):
        data = {
            'developer_first_name': 'Test',
            'developer_last_name': 'Newtest'
        }
        response = self.client.post(self.url, data)
        self.assertTrue(Developer.objects.exists())

    def test_new_developer_invalid_data(self):
        response = self.client.post(self.url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

    def test_new_developer_invalid_data_empty_fields(self):
        data = {
            'developer_first_name': '',
            'developer_last_name': ''
        }
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Developer.objects.exists())


@tag('unit')
class NewSprintTests(TestCase):
    def setUp(self):
        self.url = reverse('create_sprint')

    def test_contains_form(self):
        response = self.client.get(self.url)
        form = response.context.get('form')
        self.assertIsInstance(form, CreateSprint)

    def test_csrf(self):
        response = self.client.get(self.url)
        self.assertContains(response, 'csrfmiddlewaretoken')

    def test_new_developer_valid_data(self):
        data = {
            'sprint_name': 'TestSprint'
        }
        response = self.client.post(self.url, data)
        self.assertTrue(Sprint.objects.exists())

    def test_new_developer_invalid_data(self):
        response = self.client.post(self.url, {})
        form = response.context.get('form')
        self.assertEquals(response.status_code, 200)
        self.assertTrue(form.errors)

    def test_new_developer_invalid_data_empty_fields(self):
        data = {
            'sprint_name': '',
        }
        response = self.client.post(self.url, data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(Sprint.objects.exists())
