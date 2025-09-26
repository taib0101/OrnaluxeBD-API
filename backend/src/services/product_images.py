from rest_framework.response import Response
from json import loads

from src.repositories import product_repos, product_image_repos, ProductImageRepo
from src.schemas import ProductImageIn, ProductImageUpdate, ProductImageOut, ProductImageTotalOut, input_validation, output_validation


class ProdcutImageService:

    def __init__(self, repo: ProductImageRepo):
        self.repo = repo

    
    def create_product_image_base(self, request):
        requested_body = loads(request.body)

        data_in = input_validation(SchemaName=ProductImageIn, data_in=requested_body)

        product_id = {
            "product_id": data_in['product_id']
        }
        category_data = product_repos.read_product_query(query_data=product_id)

        product_image_data = self.repo.create(ModelName="ProductImage", data_in=data_in, temp_write="no")
        product_image_data['product_id'] = product_image_data.pop('product')

        product_image_data = output_validation(SchemaName=ProductImageOut, data_out=product_image_data)

        return Response(data=product_image_data, status=200)
    

    def read_product_image_all_base(self, request):
        data = self.repo.read_all(ModelName="ProductImage")
        data = output_validation(SchemaName=ProductImageTotalOut, data_out=data)

        return Response(data=data, status=200)
    

    def read_product_image_query_base(self, request):
        query_data = request.GET.dict()
        
        data = self.repo.read_product_image_query(query_data=query_data)
        data = output_validation(SchemaName=ProductImageTotalOut, data_out=data)

        return Response(data=data, status=200)
    

    def update_product_image_base(self, request):
        requested_body = loads(request.body)
        
        data_update = input_validation(SchemaName=ProductImageUpdate, data_in=requested_body)

        query_data = request.GET.dict()

        data = self.repo.update(ModelName="ProductImage", query_data=query_data, data_update=data_update, temp_write="no")
        data = output_validation(SchemaName=ProductImageTotalOut, data_out=data)

        return Response(data=data, status=200)
    

    def delete_product_image_base(self, request):
        query_data = request.GET.dict()

        data = self.repo.delete(ModelName="ProductImage", query_data=query_data, temp_write="no")

        return Response(data=data, status=200)

product_image_services = ProdcutImageService(repo=product_image_repos)