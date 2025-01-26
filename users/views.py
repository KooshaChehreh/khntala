from .models import User
from elasticsearch_dsl.search_base import AggsProxy
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from .serializer import UsersSerializer
from exceptions import *
from jwt_auth import generate_access_token
from rest_framework.response import Response
from rest_framework import status, filters
from django.http import HttpResponse
import csv
from .permissions import IsAuthenticatedWithToken
from .models import User
from rest_framework.views import APIView
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
    OrderingFilterBackend,
)
        
@api_view(["POST"])
def create_user(request):
    serializer = UsersSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data["username"]
    if User.objects.filter(username=username).exists():
        raise UsernameAlreadyExists
    
    created_user = serializer.save()
    return Response(UsersSerializer(created_user).data, status=status.HTTP_201_CREATED)

@api_view(["POST"])
def login_verify_password(request):
    serializer = UsersSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data["username"]
    password = serializer.validated_data["password"]
    try:
        target_user: User = User.objects.get(username=username)
        if target_user.is_suspended():
            raise AccountSuspended
        if not target_user.check_password(entered_password=password):
            raise InvalidUsernameOrPassword
        access_token = generate_access_token(target_user)
        response_data = {
            "access_token": access_token,
        }
        return Response(response_data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        raise InvalidUsernameOrPassword
    
@api_view(["GET"])
@permission_classes([IsAuthenticatedWithToken])
def export_csv(request):
    queryset = User.objects.all()
    serializer = UsersSerializer(queryset, many=True)
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="insurances.csv"'
    writer = csv.writer(response)

    if serializer.data:
        headers = serializer.data[0].keys()  
        writer.writerow(headers)
        for item in serializer.data:
            writer.writerow(item.values())
    return response

@api_view(["GET"])
@permission_classes([IsAuthenticatedWithToken])
def records_number(request):
    queryset = User.objects.all().count()
    User.objects.filter(phone="").update(phone="09356195525")
    return Response({"Number of Records:": queryset}, status=status.HTTP_200_OK)


