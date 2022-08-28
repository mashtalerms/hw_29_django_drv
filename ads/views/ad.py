from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView

from ads.models.ad import Ad
from ads.serializers.ad import AdSerializer, AdCreateSerializer


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):

        categories = request.GET.getlist('cat', None)
        if categories:
            self.queryset = self.queryset.filter(category_id__in=categories)

        text = request.GET.get('text', None)
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        location = request.GET.get('location', None)
        if location:
            self.queryset = self.queryset.filter(author__location__name__icontains=location)

        price_from = request.GET.get('price_from', None)
        price_to = request.GET.get('price_to', None)
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().get(request, *args, **kwargs)


class AdRetrieveView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdDestroyView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateSerializer


# search_by = None

# search_by_cat = request.GET.get('cat', None)
# search_by_text = request.GET.get('text', None)
# search_by_location = request.GET.get('location', None)
# search_by_price_from = request.GET.get('price_from', None)
# search_by_price_to = request.GET.get('price_to', None)

# if search_by_cat:
#     search_by = search_by_cat

# def get_queryset(self):


@method_decorator(csrf_exempt, name="dispatch")
class AdUpdateImageView(UpdateView):
    """Ads update image View"""
    model = Ad
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author.username,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category": self.object.category.name,
            "image": self.object.image.url if self.object.image else None,
        }, json_dumps_params={'ensure_ascii': False})
