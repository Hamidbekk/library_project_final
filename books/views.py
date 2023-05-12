from requests import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, viewsets


class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# class BookListApiView(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer_data = BookSerializer(books, many=True).data
#         data = {
#             "status": f"Returned{len(books)} books",
#             "books": serializer_data
#         }
#         return Response(data)


class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# class BookCreateApiView(APIView):
#     def post(self, request):
#         data = request.data
#         serializer = BookSerializer(data=data)
#         if serializer.is_valid():
#             books = serializer.save()
#             data = {'status': f"{len(data)}Books are saved to the database",
#                     'books': books}
#             return Response(data)


class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer





