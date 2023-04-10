from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination, BasePagination

class CustomPagination(PageNumberPagination):
    page_size = 8
