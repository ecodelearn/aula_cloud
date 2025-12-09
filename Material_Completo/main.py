from flask import Flask, jsonify, request, send_from_directory # Importe send_from_directory
import os
import datetime

# Definimos onde estão os arquivos estáticos
STATIC_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__, static_folder=STATIC_DIR, static_url_path='') # Configura para servir da raiz

@app.route("/")
def serve_index():
    """
    Rota principal que serve o arquivo index.html.
    """
    return send_from_directory(STATIC_DIR, 'index.html')

# Rota para servir CSS, JS e outros arquivos estáticos diretamente da raiz
@app.route("/<path:filename>")
def serve_static(filename):
    """
    Serve arquivos estáticos (CSS, JS, etc.) diretamente da raiz.
    """
    # Evita que a Flask tente servir o index.html novamente para /
    if filename == 'index.html':
        return serve_index()
    return send_from_directory(STATIC_DIR, filename)

@app.route("/api/saudacao") # Rota da API renomeada para evitar conflito com '/'
def home():
    """
    Rota da API que retorna saudação e metadados.
    """
    return jsonify({
        "mensagem": "Olá, Turma de IA Aplicada! Este é o backend da sua API.",
        "status": "online",
        "tecnologia": "Python + Flask + Google Cloud Run",
        "data_hora": datetime.datetime.now().isoformat()
    })

@app.route("/ia/status")
def ia_status():
    """
    Simula um endpoint de verificação de um modelo de IA.
    """
    return jsonify({
        "modelo": "Gemini-Pro-Simulado",
        "estado": "pronto",
        "latencia_ms": 45
    })

@app.route("/ia/gerar", methods=["POST"])
def ia_gerar():
    """
    Endpoint que simula a interação com um modelo Gemini-Pro.
    Inclui um exemplo COMENTADO de como integrar o SDK real.
    """
    # Exemplo COMENTADO de como integrar com o Google Generative AI SDK
    # Para usar, você precisaria instalar a biblioteca:
    # uv add google-generativeai
    #
    # e configurar sua API Key (NÃO coloque a chave aqui diretamente! Use variáveis de ambiente):
    # import google.generativeai as genai
    # try:
    #     genai.configure(api_key=os.environ.get("GENAI_API_KEY"))
    #     model = genai.GenerativeModel('gemini-pro')
    #     
    #     prompt = request.json.get("prompt", "Gere um breve parágrafo sobre a importância da IA na educação.")
    #     response = model.generate_content(prompt)
    #     
    #     return jsonify({
    #         "resultado": response.text,
    #         "modelo": "Gemini-Pro-REAL",
    #         "status": "sucesso"
    #     }), 200
    # except Exception as e:
    #     return jsonify({
    #         "erro": str(e),
    #         "modelo": "Gemini-Pro-REAL",
    #         "status": "falha",
    #         "detalhes": "Certifique-se de que GENAI_API_KEY está configurada e o modelo está disponível."
    #     }), 500

    # Simulação para a aula:
    data = request.get_json()
    prompt = data.get("prompt", "Gere um breve parágrafo sobre a importância da IA na educação.")
    simulated_response = f"Simulação de resposta do Gemini para: '{prompt}'. A IA está revolucionando a educação, personalizando o aprendizado e otimizando processos."
    
    return jsonify({
        "resultado": simulated_response,
        "modelo": "Gemini-Pro-Simulado",
        "status": "sucesso",
        "nota": "Descomente o código acima e configure sua GENAI_API_KEY para usar o Gemini real!"
    }), 200

def create_app():
    return app

if __name__ == "__main__":
    # Pega a porta do ambiente (obrigatório para Cloud Run)
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
