import os
import socket
import hashlib
import zipfile
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
AUDIO_CACHE_DIR = os.path.join(STATIC_DIR, "audio")

# Descompacta automaticamente pacote_arquivos.zip na nuvem (ou quando as pastas não existirem)
ZIP_BUNDLE = os.path.join(BASE_DIR, "pacote_arquivos.zip")
if os.path.exists(ZIP_BUNDLE) and (os.environ.get("RENDER") or not os.path.exists(os.path.join(TEMPLATES_DIR, "index.html"))):
    try:
        with zipfile.ZipFile(ZIP_BUNDLE, "r") as zf:
            zf.extractall(BASE_DIR)
    except Exception as e:
        print(f"Aviso ao extrair pacote_arquivos.zip: {e}")

os.makedirs(AUDIO_CACHE_DIR, exist_ok=True)
os.makedirs(TEMPLATES_DIR, exist_ok=True)

app = FastAPI(
    title="Avós Online - Super App Assistivo",
    description="Aplicativo de inclusão digital e gerontecnologia com botões gigantes e narração por voz.",
    version="1.0.0"
)

# Monta arquivos estáticos e templates Jinja2 (aceita templates/ ou raiz caso arquivos tenham sido enviados soltos)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")
templates = Jinja2Templates(directory=[TEMPLATES_DIR, BASE_DIR])

@app.get("/api/tts")
async def tts_endpoint(text: str, voice: str = "pt-BR-FranciscaNeural"):
    """Gera e entrega áudios neurais ultrarrealistas e humanos com cache em disco"""
    text_clean = text.strip()
    if not text_clean:
        return JSONResponse({"error": "Texto vazio"}, status_code=400)

    text_hash = hashlib.md5(f"{voice}_{text_clean}".encode("utf-8")).hexdigest()
    file_path = os.path.join(AUDIO_CACHE_DIR, f"{text_hash}.mp3")

    if not os.path.exists(file_path):
        try:
            import edge_tts
            communicate = edge_tts.Communicate(text_clean, voice, rate="-4%")
            await communicate.save(file_path)
        except Exception as e:
            return JSONResponse({"error": str(e)}, status_code=500)

    return FileResponse(file_path, media_type="audio/mpeg")


# Estado em memória simulado para o Treino Bancário (Sandbox segura)
MOCK_BANK_STATE = {
    "saldo": 1500.00,
    "extrato": [
        {"tipo": "entrada", "descricao": "Depósito de Aposentadoria", "valor": 1500.00, "data": "Hoje, 09:30"},
        {"tipo": "saida", "descricao": "Compra Farmácia Pague Menos", "valor": 85.50, "data": "Ontem, 16:15"},
        {"tipo": "entrada", "descricao": "Pix Recebido - Filho Marcos", "valor": 100.00, "data": "12/10, 14:00"}
    ]
}

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Tela Inicial com os 6 botões gigantes"""
    return templates.TemplateResponse(request=request, name="index.html")

@app.get("/internet", response_class=HTMLResponse)
async def internet_manual(request: Request):
    """Módulo 1: Manual de Como Mexer na Internet (5 Aulas)"""
    return templates.TemplateResponse(request=request, name="internet.html")

@app.get("/whatsapp", response_class=HTMLResponse)
async def whatsapp_module(request: Request):
    """Módulo 2: WhatsApp Descomplicado (Vídeo + Atalho)"""
    return templates.TemplateResponse(request=request, name="whatsapp.html")

@app.get("/banco", response_class=HTMLResponse)
async def banco_module(request: Request):
    """Módulo 3: Treino de Transação Bancária (Simulador Pix Seguro)"""
    return templates.TemplateResponse(
        request=request,
        name="banco.html",
        context={
            "saldo": MOCK_BANK_STATE["saldo"], 
            "extrato": MOCK_BANK_STATE["extrato"]
        }
    )

@app.get("/medisafe", response_class=HTMLResponse)
async def medisafe_module(request: Request):
    """Módulo 4: Medisafe - Controle de Medicamentos e Horários"""
    return templates.TemplateResponse(request=request, name="medisafe.html")

@app.get("/telefone", response_class=HTMLResponse)
async def telefone_module(request: Request):
    """Módulo 5: Telefone - Ligações e Contatos Importantes"""
    return templates.TemplateResponse(request=request, name="telefone.html")

@app.get("/maps", response_class=HTMLResponse)
async def maps_module(request: Request):
    """Módulo 6: Google Maps - Localização e Rotas"""
    return templates.TemplateResponse(request=request, name="maps.html")

def obter_ip_local() -> str:
    """Descobre o IP da rede local para testes em Wi-Fi quando não estiver na nuvem"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

