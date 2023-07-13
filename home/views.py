from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
import jwt
import os
from home.middleware import JwtMiddleware
secret = os.getenv('ACCESS_TOKEN_SECRET')


def handleSignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()
        return JsonResponse({'message': 'User created successfully'})
    else:
        return HttpResponse('404 Not Found', status=404)


def handleLogin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

    try:
        user = User.objects.get(email=email)
        if user.check_password(password):
            print(secret)
            token = jwt.encode({email: email}, secret, algorithm="HS256")
            # Password is correct
            # Perform any additional actions if needed
            print(token)
            return HttpResponse({token, 'User exists and password is correct!'})
        else:
            # Password is incorrect
            # Perform any additional actions if needed
            return HttpResponse('Invalid login credentials!')
    except User.DoesNotExist:
        # User does not exist
        # Perform any additional actions if needed
        return HttpResponse('Invalid login credentials!')


@JwtMiddleware
def test(request):
    data = {'message': 'JWT middleware working'}
    return JsonResponse(data, safe=False)
