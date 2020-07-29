from django.test import TestCase
from blog.models import Comment

# Create your tests here.
class CommentTestCase(TestCase):
    def setup(self):
        print('setup activity')
        Comment.objects.create(name='asdaj',email='lijfsjf@gmail.com',body='slkjefs',created='2020-04-15 13:41',updated='2020-04-1 13:41',active='True')

    def test_comment_info(self):
        print('testing Comment Information')
        qs=Comment.objects.all()
        self.assertEqual(qs.count(),0)
        c1=Comment.objects.get(name='asdaj')
        self.assertEqual(c1.get_email(),'lijfsjf@gmail.com')
