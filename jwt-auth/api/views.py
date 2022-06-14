from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.authentication import JWTAuthentication


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = [StudentSerializer]
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
