from rest_framework.views import APIView

from src.middleware import LoggedInAdmin
from src.docs import create_category, read_category_query, read_category_all, update_category, delete_category
from src.schemas import CategoryIn, CategoryUpdate, CategoryOut, CategoryTotalOut, CategoryDelete
from src.services import category_services


class CategoryCreate(APIView):

    authentication_classes = [LoggedInAdmin]

    @create_category(request=CategoryIn, responses=CategoryOut)
    def post(self, request):
        if request.method == "POST":
            data = category_services.category_create(request=request)

        return data
    

class CategoryRead(APIView):

    authentication_classes = [LoggedInAdmin]

    @read_category_query(request=None, responses=CategoryTotalOut)
    def get(self, request):
        if request.method == "GET":
            data = category_services.read_category_query(request=request)

        return data
    
class CategoryReadAll(APIView):

    authentication_classes = [LoggedInAdmin]

    @read_category_all(request=None, responses=CategoryTotalOut)
    def get(self, request):
        if request.method == "GET":
            data = category_services.read_category_all(request=request)

        return data
    
class CategoryUpdate(APIView):

    authentication_classes = [LoggedInAdmin]

    @update_category(request=CategoryUpdate, responses=CategoryOut)
    def post(self, request):
        if request.method == "POST":
            data = category_services.update_category(request=request)

        return data
    
class CategoryDelete(APIView):

    authentication_classes = [LoggedInAdmin]

    @delete_category(request=None, responses=CategoryDelete)
    def get(self, request):
        if request.method == "GET":
            data = category_services.delete_category(request=request)

        return data

