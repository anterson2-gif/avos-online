# Documentação Completa: Avós Online - Super App Assistivo

> **Projeto Educacional de Gerontecnologia e Inclusão Digital**  
> Desenvolvido de forma autoral para promover autonomia, independência e segurança para pessoas idosas no uso do smartphone e da internet.

---

## 1. Visão Geral do Projeto

* **Nome do Aplicativo:** **Avós Online**
* **Objetivo Primordial:** Eliminar as barreiras digitais enfrentadas pela terceira idade, combatendo o medo de "estragar o celular", a ansiedade diante de interfaces complexas e a vulnerabilidade a golpes virtuais e bancários.
* **Modelo de Desenvolvimento:** Código próprio, limpo e aberto, sem dependência de plataformas proprietárias ou pagas.
* **Público-Alvo:** Pessoas idosas (incluindo usuários sem nenhuma experiência prévia com tecnologia) e seus familiares/cuidadores.
* **Diretório Raiz do Código:** `C:\Users\user\avos_online`
* **Atalho Rápido (Desktop):** `C:\Users\user\Desktop\Iniciar_Avos_Online.bat`
* **URL Local:** `http://127.0.0.1:8080` (porta 8080 isolada para coexistência harmoniosa com outros sistemas locais)

---

## 2. Princípios de Usabilidade e Gerontecnologia (WCAG AAA)

O desenvolvimento seguiu rigorosamente os padrões de **Gerontecnologia** e as diretrizes internacionais de acessibilidade (WCAG nível AAA):

### 2.1. Alvos de Toque e Ergonomia
* **Tamanho Mínimo de Botões:** 80px de altura com espaçamento generoso para evitar toques acidentais por tremores ou perda de precisão motora.
* **Cores de Alto Contraste:** Fundos escuros profundos (`#0B132B`, `#0F172A`) combinados com cartões de cores vibrantes e contrastantes (azul, verde esmeralda, ouro, vermelho carmesim e roxo).

### 2.2. Interações sem Frustração
* **Sem Gestos de Deslizar (Swipe) ou Pinça:** Nenhuma função depende de movimentos complexos. Toda navegação ocorre por toques únicos e objetivos.
* **Barra de Fuga Segura Fixa:** Todas as telas internas contam com uma barra dourada fixa no rodapé: `⬅ VOLTAR AO INÍCIO`. O idoso sempre sabe como retornar com segurança.

### 2.3. Sistema de Duplo Feedback Imediato
1. **Feedback Háptico (Vibração):** Pulso tátil suave de `40ms` acionado a cada toque (`navigator.vibrate([40])`).
2. **Síntese Harmônica de Som:** Acorde sintetizado em tempo real (Web Audio API a 520Hz + 660Hz) que confirma a ação sem depender de arquivos de áudio externos.
3. **Narração em Voz Alta (TTS pt-BR):** Text-to-Speech pausado (`rate = 0.90`) em português brasileiro, que lê instruções, confirma valores digitados e narra as aulas.
4. **Controle no Topo:** Botão `🔊 Voz: LIGADA / DESLIGADA` e alternador `🔤 Letra: A+`.

---

## 3. Arquitetura Tecnológica e Stack de Software

O aplicativo foi construído utilizando tecnologias modernas, leves e portáteis:

| Componente | Tecnologia Utilizada | Finalidade no Projeto |
| :--- | :--- | :--- |
| **Servidor / Backend** | Python 3.13 + FastAPI + Uvicorn | Roteamento, APIs do simulador de banco e entrega de páginas |
| **Renderização Web** | Jinja2 Templates | Modularização de layout com herança de template base |
| **Estilização** | CSS3 Moderno (Custom Properties) | Paleta WCAG AAA, teclado numérico e player de vídeo animado |
| **Motor Assistivo** | JavaScript Puro (ES6+) | Web Speech API, Web Audio API, Vibration API e controle de estados |
| **Recurso Mobile / PWA** | Web App Manifest + Service Worker | Instalação na tela inicial do celular como aplicativo nativo |
| **Gráficos & Animações**| SVG Vetorial + CSS Keyframes | Ilustrações dos personagens em alta resolução sem perda de nitidez |

---

## 4. Detalhamento dos 6 Módulos do Super App

### 4.1. Tela Inicial (`index.html`)
* **Apresentação:** Saudação acolhedora com botão *"📢 Ouvir Opções"*, que dita em voz alta pausadamente os 6 botões disponíveis.
* **Grid de 6 Botões Superdimensionados:**
  1. `1. Como Mexer na Internet` (Azul vibrante)
  2. `2. WhatsApp Descomplicado` (Verde WhatsApp)
  3. `3. Treino de Banco Seguro` (Verde Petróleo/Segurança)
  4. `4. Remédios e Horários (Medisafe)` (Vermelho saúde)
  5. `5. Telefone e Chamadas` (Roxo vibrante)
  6. `6. Como Chegar e Rotas (Maps)` (Âmbar/Laranja rotas)

