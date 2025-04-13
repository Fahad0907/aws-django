from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .task import test_func


class TestApi(APIView):
    def get(self, request):
        print("ok----------")
        test_func.delay()
        return Response(data={
            "name": "fahadsssssssssssssdfasedfs"
        },status=status.HTTP_200_OK)
