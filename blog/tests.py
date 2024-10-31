from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')

        testuser1 = User.objects.create_user(
            username='test_user1', password='123456789')
        testuser1.save()

        test_post = Post.objects.create(
            category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1, status='published')
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user1')
        self.assertEqual(title, 'Post Title')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), "Post Title")
        self.assertEqual(str(cat), "django")

    def test_post_update(self):
        client = APIClient()
        self.test_category = Category.objects.create(name='django'
        )
        self.testuser1 = User.objects.create_user(username="test_user2",password="12345678")
        self.testuser2 = User.objects.create_user(username="test_user3",password="12345678")

        test_post = Post.objects.create(
            category_id=1, title='Post Title', excerpt='Post Excerpt', content='Post Content', slug='post-title', author_id=1, status='published')
        test_post.save()

        client.login(username=self.testuser1.username,password='12345678')

        url = reverse(('blog_api:detailcreate'),kwargs={'pk':2})
        response = client.put(
            url,{
                "title": "Title",
                "author": 2,
                "excerpt": "Exercept",
                "content": "Content",
                "status": "published"
            }, format='json'
        )
        print(f'n/n/n/n/n/n/n/n/n/n{response.data}/n/n/n')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
