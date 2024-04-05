# views.py
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AppartmentBookingModel, AirbnbBookingModel
from .serializers import AppartmentBookingSerializer, AirbnbBookingSerializer

@csrf_exempt
def appartment_bookings(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                booking = AppartmentBookingModel.objects.get(pk=id)
                serializer = AppartmentBookingSerializer(booking)
                return JsonResponse(serializer.data)
            except AppartmentBookingModel.DoesNotExist:
                return JsonResponse({'error': 'Booking not found'}, status=404)
        else:
            bookings = AppartmentBookingModel.objects.all()
            serializer = AppartmentBookingSerializer(bookings, many=True)
            return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = AppartmentBookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT' or request.method == 'PATCH':
        data = json.loads(request.body)
        try:
            booking = AppartmentBookingModel.objects.get(pk=id)
        except AppartmentBookingModel.DoesNotExist:
            return JsonResponse({'error': 'Booking not found'}, status=404)
        serializer = AppartmentBookingSerializer(booking, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            booking = AppartmentBookingModel.objects.get(pk=id)
            booking.delete()
            return JsonResponse({'message': 'Booking deleted successfully'}, status=200)
        except AppartmentBookingModel.DoesNotExist:
            return JsonResponse({'error': 'Booking not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Failed to delete booking: {str(e)}'}, status=500)

@csrf_exempt
def airbnb_bookings(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                booking = AirbnbBookingModel.objects.get(pk=id)
                serializer = AirbnbBookingSerializer(booking)
                return JsonResponse(serializer.data)
            except AirbnbBookingModel.DoesNotExist:
                return JsonResponse({'error': 'Booking not found'}, status=404)
        else:
            bookings = AirbnbBookingModel.objects.all()
            serializer = AirbnbBookingSerializer(bookings, many=True)
            return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = AirbnbBookingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'PUT' or request.method == 'PATCH':
        data = json.loads(request.body)
        try:
            booking = AirbnbBookingModel.objects.get(pk=id)
        except AirbnbBookingModel.DoesNotExist:
            return JsonResponse({'error': 'Booking not found'}, status=404)
        serializer = AirbnbBookingSerializer(booking, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            booking = AirbnbBookingModel.objects.get(pk=id)
            booking.delete()
            return JsonResponse({'message': 'Booking deleted successfully'}, status=200)
        except AirbnbBookingModel.DoesNotExist:
            return JsonResponse({'error': 'Booking not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Failed to delete booking: {str(e)}'}, status=500)
