from rest_framework.views import APIView


from src.docs import create_user, read_user_all, read_user_query, update_user, delete_user
from src.schemas import UserIn, UserOut, UserTotalOut, UserUpdate, UserDelete
from src.middleware import LoggedInAdmin
from src.services import user_services

class UserCreate(APIView):

    authentication_classes = [LoggedInAdmin]

    @create_user(request=UserIn, responses=UserOut)
    def post(self, request):
        data = user_services.create_user(request=request)
        return data
    

class UserRead(APIView):

    authentication_classes = [LoggedInAdmin]

    @read_user_query(request=None, responses=UserTotalOut)
    def get(self, request):
        data = user_services.read_user_query(request=request)
        return data
class UserReadAll(APIView):

    authentication_classes = [LoggedInAdmin]

    @read_user_all(request=None, responses=UserTotalOut)
    def get(self, request):
        data = user_services.read_user_all(request=request)
        return data

class UserUpdate(APIView):

    authentication_classes = [LoggedInAdmin]

    @update_user(request=UserUpdate, responses=UserTotalOut)
    def post(self, request):
        data = user_services.update_user(request=request)
        return data

class UserDelete(APIView):

    authentication_classes = [LoggedInAdmin]

    @delete_user(request=None, responses=UserDelete)
    def get(self, request):
        data = user_services.delete_user(request=request)
        return data
