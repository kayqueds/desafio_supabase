# Desafio de Estágio Python | b2bflow

Este repositório contém a solução para o desafio de estágio em Python da b2bflow. O projeto consiste em um script que lê uma lista de contatos de um banco de dados Supabase e envia uma mensagem de WhatsApp personalizada para cada um, utilizando a Z-API.

---

## 🚀 Começando

Siga os passos abaixo para configurar e executar o projeto em sua máquina.

### Pré-requisitos

*   Python 3.8+
*   Conta gratuita no [Supabase](https://supabase.com/ )
*   Conta gratuita na [Z-API](https://www.z-api.io/ )

### 1. Instalação

Primeiro, clone o repositório e instale as dependências do projeto.

```bash
# Clone o repositório para o seu computador
git clone https://github.com/kayqueds/desafio_supabase.git

# Navegue até a pasta do projeto
cd desafio_supabase

# Instale as bibliotecas necessárias
pip install -r requirements.txt
```

### 2. Configuração do Banco de Dados (Supabase )

Para que o script funcione, você precisa de uma tabela no Supabase para armazenar os contatos.

Acesse o **SQL Editor** no seu painel do Supabase e execute o seguinte script:

```sql
-- Passo 1: Criar a tabela 'contatos'
CREATE TABLE contatos (
  id SERIAL PRIMARY KEY,
  nome_contato TEXT NOT NULL,
  numero_telefone TEXT NOT NULL
);

-- Passo 2: Inserir alguns dados de exemplo (opcional)
INSERT INTO contatos (nome_contato, numero_telefone) VALUES
  ('Primeiro Contato', '5511999999999'),
  ('Segundo Contato', '5521888888888');

-- Passo 3: Habilitar o acesso de leitura para a API (Obrigatório)
-- Isso permite que o script Python consulte os dados da tabela.
CREATE POLICY "Permitir acesso de leitura a todos"
ON public.contatos FOR SELECT USING (true);
```

### 3. Variáveis de Ambiente

O projeto utiliza um arquivo `.env` para gerenciar as chaves de API de forma segura. Crie um arquivo chamado `.env` na raiz do projeto e preencha com suas credenciais.

```ini
# Arquivo: .env

# Credenciais do Supabase
# Encontradas em: Configurações do Projeto > API
SUPABASE_URL="SUA_URL_DO_PROJETO_SUPABASE"
SUPABASE_KEY="SUA_CHAVE_ANON_SUPABASE"

# Credenciais da Z-API
# Encontradas no painel da Z-API
ZAPI_INSTANCE_ID="SEU_ID_DA_INSTANCIA"
ZAPI_TOKEN="SEU_TOKEN_DA_INSTANCIA"
ZAPI_CLIENT_TOKEN="SEU_CLIENT_TOKEN_DE_SEGURANCA"
```

---

## ▶️ Como Executar

Antes de rodar, certifique-se de que a sua instância na Z-API está **conectada** (leia o QR Code no painel com seu WhatsApp).

Para iniciar o script, execute o seguinte comando no terminal:

```bash
python main.py
```

O script irá exibir o progresso no terminal, mostrando os contatos encontrados e o status de envio de cada mensagem.
