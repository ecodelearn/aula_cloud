# 🚀 Ciclo de Vida: Do Código à Nuvem

**Objetivo:** Entender o fluxo completo de um engenheiro de software de IA.

---

## O Ciclo D.T.D. (Desenvolver, Testar, Deploy)

Não escrevemos código direto na produção. Seguimos um ritual para garantir qualidade.

### FASE 1: Desenvolvimento (Local) 🏠
É onde você cria. Seu laboratório pessoal.
*   **Onde:** No VS Code, rodando com `uv`.
*   **Comando:** `uv run main.py`
*   **Status:** "Funciona na minha máquina".

### FASE 2: Verificação (Testes) 🕵️
Antes de mostrar para o mundo, verificamos se não há erros óbvios.
*   **Testes Automatizados:** O computador testa seu código por você.
*   **Linting:** O computador verifica se seu código está "bonito" e organizado.
*   **Comando:**
    ```bash
    uv run ruff check .  # Verifica estilo
    uv run pytest        # Roda os testes lógicos
    ```

### FASE 3: Deploy (Nuvem) ☁️
O momento da verdade. Enviamos para o Google Cloud.

*   **Onde:** No **Google Cloud Shell** (disponível no Google Cloud Skills Boost ou no console GCP).
*   **Requisito:** O projeto deve ter um arquivo `requirements.txt` (O Google Cloud ainda não usa `uv` nativamente por padrão em todos os builders, então geramos um para compatibilidade).

**Passo 0: Configurar o Projeto (Evite erros de permissão!)**
Antes de fazer o deploy, garanta que o terminal sabe onde guardar seu site.

> **⚠️ ATENÇÃO:**
> *   **Se você está no Skills Boost:** NÃO crie um projeto novo! O laboratório já te dá um projeto pronto (com ID tipo `qwiklabs-gcp-...`). Use esse ID no comando de seleção abaixo. O faturamento já está pago pelo Google.
> *   **Se você está na sua conta pessoal:** Você precisará ativar o "Faturamento" (Billing) no console do Google Cloud adicionando um cartão de crédito, senão os serviços não ativarão.

1.  **Crie um projeto (APENAS se estiver na conta pessoal e não tiver um):**
    ```bash
    # O ID do projeto deve ser único no mundo todo!
    gcloud projects create projeto-aula-cloud-SEUNOME
    ```
    *(Substitua `SEUNOME` por algo único, ex: `projeto-aula-cloud-daniel`)*

2.  **Selecione o projeto:**
    ```bash
    # No Skills Boost, pegue o ID do projeto na lateral esquerda da tela do laboratório
    gcloud config set project ID_DO_PROJETO_AQUI
    ```

**Passo 1: Preparar Dependências**
Exportando dependências do UV para o padrão antigo:
```bash
uv pip compile pyproject.toml -o requirements.txt
```

**Passo 2: Enviar para o Google**
(dentro do Cloud Shell):
```bash
gcloud run deploy projeto-aula-cloud --source . --allow-unauthenticated
```


---

## Check-list Final da Aula

- [ ] Código rodando local com `uv run`.
- [ ] Testes passando (`pytest` verde).
- [ ] Código salvo no GitHub (`git push`).
- [ ] `requirements.txt` gerado.
- [ ] `gcloud run deploy` executado com sucesso.
- [ ] URL pública acessada pelo celular! 📱