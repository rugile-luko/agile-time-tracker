from datetime import timedelta
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from django.test import tag
from ..models import Story


@tag('integration')
class SeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super(SeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.story = Story.objects.create(story_name='Test Story', estimated_story_time=timedelta(0, 0))
        cls.host = 'http://127.0.0.1:8000/'

    @classmethod
    def tearDownClass(cls):
        super(SeleniumTests, cls).tearDownClass()
        cls.selenium.quit()

    def test_story_form_navigation_and_submission(self):
        self.selenium.get(self.host)
        self.selenium.find_element(By.CSS_SELECTOR, '#createStory').click()
        self.selenium.find_element(By.NAME, 'story_name').send_keys('Test Story Name')
        self.selenium.find_element(By.NAME, 'estimated_story_time').send_keys('00:20:00')
        self.selenium.find_element(By.ID, 'submit-id-submit').click()

    def test_developer_form_navigation_and_submission(self):
        self.selenium.get(self.host)
        self.selenium.find_element(By.CSS_SELECTOR, '#addSprint').click()
        self.selenium.find_element(By.NAME, 'sprint_name').send_keys('TestSprint')
        self.selenium.find_element(By.ID, 'submit-id-submit').click()

    def test_sprint_form_navigation_and_submission(self):
        self.selenium.get(self.host)
        self.selenium.find_element(By.CSS_SELECTOR, '#addDeveloper').click()
        self.selenium.find_element(By.NAME, 'developer_first_name').send_keys('Testfirstname')
        self.selenium.find_element(By.NAME, 'developer_last_name').send_keys('Testlastname')
        self.selenium.find_element(By.ID, 'submit-id-submit').click()

    def test_task_form_navigation_and_submission(self):
        self.selenium.get(self.host)
        self.selenium.find_element(By.CSS_SELECTOR, '.story-view-button:first-child').click()
        self.selenium.find_element(By.CSS_SELECTOR, '#createTask').click()
        self.selenium.find_element(By.NAME, 'task_name').send_keys('Testtaskname')
        self.selenium.find_element(By.NAME, 'developer').send_keys('Testfirstname Testlastname')
        self.selenium.find_element(By.NAME, 'sprint').send_keys('TestSprint')
        self.selenium.find_element(By.NAME, 'time_estimated').send_keys('02:00:00')
        self.selenium.find_element(By.ID, 'submit-id-submit').click()

    def test_time_form_navigation_and_submission(self):
        self.selenium.get(self.host)
        self.selenium.find_element(By.CSS_SELECTOR, '.story-view-button:first-child').click()
        self.selenium.find_element(By.CSS_SELECTOR, '.story-task-view-button:first-child').click()
        self.selenium.find_element(By.CSS_SELECTOR, '#createTime').click()
        self.selenium.find_element(By.NAME, 'time_spent').send_keys('00:45:00')
        self.selenium.find_element(By.ID, 'submit-id-submit').click()