---

### 4.2. Módulo 1: Manual de Como Mexer na Internet (`internet.html`)
Desenvolvido com um **Player de Desenho Animado Educativo** estrelado pelos personagens:
* **Dona Maria:** Vovó de óculos dourados e sorriso amigável.
* **Seu José:** Vovô simpático de boina marrom e colete verde.
* **Pedrinho:** O neto atencioso que ensina os avós com paciência.

#### As 5 Aulas em Desenho com Treino Integrado:
1. **Aula 01 - Como Tocar na Tela:**
   * *Vídeo Animado:* Dona Maria tem medo de apertar a tela. Pedrinho explica que o toque deve ser leve como uma borboleta. A tela pisca com uma estrela dourada sem quebrar nada.
   * *Treino Prático:* Botão interativo de toque suave que aciona uma estrela e som de sucesso.
2. **Aula 02 - Wi-Fi ou Dados Móveis:**
   * *Vídeo Animado:* Seu José aprende que o roteador de casa emite ondas azuis de sinal livre (Wi-Fi) que não gastam os créditos do chip da rua.
   * *Treino Prático:* Simulador de ligar o Wi-Fi com confirmação visual e sonora.
3. **Aula 03 - Pesquisar no Google por Voz:**
   * *Vídeo Animado:* Dona Maria precisa de uma receita de bolo de fubá. Em vez de digitar, aperta o microfone e fala. O Google responde com um bolo fumegante e cadeado verde de segurança 🔒.
   * *Treino Prático:* Simulador de comando de voz com retorno imediato da receita.
4. **Aula 04 - Enviar Fotos e Mensagens:**
   * *Vídeo Animado:* Dona Maria grava um áudio no microfone verde do WhatsApp. O balãozinho voa, os risquinhos ficam azuis (`✔✔`) e Pedrinho recebe com um coração de amor.
   * *Treino Prático:* Simulador de envio de áudio com explicação dos risquinhos.
5. **Aula 05 - Como se Proteger de Golpes (Detetive Antigolpe):**
   * *Vídeo Animado:* Um golpista mascarado manda mensagem com foto falsa pedindo Pix urgente. Seu José coloca óculos de detetive, liga para o filho de verdade e um escudo dourado gigante bloqueia a tentativa de golpe!
   * *Treino Prático:* Quiz interativo com desafios práticos e avisos sonoros de perigo.

---

### 4.3. Módulo 2: WhatsApp Descomplicado (`whatsapp.html`)
* **Launcher Direto:** Botão gigante em verde vibrante para abrir o aplicativo oficial instalado no aparelho (`whatsapp://send`).
* **Player dos 4 Recursos Fundamentais:**
  1. *Mensagem de Voz (Áudio):* Como manter o dedo no microfone verde e soltar para enviar.
  2. *Fotos e Galeria:* Como acionar a câmera e enviar fotos do almoço ou da família.
  3. *Chamada de Vídeo:* Como acionar a camerazinha no topo para ver o rosto de quem ama ao vivo.
  4. *Digitação de Texto:* Como digitar sem pressa e enviar na setinha verde.
* **Controles do Guia:** Botões *"Repetir Explicação"* e *"Pausar Voz"*.

---

### 4.4. Módulo 3: Treino de Transação Bancária (`banco.html`)
* **Sandbox 100% Segura:** Saldo fictício de **R$ 1.500,00** sem movimentação de dinheiro real.
* **Digitação Real do Valor Desejado:**
  * **Visor Gigante:** Mostra `R$ [digitado]` em amarelo brilhante de grande escala.
  * **Teclado Numérico Gigante na Tela:** Botões táteis de 1 a 9, 0, `🗑️ Limpar` e `⌫ Apagar` com leitura falada instantânea do valor digitado (ex: *"Cinquenta reais"*).
  * **Compatibilidade com Teclado Físico:** Teclas `0-9`, `Backspace` e `Enter` no computador.
* **Revisão Obrigatória de Segurança:** Antes de concluir o Pix, o sistema exibe o nome do destinatário em letras garrafais e alerta por voz: *"Confira o nome da pessoa antes de apertar no botão verde!"*.
* **Comprovante Fictício:** Geração de recibo simulado com carimbo verde de aprovação.
* **Extrato Simples:** Entradas em verde claro (`+`) e saídas em vermelho (`-`) sem termos técnicos como TED, DOC ou DDA.
* **Laboratório Antigolpe Bancário:** 3 cenários práticos (falso gerente do banco, nome divergente na chave Pix e falso Pix recebido por engano).

---

