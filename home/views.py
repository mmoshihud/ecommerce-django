from django.http import JsonResponse


def index(request):
    data = [
        {
            "name": "John Doe",
            "age": 30,
            "profession": "Web Developer"
        },
        {
            "name": "Jane Smith",
            "age": 35,
            "profession": "Graphic Designer"
        },
        {
            "name": "Mike Johnson",
            "age": 25,
            "profession": "Software Engineer"
        }
    ]

    return JsonResponse(data, safe=False)
