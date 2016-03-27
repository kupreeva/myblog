# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse #для get_absolute_url
from django.template.defaultfilters import slugify # Это библиотека для преобразования заголовков в ссылки
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50, unique = True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return  self.title

class Tag(models.Model):
    title = models.CharField(max_length=200, unique=True)
    #slug = models.SlugField(verbose_name='URL', max_length=200, unique=True, blank=True)

    def __unicode__(self):
        return self.title

class Like(models.Model):
    user = models.ForeignKey('auth.User', blank=True, null=True)
    post = models.ForeignKey('Post', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)#автоматически выставлять и изменить название переменной, чтоб не с like начиналось

    def __unicode__(self):
        return str(self.created_at)

class Post(models.Model):

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='/home/kristina/virtual/project_one/mysite', blank=True, null=True)#картинка на заставке поста
    categories = models.ManyToManyField(Category, blank=True)
    slug = models.CharField(verbose_name='URL', max_length=200, blank=True) # Поле для записи ссылки
    text = models.TextField()
    tease = models.TextField('Tease', blank=True) #вступление к статье, которое будет представляться в списке
    is_draft = models.BooleanField(default=True)#Черновик или опубликовано?
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(default = timezone.now, blank=True, null=True)
    allow_comments = models.BooleanField(verbose_name="allow comments", default=True)
    tags = models.ManyToManyField(Tag, verbose_name='Tags', blank=True) #тэги

    def publish(self): #метод публикации записи
        self.published_date = timezone.now()
        self.save()


    def get_absolute_url(self):
        return reverse('post.details', args=[str(self.id)])

    def __unicode__(self):
        return self.title
