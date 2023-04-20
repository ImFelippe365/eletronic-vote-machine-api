from rest_framework import serializers
from candidates.models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'name', 'vote_number', 'votes_quantity']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ['id', 'name', 'vote_number', 'votes_quantity']