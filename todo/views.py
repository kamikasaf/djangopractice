from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from .models import News
from .serializers import NewsSerializer

@api_view()
def new_list(request):
    news = News.objects.all()       # получить все новости
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)

# class NewsList(APIView):
#     def get(self, request):
#         news = News.objects.all()       # получить все новости
#         serializer = NewsSerializer(news, many=True)
#         return Response(serializer.data)

#create(POST), list, retrieve(GET)(детали, когда 1 обьект), update(PUT), partial_update(PATCH), destroy(DELETE)

class NewsList(ListAPIView):
     queryset = News.objects.all()
     serializer_class = NewsSerializer
