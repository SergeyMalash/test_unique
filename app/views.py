from django.db import transaction
from rest_framework.generics import ListCreateAPIView

from app.models import TestIP
from app.serializers import TestIPSerializer


class IPListCreateAPIView(ListCreateAPIView):
    serializer_class = TestIPSerializer
    queryset = TestIP.objects.all()

    # @transaction.atomic
    def create(self, request, *args, **kwargs):
        return super(IPListCreateAPIView, self).create(request, *args, **kwargs)
