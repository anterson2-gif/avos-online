import os
import asyncio
import hashlib
import edge_tts

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(BASE_DIR, "static", "audio")
os.makedirs(AUDIO_DIR, exist_ok=True)

VOICE = "pt-BR-FranciscaNeural"
# -4% de taxa para ficar num ritmo calmo, claro e natural para idosos
RATE = "-4%"

FRASES = [
    # Tela / Cabeçalho
    "Você está no Manual da Internet. Agora com vídeos com personagens reais de Dona Maria e Seu José para te ensinar passo a passo!",
    "Este é o seu manual com vídeos passo a passo com personagens reais. Toque em qualquer aula para assistir e aprender sem medo.",
    
    # Aula 1
    "Aula 1: Vídeo da Dona Maria tocando na tela aberta! Toque no botão azul para assistir ao vídeo passo a passo.",
    "Dona Maria tinha receio de quebrar o aparelho se tocasse na tela.",
    "O neto Pedrinho explicou com carinho: Vovó, basta um toque leve como uma borboleta pousando.",
    "A tela acendeu com uma linda estrela sem quebrar nada! Dona Maria ficou muito feliz e confiante!",
    "Parabéns! Você tocou com perfeição, igualzinho à Dona Maria no vídeo!",

    # Aula 2
    "Aula 2: Vídeo do Seu José no Wi-Fi aberta! Toque no botão azul para assistir ao vídeo passo a passo.",
    "O Seu José achava que para ver fotos e vídeos sempre gastava os créditos do celular.",
    "Mas em casa, o roteador emite o sinal de Wi-Fi, que é livre e sem limites.",
    "O símbolo do arquinho acendeu no celular! Agora o Seu José pode usar a internet à vontade sem gastar seu chip!",
    "Wi-Fi ligado! Agora você está com internet sem limite igual ao Seu José!",

    # Aula 3
    "Aula 3: Vídeo da Dona Maria pesquisando por voz aberta! Toque no botão azul para assistir ao vídeo passo a passo.",
    "Dona Maria queria achar uma receita de bolo de fubá, mas não queria digitar letrinhas pequenas.",
    "Ela tocou no microfone do Google e fez a pergunta com a sua própria voz.",
    "O Google encontrou a receita na hora em um site com o cadeado verde de segurança!",
    "Pergunta ouvida: Como fazer bolo de fubá fofinho? O Google encontrou a receita com cadeado de proteção!",

    # Aula 4
    "Aula 4: Vídeo de envio de mensagens e áudio aberta! Toque no botão azul para assistir ao vídeo passo a passo.",
    "Dona Maria segurou o botão do microfone verde do WhatsApp e gravou um áudio com carinho.",
    "A mensagem voou pelo ar e os dois risquinhos azuis confirmaram que o neto já abriu o áudio.",
    "Pedrinho ouviu a vovó sorrindo e mandou um coração cheio de amor de volta!",
    "Áudio enviado! Os dois risquinhos azuis confirmam que seu neto já ouviu!",

    # Aula 5
    "Aula 5: Vídeo do Seu José detetive contra os golpes aberta! Toque no botão azul para assistir ao vídeo passo a passo.",
    "Um golpista mandou uma mensagem falsa se passando pelo filho do Seu José pedindo dinheiro urgente.",
    "Mas o Seu José foi muito esperto: não transferiu nada e ligou para a voz do filho de verdade.",
    "O filho confirmou que era mentira! O golpe foi bloqueado e o dinheiro continuou protegido no bolso!",
    "Você acertou em cheio! Sempre faça como o Seu José no vídeo: desconfie e ligue para confirmar antes de mandar qualquer valor!",
    "Cuidado! Isso é um golpe perigoso. Lembre-se do vídeo do Seu José: sempre ligue para o seu filho antes de transferir!",

    # Controles de acessibilidade
    "Voz ativada! Eu vou te acompanhar em cada passo.",
    "Tamanho de letra normal",
    "Tamanho de letra grande",
    "Tamanho de letra gigante"
]

def get_hash(text: str, voice: str) -> str:
    return hashlib.md5(f"{voice}_{text.strip()}".encode("utf-8")).hexdigest()

async def gerar_todos():
    print(f"Gerando {len(FRASES)} áudios neurais com {VOICE}...")
    for idx, frase in enumerate(FRASES, 1):
        h = get_hash(frase, VOICE)
        filepath = os.path.join(AUDIO_DIR, f"{h}.mp3")
        if os.path.exists(filepath):
            print(f"[{idx}/{len(FRASES)}] Já em cache: {frase[:35]}...")
            continue
        try:
            communicate = edge_tts.Communicate(frase, VOICE, rate=RATE)
            await communicate.save(filepath)
            print(f"[{idx}/{len(FRASES)}] Gerado com sucesso: {frase[:35]}...")
        except Exception as e:
            print(f"[{idx}/{len(FRASES)}] Erro: {e}")

if __name__ == "__main__":
    asyncio.run(gerar_todos())
