from django.test import TestCase
from django.urls import reverse
from .models import Tag, TaskStatus, Task
from users.models import CustomUser


# Create your tests here.
class TaskTest(TestCase):

    def setUp(self):
        user1 = CustomUser.objects.create_user(username='user1',
                                               password='12345',
                                               email='1@mail.ru')
        user1.save()
        user2 = CustomUser.objects.create_user(username='user2',
                                               password='09876',
                                               email='2@mail.ru')
        user2.save()
        status = TaskStatus.objects.create(name='TestTaskStatus')
        status.save()
        tag1 = Tag.objects.create(name='TestTag1')
        tag1.save()
        tag2 = Tag.objects.create(name='TestTag2')
        tag2.save()
        task = Task.objects.create(
            name='Go home',
            description='Faster!',
            status=status,
            creator=user1,
            assigned_to=user2,
        )
        task.tags.set((tag1, tag2))
        task.save()

    def test_tag(self):
        tag = Tag.objects.get(id=1)
        self.assertTrue(isinstance(tag, Tag))
        max_length = tag._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)

    def test_status(self):
        task_status = TaskStatus.objects.get(id=1)
        self.assertTrue(isinstance(task_status, TaskStatus))
        max_length = task_status._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)
        task_status.name = 'new_name'
        name = task_status.__str__()
        self.assertEquals(name, 'new_name')
        task_status.delete()
        self.assertEqual(TaskStatus.objects.count(), 0)

    def test_task(self):
        task = Task.objects.get(id=1)
        self.assertTrue(isinstance(task, Task))
        max_length = task._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)
        task.name = 'new_name'
        name = task.__str__()
        self.assertEquals(name, 'new_name')
        assert task.description == 'Faster!'
        task.description = 'blablabla'
        assert task.description == 'blablabla'
        task.delete()
        self.assertEqual(Task.objects.count(), 0)

    def test_index_view(self):
        resp = self.client.get('/tasks/')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(reverse('tasks'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'tasks/tasks.html')

    def test_user_login(self):
        self.client.login(username='user1', password='12345')
        resp = self.client.get(reverse('statuses'))
        self.assertEqual(str(resp.context['user']), 'user1')
        self.assertEqual(resp.status_code, 200)
