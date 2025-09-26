from rest_framework.views import APIView

from src.docs import create_product_base, read_product_all_base, read_product_base, update_product_base, delete_product_base
from src.schemas import ProductIn, ProductUpdate, ProductOut, ProductTotalOut, ProductDelete
from src.middleware import LoggedInAdmin
from src.services import product_services

class ProductCreateBase(APIView):

    authentication_classes = [LoggedInAdmin]

    @create_product_base(request=ProductIn, responses=ProductOut)
    def post(self, request):
        data = product_services.create_product_base(request=request)
        return data


class ProductReadAllBase(APIView):

    authentication_classes = [LoggedInAdmin]

    @read_product_all_base(request=None, responses=ProductTotalOut)
    def get(self, request):
        data = product_services.read_product_all_base(request=request)
        return data


class ProductReadBase(APIView):

    authentication_classes = [LoggedInAdmin]

    @read_product_base(request=None, responses=ProductTotalOut)
    def get(self, request):
        data = product_services.read_product_query_base(request=request)
        return data
    

class ProductUpdateBase(APIView):

    authentication_classes = [LoggedInAdmin]

    @update_product_base(request=ProductUpdate, responses=ProductTotalOut)
    def post(self, request):
        data = product_services.update_product_base(request=request)
        return data
    

class ProductDeleteBase(APIView):

    authentication_classes = [LoggedInAdmin]

    @delete_product_base(request=None, responses=ProductDelete)
    def get(self, request):
        data = product_services.delete_product_base(request=request)
        return data