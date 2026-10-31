# Guia Passo a Passo: Hospedar o "Avós Online" na Nuvem (Link Fixo + QR Code para o Evento)

Este guia mostra como colocar o **Avós Online** no ar gratuitamente no **Render.com** (ou **Railway**) gerando um link fixo `https://...` compatível com **iPhone (Safari)** e **Smartphone Android (Chrome)** — ideal para imprimir o QR Code antes do evento.

---

## Parte 1: O que já está pronto na pasta `C:\Users\user\avos_online`

Todos os arquivos exigidos pelos servidores em nuvem já foram gerados automaticamente:
* `requirements.txt` — Lista exata das bibliotecas (`fastapi`, `uvicorn`, `jinja2`, `edge-tts`).
* `render.yaml` — Configuração automática (Blueprint) para o Render.com.
* `Procfile` — Configuração automática para o Railway.
* `templates/qrcode.html` — Cartaz pronto para impressão A4 e telão em `/qrcode`, com modo anti-hibernação para o dia do evento.
* `static/audio/` — 37 áudios neurais da voz humana (`pt-BR-FranciscaNeural`) já salvos em cache para resposta imediata na nuvem.

---

## Parte 2: Subir o Projeto no GitHub (Pelo Navegador, sem precisar de comandos)

1. Acesse **[github.com](https://github.com)** e entre na sua conta (ou crie uma gratuita).
2. Clique no botão **`+`** (canto superior direito) e escolha **"New repository"**.
3. Em **Repository name**, digite: `avos-online`
4. Deixe marcado como **Public** (ou Private) e clique no botão verde **"Create repository"**.
5. Na tela seguinte, clique no link azul **"uploading an existing file"**.
6. Abra a pasta `C:\Users\user\avos_online` no seu computador, selecione **todos os arquivos e pastas** (exceto a pasta `__pycache__`) e **arraste para dentro da janela do GitHub**.
7. Aguarde a barra de envio terminar e clique no botão verde **"Commit changes"** lá embaixo.

---

## Parte 3: Ativar o Link Fixo Gratuito no Render.com (3 Minutos)

1. Acesse **[render.com](https://render.com)** e clique em **"Get Started for Free"**.
2. Escolha **"Sign in with GitHub"** (entrar com a mesma conta do GitHub do passo anterior).
3. No painel do Render, clique em **"New +"** (no topo) e selecione **"Web Service"**.
4. Selecione o repositório **`avos-online`** que você acabou de criar e clique em **"Connect"**.
5. Preencha apenas estes 3 campos (se já não vierem preenchidos):
   * **Name:** `avos-online` *(isso criará o link `https://avos-online.onrender.com`)*
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `uvicorn app:app --host 0.0.0.0 --port $PORT`
6. Escolha a opção **Free ($0/month)** e clique no botão **"Deploy Web Service"**.
7. Em cerca de **2 a 3 minutos**, aparecerá **`Live`** em verde no topo com o seu link fixo oficial (ex: `https://avos-online.onrender.com`)!

---

## Parte 4: Imprimir o Cartaz A4 com QR Code para o Evento

1. Assim que o seu link da nuvem estiver no ar, acesse:
   👉 **`https://SEU-LINK.onrender.com/qrcode`** (ou acesse localmente `http://127.0.0.1:8080/qrcode` e cole o link da nuvem na caixa de texto).
2. Clique em **"🖨️ Imprimir Cartaz A4"**.
3. O sistema já imprime o **QR Code gigante de alto contraste** + as instruções separadas para **🍎 iPhone (Safari)** e **🤖 Android (Chrome)**.

---

## 💡 Dica de Ouro para o Dia do Evento (Zero Espera no Plano Grátis)

No plano gratuito do Render, se ninguém acessar o site por 15 minutos, ele entra em "repouso". Para garantir que o aplicativo abra **instantaneamente em menos de 1 segundo** durante todo o dia do evento:
* No início do evento, deixe a página **`https://SEU-LINK.onrender.com/qrcode`** aberta em qualquer computador ou celular da organização.
* Essa página possui um **Modo Evento Ativo (Anti-Hibernação)** que envia um sinal automático a cada 3 minutos para `/health`, mantendo o servidor da nuvem 100% acordado durante todo o evento!
