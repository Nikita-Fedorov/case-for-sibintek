from rest_framework import generics
from myself.models import Myself
from api.serializers import MyselfSerializer


class MyselfAPIView(generics.ListAPIView):
    queryset = Myself.objects.all()
    serializer_class = MyselfSerializer
