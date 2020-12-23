from django.test import TestCase  # noqa: F401
from .models import Tag, TaskStatus, Task  # noqa: F401


# Create your tests here.
class TagModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='TestTag')

    def test_name_max_length(self):
        tag = Tag.objects.get(id=1)
        max_length = tag._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)


class TaskStatusModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        TaskStatus.objects.create(name='TestTaskStatus')

    def test_name_max_length(self):
        task_status = TaskStatus.objects.get(id=1)
        max_length = task_status._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)
