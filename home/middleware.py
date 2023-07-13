import jwt
import os
from django.http import HttpResponse


class JwtMiddleware:
    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        authorization = request.headers.get('Authorization')
        if not authorization:
            return HttpResponse('Unauthorized access', status=401)

        token = authorization.split(' ')[1]
        print(token)
        try:
            decoded = jwt.decode(
                token, os.getenv('ACCESS_TOKEN_SECRET'), algorithms="HS256")

            request.decoded = decoded

        except jwt.exceptions.DecodeError:
            return HttpResponse('Unauthorized access', status=401)

        response = self.get_response(request)

        return response
