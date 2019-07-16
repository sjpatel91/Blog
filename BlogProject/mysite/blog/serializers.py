'''
Created on Jul 15, 2019

@author: sjpat
'''
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("author","title","text","create_date",) 
