from django.shortcuts import render, redirect
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from .forms import FeedBackForm
from django.views.generic import View, ListView, TemplateView
from feedback.models import FeedBack
from .serializers import FeedbackSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated



class FeedBackView(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        feedback = FeedBack.objects.all()
        serializer = FeedbackSerializer(feedback, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = FeedbackSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return redirect("http://127.0.0.1:8000")
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class FeedbackDetails(APIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return FeedBack.objects.get(id=id)
    
        except FeedBack.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):
        article = self.get_object(id)
        serializer = FeedbackSerializer(article)
        return Response(serializer.data)

    def put(self, request, id):
        article = self.get_object(id)
        serializer = FeedbackSerializer(article, data = request.data)    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        article = self.get_object(id)
        article.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)