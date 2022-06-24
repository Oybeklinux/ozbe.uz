from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import FilterSet, DateFilter, NumberFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# sana va sonni ikki oraliq bo'yicha qidirish


class OrderFilter(FilterSet):
    min_price = NumberFilter(field_name="total", lookup_expr="gte")
    max_price = NumberFilter(field_name="total", lookup_expr="lte")
    start_date = DateFilter(field_name="created", lookup_expr="gte")
    end_date = DateFilter(field_name="created", lookup_expr="lte")


class ProductViewSet(viewsets.ModelViewSet):
    parser_classes = (JSONParser, FormParser, MultiPartParser)
    # permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Products.objects.all().order_by('id')
    serializer_class = ProductSerializer
    pagination_class = None

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'organization']
    # @ -fts PostgreSQL o'rnatgandan keyin ishlatilsin
    search_fields = ['^name']
    ordering_fields = ['name', 'price', 'organization']


class CategoryViewSet(viewsets.ModelViewSet):
    parser_classes = (JSONParser, FormParser, MultiPartParser)
    # permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name']
    search_fields = ['^name']

    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    pagination_class = None


class OrganizationViewSet(viewsets.ModelViewSet):
    parser_classes = (JSONParser, FormParser, MultiPartParser)
    # permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Organization.objects.all().order_by('id')
    serializer_class = OrganizationSerializer
    pagination_class = None


class ImagesViewSet(viewsets.ModelViewSet):
    parser_classes = (JSONParser, FormParser, MultiPartParser)
    # permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Images.objects.all().order_by('id')
    serializer_class = ImagesSerializer
    pagination_class = None


class SettingsViewSet(viewsets.ModelViewSet):
    queryset = Settings.objects.all()
    serializer_class = SettingsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = None


class OrderList(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    queryset = Order.objects.filter()
    filter_backends = [DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter]
    filterset_class = OrderFilter
    search_fields = ['^phone']
    ordering_fields = ['created']


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
