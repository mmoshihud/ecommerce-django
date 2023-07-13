from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponseNotFound
from django.middleware.csrf import get_token
from home.middleware import JwtMiddleware
import json
import jwt
import os


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


def handleSignup(request):
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))

        username = json_data.get('username')
        email = json_data.get('email')
        password = json_data.get('password')

        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        return JsonResponse({'message': 'User created successfully'})

    else:
        return HttpResponseNotFound("<h1>Page not found</h1>")


def handleLogin(request):
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))

        email = json_data.get('email')
        password = json_data.get('password')

        try:
            user = User.objects.get(email=email)

            if user.check_password(password):
                token = jwt.encode(
                    {email: email}, os.getenv('ACCESS_TOKEN_SECRET'), algorithm="HS256")
                print(token)
                response_data = {
                    'token': token,  # No need to decode here
                    'message': 'User exists and password is correct!'
                }
                return JsonResponse(response_data)

            else:
                response_data = {
                    'message': 'Invalid login credentials!'
                }
                return JsonResponse(response_data)

        except User.DoesNotExist:
            response_data = {
                'message': 'Invalid login credentials!'
            }
            return JsonResponse(response_data)
    else:
        response_data = {
            'message': 'Invalid request method!'
        }
        return HttpResponseNotFound("<h1>Page not found</h1>")


@JwtMiddleware
def test(request):
    data = {'message': 'JWT middleware working'}
    return JsonResponse(data, safe=False)
