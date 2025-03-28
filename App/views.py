from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TestApi(APIView):
    def get(self, request):
        print("ok----------")
        return Response(data={
            "name": "fahadsssssssssss"
        },status=status.HTTP_200_OK)
