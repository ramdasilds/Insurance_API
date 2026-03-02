from django.http import HttpResponse
from django.shortcuts import render

from api.serializers import InsuranceSerializer
from api.models import Insurance
from rest_framework import viewsets

# Create your views here.
def home(k):
    return HttpResponse("this is home page")

def about(request):
    return render(request,'index.html')

class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializer
