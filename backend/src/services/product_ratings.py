from rest_framework.response import Response
from json import loads

from src.repositories import product_repos, product_rating_repos, ProductRatingRepo
from src.schemas import ProductRatingIn, ProductRatingUpdate, ProductRatingOut, ProductRatingTotalOut, input_validation, output_validation


class ProductRatingService:

    def __init__(self, repo: ProductRatingRepo):
        self.repo = repo


    def create_product_rating(self, request):
        requested_body = loads(request.body)

        data_in = input_validation(SchemaName=ProductRatingIn, data_in=requested_body)

        product_id = {
            "product_id": data_in['product_id']
        }
        product_data = product_repos.read_product_query(query_data=product_id)

        product_rating_data = self.repo.create(ModelName="Rating", data_in=data_in, temp_write="no")
        product_rating_data['product_id'] = product_rating_data.pop('product')

        product_rating_data = output_validation(SchemaName=ProductRatingOut, data_out=product_rating_data)

        return Response(data=product_rating_data, status=200)
    

    def read_product_rating_all(self, request):
        data = self.repo.read_all(ModelName="Rating")
        data = output_validation(SchemaName=ProductRatingTotalOut, data_out=data)

        return Response(data=data, status=200)
    

    def read_product_rating_query(self, request):
        query_data = request.GET.dict()
        
        data = self.repo.read_product_rating_query(query_data=query_data)
        data = output_validation(SchemaName=ProductRatingTotalOut, data_out=data)

        return Response(data=data, status=200)
    
    
    def update_product_rating(self, request):
        requested_body = loads(request.body)
        
        data_update = input_validation(SchemaName=ProductRatingUpdate, data_in=requested_body)

        query_data = request.GET.dict()

        data = self.repo.update(ModelName="Rating", query_data=query_data, data_update=data_update, temp_write="no")
        data = output_validation(SchemaName=ProductRatingTotalOut, data_out=data)

        return Response(data=data, status=200)
    
   
    def delete_product_rating(self, request):
        query_data = request.GET.dict()

        data = self.repo.delete(ModelName="Rating", query_data=query_data, temp_write="no")

        return Response(data=data, status=200)

product_rating_services = ProductRatingService(repo=product_rating_repos)