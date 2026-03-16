# 🚀 Automação de Rotina Diária e Agendamento

Este projeto é um script em Python desenvolvido para automatizar o início da rotina de trabalho e estudos. Ele une automação web (para abrir abas e fazer login em múltiplas plataformas essenciais) e comandos de sistema (para agendar o desligamento automático do computador).

O objetivo é economizar tempo todos os dias, executando tarefas repetitivas com um único clique!

---

## 🛠️ Funcionalidades

1.  **Agendamento Automático de Desligamento:** Calcula o tempo exato e agenda o desligamento silencioso do PC para um horário específico (ex: 14h28). Inclui um alerta visual na tela confirmando o agendamento.
2.  **Abertura Limpa do Navegador:** Inicia o Google Chrome no modo anônimo e escuro (Dark Mode), ignorando banners de automação para evitar detecções.
3.  **Logins Sequenciais Automatizados:**
    * **Google / Gmail:** Preenche e-mail e senha e acessa a caixa de entrada.
    * **Google Gemini:** Abre em uma nova aba e aguarda o carregamento.
    * **GitHub:** Navega até a página de login, insere as credenciais e acessa a dashboard principal.
    * **Portal do Estudante SENAI:** Abre a página do aluno para login (Aviso: O preenchimento automático desta página está em desenvolvimento ainda).
4.  **Aba Final de Pesquisa:** Deixa uma aba extra aberta no Google, pronta para começar o trabalho.

---

## 💻 Pré-requisitos e Instalação

Para rodar este projeto na sua máquina, você precisará ter o **Python** e o **Google Chrome** instalados.

1. Baixe ou clone este projeto para o seu computador.
2. Abra o terminal (ou prompt de comando) na pasta do projeto.
3. Instale as bibliotecas necessárias executando o comando abaixo:

    ```bash
    pip install selenium webdriver-manager pyautogui
    ```

---

## 🔐 Tutorial: Configurando suas Credenciais (IMPORTANTE)

Para que o robô consiga fazer os logins por você, ele precisa saber os seus e-mails e senhas. No entanto, **NUNCA devemos colocar senhas diretamente no código principal (`main.py`)**. 

Para manter suas contas seguras, usamos um arquivo separado chamado `Credentials.py`. Siga o passo a passo abaixo para configurá-lo:

### Passo 1: Criar o arquivo
Na mesma pasta onde está o seu script principal de automação, crie um novo arquivo de texto e nomeie-o exatamente como: `Credentials.py`

### Passo 2: Copiar o modelo
Abra o arquivo `Credentials.py` que você acabou de criar e cole o código abaixo dentro dele:

    ```python
    # Credenciais do Google
    email = "SEU_EMAIL_AQUI@gmail.com"
    password = "SUA_SENHA_DO_GOOGLE_AQUI"

    # Credenciais do GitHub
    github_email = "SEU_USUARIO_OU_EMAIL_DO_GITHUB"
    github_password = "SUA_SENHA_DO_GITHUB_AQUI"

    # Credenciais do SENAI
    senai_user = "SEU_CPF_OU_EMAIL_AQUI"
    senai_password = "SUA_SENHA_DO_SENAI_AQUI"
    ```

### Passo 3: Preencher com seus dados reais
Substitua os textos genéricos (como `"SEU_EMAIL_AQUI@gmail.com"`) pelos seus dados verdadeiros. 
**Atenção:** Mantenha as aspas duplas (`" "`) ao redor dos seus e-mails e senhas!

### Passo 4: Proteja o arquivo (Aviso sobre o GitHub)
Se você for subir este projeto para o GitHub ou qualquer outro controle de versão, **você deve ignorar o arquivo de credenciais**. 
Crie um arquivo chamado `.gitignore` na mesma pasta e escreva dentro dele apenas:
    
    Credentials.py

Isso garante que o GitHub ignore o arquivo com as suas senhas e suba apenas o código do robô.

---

## ▶️ Como Executar o Projeto

Com as bibliotecas instaladas e o arquivo `Credentials.py` configurado, você está pronto para rodar!

Abra o seu terminal na pasta do projeto e execute o script principal (substitua `nome_do_arquivo.py` pelo nome real do seu script):

    ```bash
    python nome_do_arquivo.py
    ```

**O que vai acontecer:**
1. Um pop-up aparecerá confirmando em quantos segundos o seu PC será desligado.
2. O Google Chrome abrirá sozinho no modo anônimo.
3. Não mexa no mouse ou teclado enquanto o robô estiver trabalhando.
4. Ao final, você terá todas as suas abas logadas e prontas para o uso!