import pytest
from src.main import create_app # Importe create_app em vez de app diretamente
import json

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    """Testa se a página inicial responde com sucesso (200)"""
    response = client.get('/')
    assert response.status_code == 200

def test_home_json_structure(client):
    """Testa se a resposta é um JSON válido e tem as chaves certas"""
    response = client.get('/')
    dados = response.get_json()
    
    assert "mensagem" in dados
    assert "tecnologia" in dados
    assert dados["status"] == "online"
    assert "data_hora" in dados

def test_ia_status_endpoint(client):
    """Testa a rota /ia/status"""
    response = client.get('/ia/status')
    dados = response.get_json()
    assert response.status_code == 200
    assert dados["modelo"] == "Gemini-Pro-Simulado"
    assert dados["estado"] == "pronto"

def test_ia_gerar_endpoint_default(client):
    """Testa a rota /ia/gerar com prompt padrão"""
    response = client.post(
        '/ia/gerar',
        data=json.dumps({}),
        content_type='application/json'
    )
    dados = response.get_json()
    assert response.status_code == 200
    assert "Simulação de resposta do Gemini para: 'Gere um breve parágrafo sobre a importância da IA na educação.'" in dados["resultado"]
    assert dados["modelo"] == "Gemini-Pro-Simulado"

def test_ia_gerar_endpoint_custom_prompt(client):
    """Testa a rota /ia/gerar com prompt personalizado"""
    custom_prompt = "Explique a computação em nuvem de forma simples."
    response = client.post(
        '/ia/gerar',
        data=json.dumps({"prompt": custom_prompt}),
        content_type='application/json'
    )
    dados = response.get_json()
    assert response.status_code == 200
    assert f"Simulação de resposta do Gemini para: '{custom_prompt}'" in dados["resultado"]
    assert dados["modelo"] == "Gemini-Pro-Simulado"
