from django.urls import path
from .views import UserList, CreateNewUser, UpdateExistingUser, UpdateDetail, DeleteUser

urlpatterns = [
    path('listusers/', UserList.as_view(), name='user-list'),
    path('createnewuser/', CreateNewUser.as_view(), name='create-new-user'),
    path('updateexistinguser/<str:email>/', UpdateExistingUser.as_view(), name='update-existing-user'),
    path('updatedetails/<str:email>/', UpdateDetail.as_view(), name='update-details'),
    path('deleteuser/<str:email>/', DeleteUser.as_view(), name='delete-user-by-email')
]
