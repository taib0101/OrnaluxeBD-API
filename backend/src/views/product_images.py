from rest_framework.views import APIView

from src.docs import create_product_image_base, read_product_image_all_base, read_product_image_base, update_product_image_base, delete_product_image_base
from src.schemas import ProductImageIn, ProductImageUpdate, ProductImageOut, ProductImageTotalOut, ProductImageDelete
from src.middleware import LoggedInAdmin
from src.services import product_image_services


class ProductImageCreateBase(APIView):

    authentication_classes = [LoggedInAdmin]

    @create_product_image_base(request=ProductImageIn, responses=ProductImageOut)
    def post(self, request):
        data = product_image_services.create_product_image_base(request=request)
        return data
    

class ProductImageReadAllBase(APIView):

    authentication_classes = [LoggedInAdmin]

    @read_product_image_all_base(request=None, responses=ProductImageTotalOut)
    def get(self, request):
        data = product_image_services.read_product_image_all_base(request=request)
        return data
    

class ProductImageReadBase(APIView):

    authentication_classes = [LoggedInAdmin]

    @read_product_image_base(request=None, responses=ProductImageTotalOut)
    def get(self, request):
        data = product_image_services.read_product_image_query_base(request=request)
        return data
    

class ProductImageUpdateBase(APIView):

    authentication_classes = [LoggedInAdmin]

    @update_product_image_base(request=ProductImageUpdate, responses=ProductImageOut)
    def post(self, request):
        data = product_image_services.update_product_image_base(request=request)
        return data
    

class ProductImageDeleteBase(APIView):

    authentication_classes = [LoggedInAdmin]

    @delete_product_image_base(request=None, responses=ProductImageDelete)
    def get(self, request):
        data = product_image_services.delete_product_image_base(request=request)
        return data