from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.contrib.contenttypes.fields import GenericRelation




STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='mblog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField(upload_to='media/img', blank=True, null=True)
    video = models.FileField(upload_to='media/videos', blank=True, null=True)

class Rating(models.Model):
    post = models.ForeignKey(Post, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    score = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user', 'ip_address')

    def __str__(self):
        return f"{self.post.title} - {self.score}"


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse("post_detail", kwargs={"slug": str(self.slug)})



class ProfileImage(models.Model):
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)



class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return "Comment {} by {}".format(self.body, self.name)


class ContactInfo(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    birth_day = models.DateField()
    email = models.EmailField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"