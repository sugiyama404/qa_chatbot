from django.shortcuts import render

import django_filters
from rest_framework import viewsets, filters

from .models import Ghostintheshell
from .serializer import GhostintheshellSerializer
from rest_framework.response import Response

class GhostintheshellViewSet(viewsets.ModelViewSet):
    queryset = Ghostintheshell.objects.all()
    serializer_class = GhostintheshellSerializer

    # POST送信で「質問」を受け取り、データベースで検索を行い「質問」と一致するものを探す。一致すれば、「答え」を返す。
    # Receive a "question" by sending a POST and search the database for a match to the "question. If a match is found, an "answer" is returned.
    def create(self, request, *args, **kwargs):
        question = request.data.get('question')
        queryset = Ghostintheshell.objects.filter(question=question)
        serializer = GhostintheshellSerializer(queryset, many=True)
        return Response(serializer.data)
