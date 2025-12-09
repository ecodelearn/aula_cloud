# 🐍 Python Moderno: Ambientes Virtuais com UV

**Objetivo:** Criar ambientes de desenvolvimento isolados, rápidos e profissionais.
**Ferramenta:** `uv` (Sucessor ultrarrápido do pip).

---

## 1. O Problema dos Ambientes
Imagine que você tem dois projetos:
*   **Projeto A:** Usa uma IA antiga que precisa do `pandas` versão 1.0.
*   **Projeto B:** Usa uma IA nova que precisa do `pandas` versão 2.0.

Se você instalar tudo no seu computador principal, um projeto vai quebrar o outro.
**Solução:** Criamos "caixas" isoladas para cada projeto. Chamamos isso de **Virtual Environment (venv)**.

---

## 2. Por que UV?
Antigamente, usávamos `pip` e `venv`. Era lento e confuso.
O **UV** é uma ferramenta moderna (escrita em Rust) que faz tudo isso instantaneamente.

**Instalação do UV:**
```bash
# Mac / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

---

## 3. Iniciando um Projeto

Esqueça `python -m venv ...`. Com UV é assim:

### Passo 1: Inicializar
Na pasta do seu projeto:
```bash
uv init
```
Isso cria um arquivo `pyproject.toml`. Ele é a "receita do bolo" do seu projeto.

### Passo 2: Criar o Ambiente Virtual
```bash
uv venv
```
Isso cria a pasta `.venv` (a caixa isolada). O UV baixa o Python automaticamente se precisar!

### Passo 3: Adicionar Bibliotecas
Não use `pip install`. Use `uv add`. Ele atualiza sua receita (`pyproject.toml`) automaticamente.
```bash
uv add flask gunicorn
uv add pytest --dev  # Adiciona como dependência apenas de desenvolvimento/teste
```

---

## 4. Rodando seu Código

Para rodar o código usando as bibliotecas da "caixa" isolada, coloque `uv run` antes do comando.

```bash
# Rodar seu script (na raiz do projeto)
uv run main.py

# Rodar testes
uv run pytest
```

---

## 5. Resumo para a Aula

1.  Crie a pasta: `mkdir projeto-aula-cloud`
2.  Entre nela: `cd projeto-aula-cloud`
3.  Inicie o UV: `uv init`
4.  Instale Flask: `uv add flask`
5.  Crie seu código (`main.py` na raiz).
6.  Rode: `uv run main.py`

Simples assim. Sem conflitos de versão, sem dor de cabeça.