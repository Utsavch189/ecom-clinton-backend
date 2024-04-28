from utils.responses.main import Response
from rest_framework import status
from utils.exceptions import main
import json,jsonschema
from utils.responses.main import Response
from rest_framework import status
from django.http import JsonResponse

class SchemaValidate:

    def __init__(self,request_data:dict,json_file:str) -> None:
        self.request_data=request_data
        self.json_file=json_file
    
    def __get_schema(self):
        try:
            with open(self.json_file, 'r') as file:
                schema = json.load(file)
            return schema
        except Exception as e:
            raise Exception(str(e))
    
    def validate(self)->bool:
        try:
            execute_api_schema = self.__get_schema()
            try:
                jsonschema.validate(instance=self.request_data, schema=execute_api_schema)
            except jsonschema.exceptions.ValidationError as err:
                error_string = {"message": err.message,
                                    "payload": err.instance,
                                    "expected": err.schema
                                }
                return False,error_string
            except Exception as e:
                return False,error_string
            return True,None
        except Exception as e:
            raise Exception(str(e))

def schema_validate(schema_name:str):
    def inner(func):
        def wrapper(*args, **kwargs):
            validation=SchemaValidate(request_data=args[0].data,json_file=schema_name)
            validate=validation.validate()  
            error=validate[1]
            is_valid=validate[0]
            if is_valid:    
                return func(*args, **kwargs)
            else:
                print('yessss')
                raise main.Unprocessable(detail=str(error))
        return wrapper
    return inner