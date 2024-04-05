import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import InquiryModel
from .serializers import InquirySerializer

@csrf_exempt
def inquiries(request, id=None):
    if request.method == 'GET':
        if id is not None:
            try:
                inquiry = InquiryModel.objects.get(pk=id)
                serializer = InquirySerializer(inquiry)
                return JsonResponse(serializer.data)
            except InquiryModel.DoesNotExist:
                return JsonResponse({'error': 'Inquiry not found'}, status=404)
        else:
            inquiries = InquiryModel.objects.all()
            serializer = InquirySerializer(inquiries, many=True)
            return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = InquirySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method in ['PUT', 'PATCH']:
        data = json.loads(request.body)
        try:
            inquiry = InquiryModel.objects.get(pk=id)
        except InquiryModel.DoesNotExist:
            return JsonResponse({'error': 'Inquiry not found'}, status=404)
        serializer = InquirySerializer(inquiry, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            inquiry = InquiryModel.objects.get(pk=id)
            inquiry.delete()
            return JsonResponse({'message': 'Inquiry deleted successfully'}, status=200)
        except InquiryModel.DoesNotExist:
            return JsonResponse({'error': 'Inquiry not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Failed to delete inquiry: {str(e)}'}, status=500)
