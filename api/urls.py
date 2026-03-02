
from .views import home
from django.urls import include,path
from rest_framework import routers
from api.views import InsuranceViewSet

router = routers.DefaultRouter()
router.register(r"insurance", InsuranceViewSet)

urlpatterns = [
    path('index/',home,name='home'),
    path('',include(router.urls))
]

