from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse




class Post(models.Model):
    title = models.CharField(max_length = 256)
    author = models.ForeignKey('auth.User')
    text = models.TextField()
    creation_date = models.DateTimeField(default = timezone.now())
    publish_date = models.DateTimeField(blank = True, null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_main:blog_detail', kwargs = {'pk': self.pk})

    def publish_post(self):
        self.publish_date = timezone.now()
        self.save()

    def approve_comment(self):
        self.comments.filter(aproved_comment = True)
        self.save()


class post_comment(models.Model):
    author = models.CharField(max_length = 256)
    post = models.ForeignKey(Post, related_name='comments')
    text = models.TextField()
    creation_date = models.DateTimeField(default = timezone.now())
    aproved_comment = models.BooleanField(default = False)
    approved_date = models.DateTimeField(blank = True, null = True)


    def __str__(self):
        return self.author

    def aprove_comment(self):
        self.aproved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('blog_main:post_list')












    # Create your models here.
