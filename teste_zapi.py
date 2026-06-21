import os
import requests
from dotenv import load_dotenv

load_dotenv()

url = (
    f"https://api.z-api.io/instances/"
    f"{os.getenv('ZAPI_INSTANCE_ID')}"
    f"/token/{os.getenv('ZAPI_TOKEN')}"
    f"/send-text"
)

payload = {
    "phone": "5514998445606",  
    "message": "Teste de envio"
}

print("URL utilizada:")
print(url)
print()

response = requests.post(
    url,
    json=payload
)

print("Status Code:", response.status_code)
print("Resposta:")
print(response.text)