from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    poster = models.CharField(max_length=100)
    post_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, unique_for_date='post_date')
    description = models.TextField()

    class Meta:
        ordering = ['-post_date']

    def get_absolute_url(self):
        return reverse('detail', args=[
            self.post_date.year,
            self.post_date.month,
            self.post_date.day,
            self.slug
            ])

    def get_absolute_url_2(self):
        return reverse('add_comment', args=[
            self.post_date.year,
            self.post_date.month,
            self.post_date.day,
            self.slug
            ])

class About(models.Model):
    comment = models.CharField(max_length=255)
    description = models.TextField()
    quote = models.TextField()
    quote_author = models.CharField(max_length=100)
    my_skills_and_experiences = models.TextField()

class MySkill(models.Model):
    name = models.CharField(max_length=100)
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='my_skills')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name='categories')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, related_name='tags')

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='blog-image/')
    upload_date = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    about = models.OneToOneField(About, on_delete=models.CASCADE, related_name='images', null=True, blank=True)


class Email(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-send_date']

class EmailSite(models.Model):
    comment = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    email = models.EmailField()

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    send_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['-send_date']


class PrivacyPolicy(models.Model):
    comment = models.CharField(max_length=255)
    responsibility_of_contributors = models.TextField()
    gathering_of_personal_information = models.TextField()
    protection_of_personal_information = models.TextField()


class PolicyChanges(models.Model):
    change = models.CharField(max_length=255)
    policy = models.ForeignKey(PrivacyPolicy, on_delete=models.CASCADE, related_name='changes', null=True, blank=True)

    def __str__(self):
        return self.change
