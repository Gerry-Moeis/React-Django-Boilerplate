from rest_framework.decorators import api_view
from rest_framework.response import Response

from boilerplate.models import *
from .serializers import *

@api_view()
def getAPIUrl(request):
    urls = {
        'getAPIUrl': '/'
    }

    return Response(urls)