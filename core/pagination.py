from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'size'
    page_size = 20

    def get_paginated_response(self, data):

        return Response({
            'atual_page': self.page.number,
            'num_pages': self.page.paginator.num_pages,
            'num_itens': self.page.paginator.count,
            'has_previus': self.page.has_previous(),
            'has_next': self.page.has_next(),
            'results': data
        })
