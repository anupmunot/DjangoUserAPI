# -*- coding: utf-8 -*-
import datetime
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import json

class APIHealthCheckView(APIView):

    def get(self, request):
        # GET API call
        # Debug statement using 
        # import pdb;pdb.set_trace()
        # define header key,value and pass to method as below
        
        app_headers = {'Authorization' : 'Bearer testkoen123'}
        response = requests.get("http://api.open-notify.org/astros.json", headers=app_headers)
        if (response.status_code == 200):
                return Response(status=200, data=response.json())
        return Response(status=response.status_code,data={"Error occured for GET API call."})

    def post(self, request):
        # POST API call
        response = requests.post('https://httpbin.org/post', data = {'key':settings.APP_NAME})
        return Response(status=200, data={response})
    
    def get_extra_actions():
        return[]
