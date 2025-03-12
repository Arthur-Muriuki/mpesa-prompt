from urllib import response

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django_daraja.mpesa.core import MpesaClient


# Create your views here.
def index(request):
    return render(request,'index.html')
def lipa_na_mpesa_online(request):
    if request.method == 'POST':
        phone_number = request.POST['phone']
        amount = int(request.POST['amount'])
        account_reference = 'Reference',
        transaction_desc="Description",
        callback_url="https://fda6-154-70-14-172.ngrok-free.app/callback"

        cl=MpesaClient()
        response=cl.stk_push(phone_number,amount, account_reference, transaction_desc, callback_url)
        return HttpResponse(response)
    return HttpResponse('invalid request')
@csrf_exempt
def mpesa_callback(request):
    if request.method == 'POST':
        data=request.body
        print("mpesa callback details",data)
        return JsonResponse({'status':'success'})
    return JsonResponse({'status':'failure'})
