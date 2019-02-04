from rest_framework.views import APIView
from rest_framework.response import Response
from statuses.models import Status
from .serializers import StatusSerializer
from rest_framework import generics

class StatusListSearchAPIView(APIView):

    def get(self, reqeust, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)

    def POST(self, reqeust, format=None):
        qs = Status.objects.all()
        serializer = StatusSerializer(qs, many=True)
        return Response(serializer.data)


class StatusCreateAPIView(generics.CreateAPIView):

    queryset    = Status.objects.all()
    serializer_class = StatusSerializer

 

