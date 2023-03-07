# -*- coding: utf-8 -*-
import datetime
from rest_framework.response import Response
from rest_framework.views import APIView

class HealthCheckView(APIView):

    def get(self, request):
        return Response(status=200, data={"ok"})
