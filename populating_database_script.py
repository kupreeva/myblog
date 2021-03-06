# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

import django
django.setup()

from myblog.models import Post, Category, Tag, Like
from django.contrib.auth.models import User
import string
import random

def populate():
    #add_post()
    #add_user()
    #for u in User.objects.all():
    #    print str(u.username)
    #add_cat()
    # Выводим на экран пользователю то, что мы добавили в базу
    #for c in Category.objects.all():
    #    print str(c)

def add_user():
    name_of_user = rand_string(random.randint(3,10))
    user_password = rand_string(random.randint(8,15))
    u = User.objects.create_user(username = name_of_user, password = user_password)
    return u

def add_post():
    text_in_post = rand_string(random.randint(100,1000))
    title_of_post = rand_string(random.randint(50,255))
    author_of_post = random.choice(User.objects.all())
    p = Post.objects.get_or_create(title = title_of_post, text = text_in_post, author = author_of_post)
    return p

def add_cat():
    number = random.randint(0,50)# Целое число из указанного диапазона, 50 max длина названия категории, указанная в models.py
    name_of_category = rand_string(number)
    c = Category.objects.get_or_create(title=name_of_category)
    return c

def rand_string(n):
    a = string.ascii_letters + string.digits
    return ''.join([random.choice(a) for i in range(n)])


if __name__ == '__main__':
    print "Starting script..."
    populate()