@app.get("/qrcode", response_class=HTMLResponse)
async def qrcode_evento(request: Request):
    """Página com Cartaz e QR Code para o Dia do Evento (iPhone e Android)"""
    forwarded_proto = request.headers.get("x-forwarded-proto", request.url.scheme)
    host = request.headers.get("x-forwarded-host") or request.headers.get("host") or "127.0.0.1:8080"
    
    # Se estiver acessando via localhost no computador, sugere o IP da rede local ou URL da nuvem
    if "127.0.0.1" in host or "localhost" in host:
        ip_local = obter_ip_local()
        porta = host.split(":")[1] if ":" in host else "8080"
        url_acesso = f"http://{ip_local}:{porta}"
    else:
        url_acesso = f"{forwarded_proto}://{host}"

    return templates.TemplateResponse(
        request=request,
        name="qrcode.html",
        context={
            "url_acesso": url_acesso,
            "host_atual": host
        }
    )

@app.get("/health")
async def health_check():
    """Endpoint de saúde para manter o servidor da nuvem acordado durante o evento"""
    return JSONResponse({"status": "ok", "app": "Avós Online"})

# Endpoints do Simulador de Banco
@app.post("/api/banco/pix")
async def simular_pix(request: Request):
    """Simula envio de Pix seguro sem dinheiro real"""
    data = await request.json()
    chave = data.get("chave", "")
    nome = data.get("nome", "Destinatário Simulado")
    valor = float(data.get("valor", 0))

    if valor <= 0:
        return JSONResponse({"sucesso": False, "mensagem": "Digite um valor maior que zero."})

    if valor > MOCK_BANK_STATE["saldo"]:
        return JSONResponse({"sucesso": False, "mensagem": "Saldo simulado insuficiente."})

    MOCK_BANK_STATE["saldo"] -= valor
    MOCK_BANK_STATE["extrato"].insert(0, {
        "tipo": "saida",
        "descricao": f"Pix enviado para {nome}",
        "valor": valor,
        "data": "Agora mesmo"
    })

    return JSONResponse({
        "sucesso": True,
        "mensagem": f"Pix de R$ {valor:.2f} enviado com sucesso para {nome}!",
        "novo_saldo": MOCK_BANK_STATE["saldo"],
        "comprovante": {
            "valor": f"R$ {valor:.2f}",
            "destinatario": nome,
            "chave": chave,
            "status": "Concluído com Sucesso (Simulação)"
        }
    })

@app.post("/api/banco/reset")
async def reset_banco():
    """Restaura saldo inicial do simulador para treinar novamente"""
    MOCK_BANK_STATE["saldo"] = 1500.00
    MOCK_BANK_STATE["extrato"] = [
        {"tipo": "entrada", "descricao": "Depósito de Aposentadoria", "valor": 1500.00, "data": "Hoje, 09:30"},
        {"tipo": "saida", "descricao": "Compra Farmácia Pague Menos", "valor": 85.50, "data": "Ontem, 16:15"},
        {"tipo": "entrada", "descricao": "Pix Recebido - Filho Marcos", "valor": 100.00, "data": "12/10, 14:00"}
    ]
    return JSONResponse({"sucesso": True, "novo_saldo": 1500.00})

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("app:app", host="0.0.0.0", port=port, reload=False)
