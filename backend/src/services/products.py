from rest_framework.response import Response
from json import loads

from src.repositories import category_repos, product_repos, ProductRepo
from src.schemas import ProductIn, ProductUpdate, ProductOut, ProductTotalOut, input_validation, output_validation

class ProductService:

    def __init__(self, repo: ProductRepo):
        self.repo = repo

    def create_product_base(self, request):
        requested_body = loads(request.body)

        data_in = input_validation(SchemaName=ProductIn, data_in=requested_body)

        category_id = {
            "category_id": data_in['category_id']
        }
        category_data = category_repos.read_category_query(query_data=category_id)

        product_data = self.repo.create(ModelName="Product", data_in=data_in, temp_write="no")
        product_data['category_id'] = product_data['category']

        product_data = output_validation(SchemaName=ProductOut, data_out=product_data)

        return Response(data=product_data, status=200)
    
    def read_product_all_base(self, request):
        data = self.repo.read_all(ModelName="Product")
        data = output_validation(SchemaName=ProductTotalOut, data_out=data)

        return Response(data=data, status=200)
    
    def read_product_query_base(self, request):
        query_data = request.GET.dict()
        
        data = self.repo.read_user_query(query_data=query_data)
        data = output_validation(SchemaName=ProductTotalOut, data_out=data)

        return Response(data=data, status=200)

    def update_product_base(self, request):
        requested_body = loads(request.body)
        
        data_update = input_validation(SchemaName=ProductUpdate, data_in=requested_body)

        query_data = request.GET.dict()

        data = self.repo.update(ModelName="Product", query_data=query_data, data_update=data_update, temp_write="no")
        data = output_validation(SchemaName=ProductTotalOut, data_out=data)

        return Response(data, status=200)
    
    def delete_product(self, request):
        query_data = request.GET.dict()

        data = self.repo.delete(ModelName="Product", query_data=query_data, temp_write="no")

        return Response(data, status=200)


product_services = ProductService(repo=product_repos)