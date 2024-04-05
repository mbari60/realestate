# views.py
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        if not username or not password:
            return JsonResponse({'error': 'Both username and password are required'}, status=400)
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)
        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({'message': 'User created successfully', 'success': True}, status=201)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful', 'success': True}, status=200)
        else:
            return JsonResponse({'error': 'Invalid username or password'}, status=401)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Logged out successfully', 'success': True}, status=200)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
