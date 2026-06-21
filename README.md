# 📲 Supabase + Z-API Challenge

> Projeto desenvolvido como desafio técnico para uma vaga de **estágio em Desenvolvimento Python**.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![WhatsApp](https://img.shields.io/badge/WhatsApp-Z--API-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)

---

## 📖 Sobre o projeto

Esta aplicação realiza a integração entre **Supabase** e **Z-API**, buscando contatos cadastrados em um banco de dados e enviando automaticamente uma mensagem personalizada pelo WhatsApp.

**Mensagem enviada:**

```
Olá, <nome_contato> tudo bem com você?
```

---

## 📸 Demonstração

### Supabase — tabela de contatos

<p align="center">
  <img width="700" alt="Tabela de contatos cadastrados no Supabase" src="https://github.com/user-attachments/assets/9b9294d2-8ebb-4421-9719-d822d0237548" />
</p>

### Terminal — execução do script


<p align="center">
  <img width="700" alt="Saída do terminal após envio das mensagens" src="https://github.com/user-attachments/assets/425135d0-3acd-4163-8546-21536bc07f5f" />
</p>

### WhatsApp — mensagem recebida

<p align="center">
  <img width="700" alt="Mensagem personalizada recebida no WhatsApp" src="https://github.com/user-attachments/assets/0043cd6b-9451-4210-bf27-95862ee7731e" />
</p>

---

## 🚀 Tecnologias

| Tecnologia | Descrição |

|------------|-----------|
| **Python 3** | Linguagem principal |
| **Supabase** | Banco de dados e API |
| **Z-API** | Integração com WhatsApp |
| **Requests** | Requisições HTTP |
| **python-dotenv** | Gerenciamento de variáveis de ambiente |

---

## 📂 Estrutura do projeto

```
.
├── assets/
│   ├── supabase.png
│   ├── terminal.png
│   └── whatsapp.png
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

---

## 🗄️ Estrutura da tabela

**Tabela:** `contatos`

| Campo | Tipo |
|-------|------|
| `id` | int8 |
| `nome_contato` | text |
| `telefone_contato` | text |

---

## ⚙️ Configuração

### 1. Clone o projeto

```bash
git clone https://github.com/Gabrielb-del/python-challenge.git
cd supabase-zapi-challenge
```

### 2. Crie um ambiente virtual

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 🔐 Variáveis de ambiente

Crie um arquivo chamado `.env` na raiz do projeto utilizando o `.env.example` como modelo.

```env
SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
ZAPI_CLIENT_TOKEN=
```

---

## ▶️ Executando

```bash
python main.py
```

---

## 🔄 Fluxo da aplicação

```
Supabase
     │
     ▼
Busca até 3 contatos
     │
     ▼
Personaliza a mensagem
     │
     ▼
Envia via Z-API
     │
     ▼
Resultado exibido no terminal
```

---

## 💻 Exemplo de saída

```
1 contato(s) encontrado(s).

✅ Mensagem enviada para Gabriel (5514999999999)
```

---

## 📦 Dependências

| Pacote | Uso |
|--------|-----|
| `supabase` | Conexão com o banco de dados |
| `requests` | Envio de mensagens via Z-API |
| `python-dotenv` | Carregamento de credenciais |

---

## ✅ Funcionalidades

- [x] Busca contatos no Supabase
- [x] Limita o envio para até **3 contatos**
- [x] Personaliza a mensagem utilizando o nome do contato
- [x] Envia mensagens via WhatsApp utilizando a Z-API
- [x] Utiliza variáveis de ambiente
- [x] Tratamento básico de erros

---

## 📌 Observações

> ⚠️ Este projeto utiliza apenas recursos **gratuitos** do Supabase e da Z-API.

- O arquivo `.env` **não deve** ser enviado ao GitHub.
- As credenciais são carregadas por variáveis de ambiente utilizando `python-dotenv`.

---

## 👨‍💻 Autor

**Gabriel Baunilia**
