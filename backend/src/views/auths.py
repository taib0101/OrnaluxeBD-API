from rest_framework.views import APIView

<<<<<<< HEAD
from src.schemas import AuthLogIn, AuthTokenOut
from src.docs import login, auth_check
from src.middleware import LoggedInAdmin
from src.services import auth_services
=======
from src.schemas import AuthLogIn, AuthTokenOut, UserOut
from src.middleware import LoggedInAdmin
from src.services import auth_services
from src.docs import login, auth_check
>>>>>>> master

class Login(APIView):

    authentication_classes = []

    @login(request=AuthLogIn, responses=AuthTokenOut)
    def post(self, request):
        if request.method == "POST":
            data = auth_services.login(request=request)

        return data
<<<<<<< HEAD
    
=======

>>>>>>> master

class Auth(APIView):

    authentication_classes = [LoggedInAdmin]

<<<<<<< HEAD
    @auth_check(request=None, responses=AuthTokenOut)
=======
    @auth_check(request=None, responses=UserOut)
>>>>>>> master
    def get(self, request):
        if request.method == "GET":
            data = auth_services.auth_check(request=request)

        return data
<<<<<<< HEAD

=======
>>>>>>> master
