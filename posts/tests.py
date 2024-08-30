from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.

class PostModelTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text = 'just a test')
    
    
    def test_text_content(self):
        post = Post.objects.get(id = 1)
        excepted_object_name = f'{post.text}'
        self.assertEqual(excepted_object_name,'just a test')


class HomePageViewTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text='this is anther test')
    
    
    def test_view_url_exists_at_proper_loction(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code,200)
        
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
    
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code,200)
        self.assertTemplateUsed(resp,'home.html')