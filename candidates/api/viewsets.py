from rest_framework.viewsets import ModelViewSet, generics
from candidates.models import Candidate
from candidates.api.serializers import CandidateSerializer, ReportSerializer

class CandidatesViewSet(ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    http_method_names=['get', 'patch']

class ReportViewSet(generics.ListAPIView):
    queryset = Candidate.objects.all().order_by('-votes_quantity')
    serializer_class = ReportSerializer