import requests

url = "http://localhost:8000/o/token/"
data = {
    "grant_type": "password",
    "username": "Luis",
    "password": "Mudar123",
    "client_id": "WEB_APP",
    "client_secret": "WEB_APP",
}

response = requests.post(url, data=data)

if response.status_code == 200:
    token = response.json()["access_token"]
    print("Token de acesso: " + token)
    print("response: " + str(response.json()))
else:
    print(
        "Falha na solicitação de token. Código de status: "
        + str(response.status_code)
        + "\n\n"
        + response.text
    )


# {"secret_key": "WG7UTEIP64R32MT2FKQ6WMDLEMRLJXDI"}
