# # views.py
# from django.shortcuts import render
# from django.http import JsonResponse
# from django_daraja.mpesa.core import MpesaClient

# def initiate_payment(request):
#     mpesa_client = MpesaClient()
#     phone_number = '2547XXXXXXXX'
#     amount = 1
#     account_reference = 'account_reference'
#     transaction_desc = 'Payment description'
#     callback_url = 'https://yourdomain.com/callback'
#     response = mpesa_client.lipa_na_mpesa_online(
#         phone_number, amount, account_reference, transaction_desc, callback_url)
#     return JsonResponse(response)
