import requests
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse  # Importe o HttpResponse


@login_required
def minha_pagina(request):
    print(request.__dict__)

    return render(request, "payment.html")


# A autenticação foi bem-sucedida, agora você pode fazer a solicitação desejada
# print(request.__dict__)
# print(request.__dir__())
# payment_list_url = "http://localhost:8000/payment/list"  # Substitua pelo URL real
# response = requests.get(
#     payment_list_url,
#     cookies=request.COOKIES,
#     headers=request.headers,

# )
# print(response)
# if response.status_code == 200:
#     # A solicitação para a lista de pagamentos foi bem-sucedida
#     payment_list = response.json()  # Suponha que a resposta seja em JSON
#     return render(request, "payment.html", {"payment_list": payment_list})
# else:
#     return render(
#         request,
#         "erro.html",
#         {"mensagem": "Falha na solicitação para a lista de pagamentos"},
#     )
