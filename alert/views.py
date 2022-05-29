from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from . models import *
# Create your views here.

@api_view(['GET'])
def apiOverview(request):

	api_urls = {

					#Birthday

					'birthday-list',
					'birthday-detail/<str:pk>',
					'birthday-create',
					'birthday-update/<str:pk>/',
					'birthday-delete/<str:pk>/',



					'mothersday-list',
					'mothersday-detail/<str:pk>',
					'mothersday-create',
					'mothersday-update/<str:pk>/',
					'mothersday-delete/<str:pk>/',

					
					'relanni-list',
					'relanni-detail/<str:pk>',
					'relanni-create',
					'relanni-update/<str:pk>/',
					'relanni-delete/<str:pk>/',



					'marranni-list',
					'marranni-detail/<str:pk>',
					'marranni-create',
					'marranni-update/<str:pk>/',
					'marranni-delete/<str:pk>/',
	}

	return Response(api_urls)

@api_view(['GET'])
def BirthdayList(request):
	birthdays = Birthday.objects.all()
	serializer = BirthdaySerializer(birthdays, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def BirthdayDetail(request, pk):
	birthdays = Birthday.objects.get(id=pk)
	serializer = BirthdaySerializer(birthdays, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def BirthdayCreate(request):
	serializer = BirthdaySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def BirthdayUpdate(request, pk):
	birthday = Birthday.objects.get(id=pk)
	serializer = BirthdaySerializer(instance=birthday, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def BirthdayDelete(request, pk):
	birthday = Birthday.objects.get(id=pk)
	birthday.delete()

	return Response('item successfully deleted')


#MARRIAGEANNIVERSARY

@api_view(['GET'])
def MarriageAnniversaryList(request):
	marriage_anniversaries = MarriageAnniversary.objects.all()
	serializer = MarriageAnniversarySerializer(marriage_anniversaries, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def MarriageAnniversaryDetail(request, pk):
	marriage_anniversary = MarriageAnniversary.objects.get(id=pk)
	serializer = MarriageAnniversarySerializer(marriage_anniversaries, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def MarriageAnniversaryCreate(request):
	serializer = MarriageAnniversarySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def MarriageAnniversaryUpdate(request, pk):
	marriage_anniversary = MarriageAnniversary.objects.get(id=pk)
	serializer = MarriageAnniversarySerializer(instance=marriage_anniversary, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def MarriageAnniversaryDelete(request, pk):
	marriage_anniversary = MarriageAnniversary.objects.get(id=pk)
	marriage_anniversary.delete()

	return Response('item successfully deleted')





	#RELATIONSHIP ANNIVERSARY 

@api_view(['GET'])
def RelationshipAnniversaryList(request):
	relationship_anniversaries = RelationshipAnniversary.objects.all()
	serializer = RelationshipAnniversarySerializer(relationship_anniversaries, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def RelationshipAnniversaryDetail(request, pk):
	relationship_anniversary = RelationshipAnniversary.objects.get(id=pk)
	serializer = RelationshipAnniversarySerializer(relationship_anniversary, many=True)
	return Response(serializer.data)


@api_view(['POST'])
def RelationshipAnniversaryCreate(request):
	serializer = RelationshipAnniversarySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def RelationshipAnniversaryUpdate(request, pk):
	relationship_anniversary = RelationshipAnniversary.objects.get(id=pk)
	serializer = MarriageAnniversarySerializer(instance=relationship_anniversary, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def RelationshipAnniversaryDelete(request, pk):
	relationship_anniversary = RelationshipAnniversary.objects.get(id=pk)
	relationship_anniversary.delete()

	return Response('item successfully deleted')


#MOTHERS DAY

@api_view(['GET'])
def MothersDayList(request):
	mothersdays = MothersDay.objects.all()
	serializer = MothersDaySerializer(mothersdays, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def MothersDayDetail(request, pk):
	mothersdays = MothersDay.objects.get(id=pk)
	serializer = MothersDaySerializer(mothersdays, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def MothersDayCreate(request):
	serializer = MothersDaySerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['POST'])
def MothersDayUpdate(request, pk):
	mothersday = MothersDay.objects.get(id=pk)
	serializer = MothersDaySerializer(instance=mothersday, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def MothersDayDelete(request, pk):
	mothersday = MothersDay.objects.get(id=pk)
	mothersday.delete()

	return Response('item successfully deleted')