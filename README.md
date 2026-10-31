# Avós Online - Super Aplicativo Assistivo de Inclusão Digital

**Projeto Educacional de Gerontecnologia desenvolvido por alunos.**

O **Avós Online** foi planejado e construído especificamente para capacitar pessoas idosas a utilizarem a tecnologia com total independência, tranquilidade, segurança e sem medo de errar ou danificar o aparelho.

---

## 👵 Padrões de Usabilidade e Acessibilidade (Gerontecnologia)

* **Tela Inicial com 6 Botões Gigantes:** Alvos de toque ampliados (mínimo de 80px de altura), ícones universais e cores de altíssimo contraste (WCAG AAA).
* **Zero Gestos Complexos:** Nenhuma ação requer movimentos de pinça ou arrastar (swipe). Tudo funciona através de toques simples e diretos.
* **Duplo Feedback Imediato:**
  * **Vibração Tátil:** O celular vibra levemente (40ms) ao tocar em qualquer botão.
  * **Confirmação Sonora & Voz:** Chime auditivo sintetizado e narração em voz alta em português brasileiro (`pt-BR`) pausada e compreensível.
* **Barra de Fuga Segura:** Botão fixo no rodapé de todas as telas internas: `⬅ VOLTAR AO INÍCIO`.
* **Controle de Letras:** Botão `🔤 Letra: A+` no topo para alternar instantaneamente entre fontes Normal, Grande e Gigante.

---

## 📱 Os 6 Módulos Integrados

1. **🌐 Como Mexer na Internet:**
   * **Vídeos Didáticos Realistas em HD:**
     * Personagens acolhedores, empáticos e fotorrealistas em formato 16:9 widescreen: **Dona Maria** (vovó afetuosa de óculos elegantes), **Seu José** (vovô de boina clássica e olhar sábio) e o neto **Pedrinho** (jovem paciente e atencioso).
     * **Tela Panorâmica Limpa:** Imagens 100% desobstruídas com efeito cinematográfico Ken Burns, sem ícones, identificadores de cenas ou tags cobrindo os rostos e mãos dos personagens.
     * **Voz Humana de Estúdio (Francisca Neural):** Narração acolhedora, natural e sem efeito robótico (`pt-BR-FranciscaNeural`), com sincronização orientada a eventos (`audio.onended`) e pausas de 1,2s para assimilação tranquila pelo idoso.
     * Player com controles ampliados (Assistir, Pausar, Repetir), barra de progresso em tempo real e legendas amarelas de alto contraste abaixo do vídeo:
       * *Vídeo 1:* Dona Maria aprendendo a tocar com leveza sem medo de quebrar o aparelho.
       * *Vídeo 2:* Seu José conectando no Wi-Fi de casa sem gastar os créditos do chip.
       * *Vídeo 3:* Dona Maria pesquisando receitas no Google falando pelo microfone.
       * *Vídeo 4:* Dona Maria mandando mensagem de voz para o Pedrinho e os dois risquinhos azuis (`✔✔`).
       * *Vídeo 5:* O Seu José desconfiando de mensagem suspeita, ligando para o filho real e ativando o escudo protetor antigolpe.
     * Treino prático e Quiz interativo logo abaixo de cada vídeo.

2. **💬 WhatsApp Descomplicado:**
   * Vídeo-guia passo a passo com legendas e narração (áudio, foto, chamada de vídeo e texto).
   * Botão de lançamento rápido (`whatsapp://`) para abrir o WhatsApp no celular com 1 toque.

3. **🏦 Treino de Banco Seguro (Sandbox sem Risco):**
   * Ambiente 100% simulado com saldo fictício (R$ 1.500,00) sem dinheiro real.
   * **Digitação Real do Valor Desejado:**
     * **Teclado Numérico Gigante na Tela** adaptado para idosos (teclas 0 a 9, Apagar e Limpar) com retorno sonoro e leitura em voz alta do valor digitado em tempo real.
     * Suporte automático para digitação em teclados físicos no computador (0-9, Backspace, Enter).
   * Tela obrigatória de revisão de segurança com confirmação do nome e comprovante fictício.
   * Extrato claro (Verde = entrou / Vermelho = saiu).
   * Laboratório Antigolpe (falso funcionário do banco, Pix errado e nomes trocados).

4. **💊 Meus Remédios e Horários (Medisafe):**
   * Instruções didáticas dos recursos do aplicativo (som de chocalho, botão "TOMEI", soneca e cuidador amigo).
   * Atalho direto para abrir o Medisafe no smartphone ou baixar na Google Play Store.

5. **📞 Telefone e Chamadas Rápidas:**
   * Botões de emergência de 1 toque: SAMU 192, Polícia Militar 190 e Bombeiros 193.
   * Grade de favoritos com fotos grandes dos filhos e netos para ligar direto.
   * **Simulador de Chamada Recebida:** O celular toca para o idoso praticar o ato de atender com calma.
   * Atalho para o discador nativo com teclas ampliadas.

6. **📍 Como Chegar e Rotas (Google Maps):**
   * Explicação didática de que a **bolinha azul** representa onde o idoso está agora.
   * Instruções de busca por voz e seleção de rotas (A pé, Ônibus ou Carro).
   * Atalho direto para abrir o Google Maps e botões rápidos ("Farmácia perto", "Posto de saúde").

---

## 🚀 Como Iniciar a Plataforma

### Pelo Windows (Atalho na Área de Trabalho):
1. Dê um duplo clique no atalho da Área de Trabalho: **`Iniciar_Avos_Online.bat`**
2. O sistema abrirá automaticamente o navegador em `http://127.0.0.1:8080`.

### Pelo Terminal / Linha de Comando:
```powershell
cd C:\Users\user\avos_online
python -m uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```

### Acesso no Celular via Wi-Fi:
* Conecte o celular na mesma rede Wi-Fi do computador e acesse `http://[IP-DO-COMPUTADOR]:8080`.
* No celular, toque no menu do navegador e selecione **"Adicionar à Tela Inicial"** para instalar como um aplicativo nativo (PWA)!
