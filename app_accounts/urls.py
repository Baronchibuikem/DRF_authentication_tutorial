from django.urls import path
# from rest_framework_simplejwt.views import TokenRefreshView
from app_accounts.views import GetAllUser, GetAllHRTeamMember, LoginView, SignUpView


urlpatterns = [
    path('users/', GetAllUser.as_view(), name="users"),
    path("hr-team-list/", GetAllHRTeamMember.as_view(), name="hr-list"),
    path('login/', LoginView.as_view(), name="log_in"),
    path('register/', SignUpView.as_view(), name="signup"),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    # path('users/', UsersListView.as_view(), name="users"),
    # path("all-riders/", GetAllRidersView.as_view(), name="all-riders"),
    # path("all-drivers/", GetAllDriversView.as_view(), name="all-drivers"),
    # path("user/<int:pk>/", GetUserById.as_view(), name="user")
]
