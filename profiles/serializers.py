from rest_framework import serializers
from .models import Profiles
from posts.serializers import PostSerializer
from posts.models import Posts

#
# class ProfileSerializer(serializers.Serializer):
#     phone_number = serializers.CharField(max_length=11)
#     first_name = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=100)
#
#     def create(self, validated_data):
#         return Profiles.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.phone_number = validated_data.get('phone_number')
#         instance.first_name = validated_data.get('first_name')
#         instance.last_name = validated_data.get('last_name')
#         instance.save()
#         return instance

# Model Serializer

class ProfileSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)
    post = PostSerializer(write_only=True)

    class Meta:
        model = Profiles
        fields = '__all__'

    def create(self, validated_data):
        post = validated_data.pop('post')
        my_profile = Profiles.objects.create(**validated_data)
        my_post = Posts.objects.create(**post, author=my_profile)
        return my_profile 