### 4.5. Módulo 4: Medisafe - Medicamentos e Horários (`medisafe.html`)
* **Launcher Direto:** Abertura do Medisafe instalado (`Intent` do Android) com link assistido para a Google Play Store.
* **Guia Didático dos 5 Recursos:**
  1. *Som de Chocalho de Remédio:* Demonstração do alarme sonoro característico e visualização do comprimido.
  2. *Botão "TOMEI":* Instrução para registrar a dose e evitar tomar remédios em duplicidade.
  3. *Função Soneca (Lembrar Mais Tarde):* Como adiar em 15 minutos caso esteja almoçando ou fora.
  4. *Aviso de Reabastecimento:* Como o app avisa quando sobram 3 ou 4 pílulas para comprar na farmácia.
  5. *Rede de Apoio (Medfriend):* Explicação de que filhos e cuidadores podem receber notificações de segurança.

---

### 4.6. Módulo 5: Telefone e Chamadas Rápidas (`telefone.html`)
* **Chamadas de Emergência Gratuitas (1 Toque):** Botões diretos para **SAMU 192**, **Polícia Militar 190** e **Bombeiros 193**.
* **Agenda de Favoritos com Foto:** Cartões dos familiares (Filho Marcos, Filha Mariana, Neto Lucas) com foto grande e acionamento direto via `tel:`.
* **Simulador de Chamada Recebida:** O aparelho simula uma ligação tocando (toque sonoro e vibração contínua) com botões *"ATENDER"* e *"RECUSAR"*, permitindo que o idoso treine o gesto sem nervosismo.
* **Atalho para Discador Nativo:** Acesso ao teclado de discagem do smartphone (`tel:`).

---

### 4.7. Módulo 6: Google Maps - Localização e Rotas (`maps.html`)
* **Launcher Direto:** Abertura do Google Maps (`geo:0,0?q=`).
* **Atalhos Rápidos com 1 Toque:** "Farmácia Perto" e "Posto de Saúde".
* **Tutorial Didático da Bolinha Azul:**
  * Explicação clara de que a **bolinha azul** representa exatamente a localização física do idoso.
  * Como usar a **busca por voz pelo microfone** para encontrar ruas e igrejas.
  * Escolha de meios de transporte com instruções: **A Pé**, **Ônibus** e **Carro**, com acionamento do botão *"INICIAR"* para GPS falado.

---

## 5. Estrutura Completa de Diretórios e Arquivos

```
C:\Users\user\avos_online\
│
├── app.py                         # Servidor FastAPI com rotas e API do banco simulado
├── iniciar_avos_online.bat        # Script de inicialização automática local
├── README.md                      # Guia do projeto e especificações para alunos
├── DOCUMENTACAO_COMPLETA.md       # Documentação técnica e operacional detalhada
│
├── templates\                     # Templates HTML Jinja2
│   ├── base.html                  # Layout base (PWA, motor de acessibilidade, barra de retorno)
│   ├── index.html                 # Tela Inicial (6 botões gigantes e botão ouvir opções)
│   ├── internet.html              # Módulo 1 (5 vídeos animados em desenho + treinos)
│   ├── whatsapp.html              # Módulo 2 (Launcher WhatsApp + guia dos 4 recursos)
│   ├── banco.html                 # Módulo 3 (Simulador Pix com teclado gigante na tela)
│   ├── medisafe.html              # Módulo 4 (Launcher Medisafe + guia dos medicamentos)
│   ├── telefone.html              # Módulo 5 (Emergência 192/190/193 + simulador de chamada)
│   └── maps.html                  # Módulo 6 (Launcher Maps + guia da bolinha azul e rotas)
│
└── static\                        # Recursos estáticos
    ├── manifest.json              # Manifesto PWA para instalação no celular
    ├── sw.js                      # Service Worker para cache e suporte offline
    ├── css\
    │   └── app.css                # Estilos WCAG AAA, teclado gigante e player animado
    ├── js\
    │   └── app.js                 # Motor assistivo (Web Speech, Web Audio, Vibração)
    └── icons\
        ├── icon-192.png           # Ícone PWA 192x192
        └── icon-512.png           # Ícone PWA 512x512
```

---

## 6. Guia Operacional: Como Executar e Usar

### 6.1. Inicialização pelo Windows
Basta dar um duplo clique no atalho criado na Área de Trabalho:
👉 **`C:\Users\user\Desktop\Iniciar_Avos_Online.bat`**
O terminal iniciará o servidor Uvicorn e abrirá o navegador automaticamente em `http://127.0.0.1:8080`.

### 6.2. Inicialização via Terminal / PowerShell
```powershell
cd C:\Users\user\avos_online
python -m uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```

### 6.3. Acesso e Instalação no Smartphone dos Idosos (PWA)
1. Conecte o computador e o celular na **mesma rede Wi-Fi**.
2. No celular, abra o navegador (Chrome ou Safari) e acesse: `http://[IP-DO-COMPUTADOR]:8080`.
3. Toque no menu do navegador (três pontinhos ou botão de compartilhar) e selecione **"Adicionar à Tela Inicial"** ou **"Instalar Aplicativo"**.
4. O ícone do **Avós Online** aparecerá na tela do celular como um aplicativo nativo independente, sem barras de navegador.
