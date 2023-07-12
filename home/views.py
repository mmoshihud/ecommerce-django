from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


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
        HttpResponse('404 Not Found')


def handleLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

    try:
        user = User.objects.get(username=username)
        if user.check_password(password):
            # Password is correct
            # Perform any additional actions if needed
            return HttpResponse('User exists and password is correct!')
        else:
            # Password is incorrect
            # Perform any additional actions if needed
            return HttpResponse('Invalid login credentials!')
    except User.DoesNotExist:
        # User does not exist
        # Perform any additional actions if needed
        return HttpResponse('Invalid login credentials!')
