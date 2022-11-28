from .models import Demo
from django.http import JsonResponse
from django.db import transaction

"""Create two functions which will be used in transaction"""

def first_insert():
    Demo.objects.create()
    raise Exception("Something went wrong")

def second_insert():
    Demo.objects.create()

"""Creating transactions"""    

"""Using 'ATOMIC_REQUESTS': True in db settings"""
"""In case of exception - we use middleware to recieve JSON response with error"""
def home(request):

    first_insert()
    second_insert()

    return JsonResponse({"success": True})


"""
Issue when we make error handling inside view,
transaction logic doesn't work
we will get new record in db
"""
# def home(request):
#     try:
#         first_insert()
#         second_insert()

#         return JsonResponse({"success": True})

#     except Exception as e:
#         return JsonResponse({"success": False, "error": str(e)})

"""Using transaction.atomic decorator"""
# @transaction.atomic
# def home(request):
#     first_insert()
#     second_insert()

#     return HttpResponse("OK!")

"""Using with transaction.atomic"""
# def home(request):
#     with transaction.atomic:
#         first_insert()
#         second_insert()

#     return HttpResponse("OK!")
