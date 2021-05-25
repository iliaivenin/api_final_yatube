from rest_framework import serializers

from .models import Comment, Follow, Group, Post


# class PostSerializer(serializers.ModelSerializer):
#     author = serializers.ReadOnlyField(source='author.username')

#     class Meta:
#         fields = ('id', 'text', 'author', 'pub_date')
#         model = Post


# class CommentSerializer(serializers.ModelSerializer):
#     author = serializers.ReadOnlyField(source='author.username')

#     class Meta:
#         fields = ('id', 'author', 'post', 'text', 'created')
#         model = Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    following = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Follow


class GroupSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Group
