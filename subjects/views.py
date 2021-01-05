from rest_framework import views
from rest_framework.request import Request
from rest_framework.response import Response


from schedule.models import Subject
from schedule.serializers import SubjectSerializer
from subjects.serializers import SubjectDetailSerializer


class SubjectListView(views.APIView):
    def get(self, request: Request):
        subjs = Subject.objects.all()
        serializer = SubjectDetailSerializer(subjs, many=True)
        return Response(serializer.data, status=200)


class SubjectAPIView(views.APIView):
    """View для отображения информации о конкретном предмете"""
    def get(self, request: Request, id):
        try:
            subj = Subject.objects.get(id=int(id))
        except Subject.DoesNotExist:
            return Response(status=404)
        else:
            serializer = SubjectDetailSerializer(subj, many=False)
            return Response(serializer.data, status=200)
