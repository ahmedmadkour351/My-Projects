from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.


def index(request):

    return render(request, 'pages/index.html')


# 1 without Rest and no model query
def no_rest_no_model(request):
    guests = [
        {
            'id': 1,
            'Name': 'madkour',
            'mobile': 1004582452,
        },
        {
            'id': 2,
            'name': 'drenn',
            'mobile': 774552,
        }
    ]
    return JsonResponse(guests, safe=False)
