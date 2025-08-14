# main.py - VERSÃO CORRETA E COMPLETA
import os
import time
import requests
from dotenv import load_dotenv
from supabase import create_client, Client

# --- CONFIGURAÇÃO INICIAL ---
load_dotenv()

# Configura e valida o Supabase
supabase_url = os.getenv("SUPABASE_URL")
supabase_key = os.getenv("SUPABASE_KEY")
if not supabase_url or not supabase_key:
    print("🚨 Erro: Verifique as variáveis SUPABASE_URL e SUPABASE_KEY no seu .env.")
    exit()
try:
    supabase: Client = create_client(supabase_url, supabase_key)
    print("✅ Conexão com o Supabase estabelecida.")
except Exception as e:
    print(f"🚨 Erro ao conectar com o Supabase: {e}")
    exit()

# --- FUNÇÕES ---

def buscar_contatos():
    """Busca contatos da tabela 'contatos' no Supabase."""
    try:
        print("\nBuscando contatos...")
        response = supabase.table("contatos").select("*").execute()
        if response.data:
            print(f"🔍 {len(response.data)} contatos encontrados.")
            return response.data
        else:
            print("⚠️ Nenhum contato encontrado.")
            return []
    except Exception as e:
        print(f"🚨 Erro ao buscar contatos: {e}")
        return []

def enviar_mensagem(nome_contato, numero_telefone):
    """Envia uma mensagem via Z-API com a autenticação correta."""
    # Carrega as 3 chaves necessárias da Z-API
    zapi_token = os.getenv("ZAPI_TOKEN") # <-- Lendo a variável correta
    zapi_instance_id = os.getenv("ZAPI_INSTANCE_ID")
    zapi_client_token = os.getenv("ZAPI_CLIENT_TOKEN") # <-- Lendo a chave nova

    if not all([zapi_token, zapi_instance_id, zapi_client_token]):
        print("🚨 Erro: Verifique as 3 variáveis da Z-API no seu arquivo .env.")
        return False

    url = f"https://api.z-api.io/instances/{zapi_instance_id}/token/{zapi_token}/send-text"
    
    payload = {
        "phone": str(numero_telefone ),
        "message": f"Olá {nome_contato}, tudo bem com você?"
    }
    
    # Adiciona o Client-Token no cabeçalho (ESTA É A CORREÇÃO CRÍTICA)
    headers = {
        "Content-Type": "application/json",
        "Client-Token": zapi_client_token 
    }

    try:
        print(f"  -> Enviando para {nome_contato} ({numero_telefone})...")
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        print(f"  ✅ Mensagem enviada com sucesso! ID: {response.json().get('messageId')}")
        return True
    except requests.exceptions.HTTPError as e:
        print(f"  ❌ Falha no envio: {e.response.status_code} - {e.response.text}")
        return False
    except Exception as e:
        print(f"  ❌ Falha no envio: {e}")
        return False

# --- FLUXO PRINCIPAL ---
if __name__ == "__main__":
    print("🚀 Iniciando o script do desafio b2bflow...")
    contatos = buscar_contatos()

    if contatos:
        print("\nIniciando o envio de mensagens...")
        sucessos = 0
        falhas = 0
        for contato in contatos:
            nome = contato.get("nome_contato")
            telefone = contato.get("numero_telefone")
            if nome and telefone:
                if enviar_mensagem(nome, telefone):
                    sucessos += 1
                else:
                    falhas += 1
                time.sleep(2)
            else:
                print(f"⚠️ Contato ignorado por dados ausentes: {contato}")
                falhas += 1
        
        print("\n--- Resumo do Envio ---")
        print(f"✅ Sucessos: {sucessos} | ❌ Falhas: {falhas}")
    
    print("🏁 Script finalizado.")
