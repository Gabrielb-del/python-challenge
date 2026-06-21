from dotenv import load_dotenv
from supabase import create_client
import requests
import os

# Carrega as variáveis de ambiente
load_dotenv()

# Configuração do Supabase
supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# Busca até 3 contatos
try:
    response = (
        supabase
        .table("contatos")
        .select("*")
        .limit(3)
        .execute()
    )

    contatos = response.data

except Exception as e:
    print(f"Erro ao buscar contatos: {e}")
    exit()

# Verifica se encontrou contatos
if not contatos:
    print("Nenhum contato encontrado.")
    exit()

# URL da Z-API
url = (
    f"https://api.z-api.io/instances/"
    f"{os.getenv('ZAPI_INSTANCE_ID')}"
    f"/token/{os.getenv('ZAPI_TOKEN')}"
    f"/send-text"
)

print(f"{len(contatos)} contato(s) encontrado(s).\n")

# Envia as mensagens
for contato in contatos:

    nome = contato["nome_contato"]
    telefone = contato["telefone_contato"]

    mensagem = f"Olá, {nome} tudo bem com você?"

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    try:
        
        headers = {
            "Client-Token": os.getenv("ZAPI_CLIENT_TOKEN")
        }

        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=30
        )

        if response.status_code == 200:

            print(
                f"✅ Mensagem enviada para "
                f"{nome} ({telefone})"
            )

        else:

            print(
                f"❌ Erro ao enviar para "
                f"{nome}: {response.text}"
            )

    except Exception as e:

        print(
            f"❌ Falha ao enviar para "
            f"{nome}: {e}"
        )