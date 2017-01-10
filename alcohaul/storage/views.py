from django.shortcuts import get_object_or_404 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import alcohol
from .serializers import alcoholSerializer



# List all booze or create a new one
# alcohol/
def index(request):
	return HttpResponse("<h1>This is the alchohaul app homepage</h1>")


class alcoholList(APIView):

	def get(self, request):
		Alcohol = alcohol.objects.all()
		serializers = alcoholSerializer(Alcohol, many=True)
		return Response(serializers.data)

	def post(self):
		pass













