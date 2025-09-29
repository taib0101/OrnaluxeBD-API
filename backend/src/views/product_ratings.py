from rest_framework.views import APIView

from src.middleware import LoggedInAdmin
from src.schemas import ProductRatingIn, ProductRatingUpdate, ProductRatingOut, ProductRatingTotalOut, ProductRatingDelete
from src.docs import create_product_rating, read_product_rating_all, read_product_rating_query, update_product_rating, delete_product_rating
from src.services import product_rating_services


class ProductRatingCreate(APIView):

    authentication_classes = [LoggedInAdmin]

    @create_product_rating(request=ProductRatingIn, responses=ProductRatingOut)
    def post(self, request):
        data = product_rating_services.create_product_rating(request=request)
        return data


class ProductRatingAll(APIView):

    authentication_classes = [LoggedInAdmin]

    @read_product_rating_all(request=None, responses=ProductRatingTotalOut)
    def get(self, request):
        data = product_rating_services.read_product_rating_all(request=request)
        return data


class ProductRatingRead(APIView):

    authentication_classes = [LoggedInAdmin]

    @read_product_rating_query(request=None, responses=ProductRatingTotalOut)
    def get(self, request):
        data = product_rating_services.read_product_rating_query(request=request)
        return data
    

class ProductRatingUpdate(APIView):

    authentication_classes = [LoggedInAdmin]

    @update_product_rating(request=ProductRatingUpdate, responses=ProductRatingTotalOut)
    def post(self, request):
        data = product_rating_services.update_product_rating(request=request)
        return data
    

class ProductRatingDelete(APIView):

    authentication_classes = [LoggedInAdmin]

    @delete_product_rating(request=None, responses=ProductRatingDelete)
    def get(self, request):
        data = product_rating_services.delete_product_rating(request=request)
        return data