from rest_framework.response import Response
from json import loads

from src.repositories import category_repos, CategoryRepo
from src.schemas import CategoryIn, CategoryUpdate, CategoryOut, CategoryTotalOut, input_validation, output_validation

class CategoryService:

    def __init__(self, repo: CategoryRepo):
        self.repo = repo

    def category_create(self, request):
        requested_body = loads(request.body)

        data_in = input_validation(SchemaName=CategoryIn, data_in=requested_body)

        data = self.repo.create(ModelName="Category", data_in=data_in, temp_write="no")
        data = output_validation(SchemaName=CategoryOut, data_out=data)

        return Response(data, status=200)
    
    def read_category_all(self, request):
        data = self.repo.read_all(ModelName="Category")
        data = output_validation(SchemaName=CategoryTotalOut, data_out=data)

        return Response(data, status=200)

    def read_category_query(self, request):
        query_data = request.GET.dict()

        data = self.repo.read_category_query(query_data=query_data) 
        data = output_validation(SchemaName=CategoryTotalOut, data_out=data)

        return Response(data, status=200)
    
    def update_category(self, request):
        requested_body = loads(request.body)
        
        data_update = input_validation(SchemaName=CategoryUpdate, data_in=requested_body)

        query_data = request.GET.dict()

        data = self.repo.update(ModelName="Category", query_data=query_data, data_update=data_update, temp_write="no")
        data = output_validation(SchemaName=CategoryTotalOut, data_out=data)

        return Response(data, status=200)
    
    def delete_category(self, request):
        query_data = request.GET.dict()

        data = self.repo.delete(ModelName="Category", query_data=query_data, temp_write="no")

        return Response(data, status=200)
    

category_services = CategoryService(repo=category_repos)