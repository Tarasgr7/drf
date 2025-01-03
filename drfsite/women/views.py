# from django.shortcuts import render
# from rest_framework import generics
# from women.serializers import WomenSerializer
from turtle import title

from django.forms import model_to_dict
from women.models import Women
# class WomenAPIView(generics.ListAPIView):
#     queryset=Women.objects.all()
#     serializer_class=WomenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
class WomenAPIView(APIView):
    def get(self,request):
        lst=Women.objects.all().values()
        return Response({'posts':lst})
    def post(self,request):
        post_new=Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id'],
        )
        return Response({'post':model_to_dict(post_new)})