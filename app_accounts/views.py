from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from app_accounts.models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from app_accounts.serializers import UserSerializer, LoginSerializer, RegisterSerializer


class GetAllUser(generics.ListAPIView):
    """
    This access point will return all user's in the database for you
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class GetAllHRTeamMember(generics.ListAPIView):
    """
    This access point will return all Human Resource Team members registered on the platform
    """
    serializer_class = UserSerializer

    def get_queryset(self):
        all_hr_team_members = CustomUser.objects.filter(
            role__name="Design Team")
        return all_hr_team_members


class LoginView(TokenObtainPairView):
    """
    User Login view
    """
    serializer_class = LoginSerializer


class SignUpView(generics.CreateAPIView):
    """
    User Signup view
    """
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
