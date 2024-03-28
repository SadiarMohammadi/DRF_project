from posts.models import Posts
from rest_framework import serializers
from profiles.models import Profiles


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'
        extra_kwargs = {'author': {'required': False}}
