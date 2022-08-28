from rest_framework.viewsets import ModelViewSet

from ads.models.category import Category
from ads.serializers.category import CategorySerializer


class CategoryViewSet(ModelViewSet):
    """Category View Set for whole CRUD"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
