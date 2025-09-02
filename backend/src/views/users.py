from rest_framework.views import APIView

<<<<<<< HEAD
from src.schemas import UserIn, UserOut, UserTotalOut, UserUpdate, UserDelete
from src.middleware import LoggedInAdmin
from src.docs import create_user, read_user_query, read_user_all, delete_user
=======
from src.docs import create_user, read_user_all, read_user_query, update_user, delete_user
from src.schemas import UserIn, UserOut, UserTotalOut, UserUpdate, UserDelete
from src.middleware import LoggedInAdmin
>>>>>>> master
from src.services import user_services

class UserCreate(APIView):

    authentication_classes = [LoggedInAdmin]

    @create_user(request=UserIn, responses=UserOut)
    def post(self, request):
        if request.method == "POST":
            data = user_services.create_user(request=request)

        return data
    

class UserRead(APIView):

    authentication_classes = [LoggedInAdmin]

    @read_user_query(request=None, responses=UserTotalOut)
    def get(self, request):
        if request.method == "GET":
            data = user_services.read_user_query(request=request)

        return data
<<<<<<< HEAD
    
=======

>>>>>>> master
class UserReadAll(APIView):

    authentication_classes = [LoggedInAdmin]

    @read_user_all(request=None, responses=UserTotalOut)
    def get(self, request):
        if request.method == "GET":
            data = user_services.read_user_all(request=request)

        return data

class UserUpdate(APIView):

    authentication_classes = [LoggedInAdmin]

<<<<<<< HEAD
    @delete_user(request=UserUpdate, responses=UserTotalOut)
=======
    @update_user(request=UserUpdate, responses=UserTotalOut)
>>>>>>> master
    def post(self, request):
        if request.method == "POST":
            data = user_services.update_user(request=request)

        return data
<<<<<<< HEAD
    
=======
>>>>>>> master

class UserDelete(APIView):

    authentication_classes = [LoggedInAdmin]

    @delete_user(request=None, responses=UserDelete)
    def get(self, request):
        if request.method == "GET":
            data = user_services.delete_user(request=request)

<<<<<<< HEAD
        return data
    
=======
        return data
>>>>>>> master
