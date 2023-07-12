from django.http import JsonResponse, HttpResponse
from django.contrib.auth.models import User


def handleSignup(request):
    if request.method == 'POST':
        user_data = request.POST
        print(user_data)

        user = User.objects.create_user(
            username=user_data['username'], email=user_data['email'], password=user_data['password'])
        user.save()
        return JsonResponse({'message': 'User created successfully'})
    else:
        HttpResponse('404 Not Found')
