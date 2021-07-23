from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import GroupSerializer
from .services import get_group_list


class GroupListAPIView(views.APIView):
    def get(self, request: Request):
        groups = get_group_list()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)
