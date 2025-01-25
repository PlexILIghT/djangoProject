from django.shortcuts import render

import json
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()

def is_admin(user):
    return user.is_superuser

def error_response(message, status=400):
    return JsonResponse({'error': message}, status=status)

@user_passes_test(is_admin)
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all().values('id', 'username', 'email', 'is_active')
        return JsonResponse(list(users), safe=False)
    else:
        return error_response('Method not allowed', status=405)

@user_passes_test(is_admin)
def user_detail(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    if request.method == 'GET':
        return JsonResponse({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_active': user.is_active
        })
    else:
        return error_response('Method not allowed', status=405)

@csrf_exempt
@user_passes_test(is_admin)
def user_create(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # есть ли все обязательные поля
            if not all(key in data for key in ('username', 'email', 'password')):
                return error_response('Missing required fields', status=400)
            
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
            return JsonResponse({'id': user.id, 'message': 'User created successfully'}, status=201)
        except json.JSONDecodeError:
            return error_response('Invalid JSON format', status=400)
    else:
        return error_response('Method not allowed', status=405)

@csrf_exempt
@user_passes_test(is_admin)
def user_update(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            user.username = data.get('username', user.username)
            user.email = data.get('email', user.email)
            user.is_active = data.get('is_active', user.is_active)
            user.save()
            return JsonResponse({'message': 'User updated successfully'})
        except json.JSONDecodeError:
            return error_response('Invalid JSON format', status=400)
    else:
        return error_response('Method not allowed', status=405)

@csrf_exempt
@user_passes_test(is_admin)
def user_delete(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return error_response('User not found', status=404)

    if request.method == 'DELETE':
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'}, status=204)
    else:
        return error_response('Method not allowed', status=405)
