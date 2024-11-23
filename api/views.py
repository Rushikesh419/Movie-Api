from django.shortcuts import render
from .models import Movie
from .serializer import MovieSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class MovieAPI(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            movie=Movie.objects.get(id=id)
            serializer=MovieSerializer(movie)
            return Response(serializer.data)
        movie=Movie.objects.all()
        serializer=MovieSerializer(movie,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,format=None):
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None,format=None):
        id=pk
        movie=Movie.objects.get(pk=id)
        serializer=MovieSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'data updated'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk=None,format=None):
        id=pk
        movie=Movie.objects.get(pk=id)
        serializer=MovieSerializer(movie,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'partial data updated'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk=None,format=None):
        id=pk
        movie=Movie.objects.get(pk=id)
        movie.delete()
        return Response({'msg':'data deleted'},status=status.HTTP_204_NO_CONTENT)






































    
   