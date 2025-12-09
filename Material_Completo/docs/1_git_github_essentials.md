# 🐙 Git e GitHub: A Máquina do Tempo do Seu Código

**Objetivo:** Dominar o controle de versão para trabalhar em equipe e salvar seu progresso.
**Público:** Estudantes de IA Aplicada e Desenvolvedores.

---

## 1. O Conceito (Sem "Tecnês")

Imagine que você está escrevendo um livro.
*   **Git:** É o sistema que salva o histórico de cada página que você escreve ("Capítulo 1 - versão final", "Capítulo 1 - revisão 2"). Ele permite que você "volte no tempo" se apagar algo sem querer. Isso roda **no seu computador**.
*   **GitHub:** É como o Google Drive para esse seu livro. É onde você guarda a cópia na nuvem para não perder se seu PC quebrar, e onde outras pessoas podem ler e sugerir correções.

---

## 2. Configuração Inicial (Faça uma única vez)

Antes de começar, precisamos conectar seu terminal à sua conta do GitHub. Faremos isso de forma simples usando o `gh` (GitHub CLI).

**Passo 1: Autenticar (O Pulo do Gato)**
No seu terminal (Git Bash ou VS Code), rode:

```bash
gh auth login
```
*(Siga as instruções na tela: GitHub.com -> HTTPS -> Yes -> Login with a web browser)*

**Passo 2: Identificação no Histórico**
Diga ao Git quem é você para os registros locais:

```bash
# Diga ao Git quem é você (Use o mesmo nome/email do seu GitHub)
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu.email@exemplo.com"

# Define a branch principal como 'main' (padrão moderno)
git config --global init.defaultBranch main
```

---

## 3. O Fluxo de Trabalho (Workflow)

Este é o ciclo que você repetirá centenas de vezes. Decore-o!

### Passo 1: Iniciar (Start)
Transforma uma pasta comum em um repositório Git.
```bash
cd projeto-aula-cloud
git init
```

### Passo 2: O Palco (Staging)
O Git não salva tudo automaticamente. Você precisa escolher o que vai para a "foto" (commit).
```bash
# Adiciona um arquivo específico
git add main.py

# OU adiciona TUDO que mudou (mais comum)
git add .
```

### Passo 3: O Click (Commit)
Aqui você tira a "foto" e salva no histórico.
```bash
git commit -m "Adiciona função de saudação da IA"
```
*Dica:* A mensagem entre aspas deve explicar **o que** você fez.

### Passo 4: Enviar para Nuvem (Push)
Envia suas alterações locais para o GitHub.
```bash
# Na primeira vez, você conecta o repositório remoto:
git remote add origin https://github.com/SEU_USUARIO/NOME_DO_REPO.git

# Envia os arquivos
git push -u origin main
```

---

## 4. Branching: Universos Paralelos

Nunca mexa no código principal (`main`) diretamente se estiver testando algo arriscado. Crie um universo paralelo (`branch`).

```bash
# 1. Cria e entra numa nova branch chamada 'nova-feature-ia'
git checkout -b nova-feature-ia

# 2. ... (Você faz alterações, edita arquivos, quebra coisas) ...

# 3. Salva no seu universo paralelo
git add .
git commit -m "Testando novo modelo de IA"

# 4. Volta para o universo principal (main)
git checkout main
# (Note que seus arquivos voltaram a ser como eram antes!)

# 5. Traz as alterações da branch para a main (Merge)
git merge nova-feature-ia
```

---

## 5. Cheat Sheet (Resumão)

| Comando | O que faz? | Tradução Livre |
| :--- | :--- | :--- |
| `git status` | Mostra o estado atual | "O que eu mudei e não salvei?" |
| `git log` | Mostra o histórico | "Deixa eu ver minha linha do tempo." |
| `git clone <url>` | Baixa um projeto | "Baixar esse projeto para meu PC." |
| `git pull` | Atualiza seu PC | "Baixar as novidades da nuvem." |
| `git diff` | Mostra diferenças | "O que mudou exatamente neste arquivo?" |