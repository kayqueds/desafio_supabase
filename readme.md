# Desafio B2BFlow - Envio de Mensagens

## Setup
1. Crie uma tabela `contatos` no Supabase com os campos `id`, `nome_contato` e `numero_telefone`.
2. Insira pelo menos 3 contatos.

## Variáveis de Ambiente
- `SUPABASE_URL`: URL do projeto Supabase.
- `SUPABASE_KEY`: Chave pública do Supabase.
- `ZAPI_KEY`: Chave da Z-API.
- `ZAPI_INSTANCE_ID`: Instance ID da Z-API.

## Como Rodar
```bash
pip install -r requirements.txt
python main.py
