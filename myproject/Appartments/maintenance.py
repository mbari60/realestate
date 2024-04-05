import json
from django.http import JsonResponse
from .models import MaintenanceRequestModel, ApartmentModel
from .serializers import MaintenanceRequestSerializer
from django.views.decorators.csrf import csrf_exempt 

@csrf_exempt
def maintenance_requests(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                maintenance_request = MaintenanceRequestModel.objects.get(pk=id)
                serializer = MaintenanceRequestSerializer(maintenance_request)
                return JsonResponse(serializer.data)
            except MaintenanceRequestModel.DoesNotExist:
                return JsonResponse({'error': 'Maintenance Request not found'}, status=404)
        else:
            maintenance_requests = MaintenanceRequestModel.objects.all()
            serializer = MaintenanceRequestSerializer(maintenance_requests, many=True)
            return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        
        # Check if the 'apartment_id' is provided in the request data
        apartment_id = data.get('apartment_id')
        if not apartment_id:
            return JsonResponse({'error': 'Apartment ID is required'}, status=400)
        
        # Check if the ApartmentModel instance exists
        try:
            apartment = ApartmentModel.objects.get(pk=apartment_id)
        except ApartmentModel.DoesNotExist:
            return JsonResponse({'error': 'Apartment not found'}, status=404)
        
        # Attach the apartment instance to the data before passing it to the serializer
        data['apartment'] = apartment_id
        
        # Create the serializer with the modified data
        serializer = MaintenanceRequestSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method in ['PUT', 'PATCH']:
        data = json.loads(request.body)
        
        try:
            maintenance_request = MaintenanceRequestModel.objects.get(pk=id)
        except MaintenanceRequestModel.DoesNotExist:
            return JsonResponse({'error': 'Maintenance Request not found'}, status=404)

        serializer = MaintenanceRequestSerializer(maintenance_request, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        try:
            maintenance_request = MaintenanceRequestModel.objects.get(pk=id)
            maintenance_request.delete()
            return JsonResponse({'message': 'Maintenance Request deleted successfully'}, status=200)
        except MaintenanceRequestModel.DoesNotExist:
            return JsonResponse({'error': 'Maintenance Request not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Failed to delete Maintenance Request: {str(e)}'}, status=500)
