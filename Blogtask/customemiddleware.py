
import json
from django.http import HttpResponse
from http import HTTPStatus
class MessageMiddleware():

    def __init__(self,get_response):
        self.get_response=get_response
        print('one time intial')

    def __call__(self,request,*args, **kwargs):

        print('this is before view')
        response=self.get_response(request)
        print('this is after view')
        status_code=response.status_code
        status_message = HTTPStatus(status_code).phrase
        try:
            print(response.data)
            response_content={
                "msg":status_message,
                "error":response.data['error'],
                "data":response.data['data'],
                "status_code":status_code
            }
            response=HttpResponse(json.dumps(response_content),content_type='application/json')
        except:
            pass
        # response={'data':response.data,'msg':status_message,'status_code':status_code}
        return response
