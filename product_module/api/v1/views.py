from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from product_module.views import *
from .filters import ProductFilter
from .permissions import IsAdminOrReadOnly
from .serializers import *


class ProductAPIView(ModelViewSet):
    queryset = Product.objects.filter(is_active=True, is_delete=False)
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ProductFilter
    # ordering_fields = ["-created_date"]
    ordering = ['-created_date']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_delete = True
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductCategoryAPIView(ModelViewSet):
    queryset = ProductCategory.objects.filter(is_active=True, is_delete=False, parent=None)
    serializer_class = ProductCategorySerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {"title": ["exact"]}
    ordering = ['-created_date"']


class ProductBrandAPIView(ModelViewSet):
    queryset = ProductBrand.objects.filter(is_active=True)
    serializer_class = ProductBrandSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {"title": ["exact"]}
    ordering = ['english_title']
