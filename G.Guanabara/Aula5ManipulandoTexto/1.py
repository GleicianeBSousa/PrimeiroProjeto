import requests


api_url = "HTTPS://WWW.EXCHANGERATE-API.COM/"

try:
    
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        print("Dados da API:", data)
    else:
        print(f"Falha na requisição. Código de status: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Erro na requisição: {e}")
