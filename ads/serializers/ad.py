from rest_framework import serializers

from ads.models.ad import Ad
from ads.models.category import Category
from ads.serializers.category import CategorySerializer
from users.models import User
from users.serializer import UserSerializer


class AdSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Ad
        fields = "__all__"


class AdCreateSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=User.objects.all(),
        slug_field='name'
    )

    category = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Category.objects.all(),
        slug_field='name'
    )

    def is_valid(self, raise_exception=False):
        self._author = self.initial_data.pop('author')
        self._category = self.initial_data.pop('category')
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):
        ad = Ad.objects.create(**validated_data)

        for author in self._author:
            obj, _ = User.objects.get(name=author)
            ad.author.add(obj)

        for category in self._category:
            obj, _ = Category.objects.get_or_create(name=category)
            ad.author.add(obj)

        return ad

    class Meta:
        model = Ad
        fields = '__all__'
