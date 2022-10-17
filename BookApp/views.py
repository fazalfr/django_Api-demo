from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BookApp.models import Users,Ebook
from BookApp.serializers import UserSerializer,EbookSerializer


# Create your views here.

@csrf_exempt
def userApi(request,id=0):
    if request.method=='GET':
        users = Users.objects.all()
        users_serializer=UserSerializer(users,many=True)
        return JsonResponse(users_serializer.data,safe=False)


    elif request.method=='POST':
        user_data=JSONParser().parse(request)
        users_serializer=UserSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)

    
    elif request.method=='PUT':
        user_data=JSONParser().parse(request)
        user=Users.objects.get(Username=user_data['Username'])
        users_serializer=UserSerializer(user,data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")


    elif request.method=='DELETE':
        user=Users.objects.get(Username=id)
        user.delete()
        return JsonResponse("Deleted Successfully",safe=False)



@csrf_exempt
def ebookApi(request,id=0):
    if request.method=='GET':
        ebooks = Ebook.objects.all()
        ebooks_serializer=EbookSerializer(ebooks,many=True)
        return JsonResponse(ebooks_serializer.data,safe=False)


    elif request.method=='POST':
        ebook_data=JSONParser().parse(request)
        ebooks_serializer=EbookSerializer(data=ebook_data)
        if ebooks_serializer.is_valid():
            ebooks_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)


    elif request.method=='PUT':
        ebook_data=JSONParser().parse(request)
        ebook=Ebook.objects.get(Title=ebook_data['Title'])
        ebooks_serializer=EbookSerializer(ebook,data=ebook_data)
        if ebooks_serializer.is_valid():
            ebooks_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")


    elif request.method=='DELETE':
        ebook=Ebook.objects.get(Title=id)
        ebook.delete()
        return JsonResponse("Deleted Successfully",safe=False)
 

 
# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from django.http.response import JsonResponse

# from BookApp.models import Users,Ebook
# from BookApp.serializers import EbookSerializer,UsersSerializer

# # Create your views here.

# @csrf_exempt
# def userApi(request,id=0):
#     if request.method=='GET':
#         users = Users.object.all()
#         users_Serializer=UsersSerializer(users,many=True)
#         return JsonResponse(users_Serializer.data,safe=False)

#     elif request.method=='POST':
#         users_data=JSONParser().parse(request)
#         users_Serializer=UsersSerializer(data=users_data)
#         if users_Serializer.is_valid():
#             users_Serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)

#     elif request.method=='PUT':
#         users_data=JSONParser().parse(request)
#         user=Users.objects.get(Username=users_data['Username'])
#         users_Serializer=UsersSerializer(user,data=users_data)
#         if users_Serializer.is_valid():
#             users_Serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update")


#     elif request.method=='DELETE':
#         user=Users.objects.get(Username=id)
#         user.delete()
#         return JsonResponse("Deleted Successfullly",safe=False)

    

# @csrf_exempt
# def ebookApi(request,id=0):
#     if request.method=='GET':
#         ebook = Ebook.object.all()
#         ebook_Serializer=EbookSerializer(ebook,many=True)
#         return JsonResponse(ebook_Serializer.data,safe=False)

#     elif request.method=='POST':
#         ebook_data=JSONParser().parse(request)
#         ebook_Serializer=EbookSerializer(data=ebook_data)
#         if ebook_Serializer.is_valid():
#             ebook_Serializer.save()
#             return JsonResponse("Added Successfully",safe=False)
#         return JsonResponse("Failed to Add",safe=False)

#     elif request.method=='PUT':
#         ebook_data=JSONParser().parse(request)
#         ebook=Ebook.objects.get(Title=ebook_data['Title'])
#         ebook_Serializer=EbookSerializer(Ebook,data=ebook_data)
#         if ebook_Serializer.is_valid():
#             ebook_Serializer.save()
#             return JsonResponse("Updated Successfully",safe=False)
#         return JsonResponse("Failed to Update")


#     elif request.method=='DELETE':
#         ebook=Ebook.objects.get(Title=id)
#         ebook.delete()
#         return JsonResponse("Deleted Successfullly",safe=False)

    



