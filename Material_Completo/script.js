document.getElementById('fetchApiData').addEventListener('click', async () => {
    const apiOutput = document.getElementById('apiOutput');
    apiOutput.textContent = 'Buscando dados da API...';

    try {
        const response = await fetch('/api/saudacao'); // Rota da API Flask
        const data = await response.json();
        apiOutput.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        apiOutput.textContent = 'Erro ao buscar dados da API: ' + error.message;
        console.error('Erro ao buscar dados da API:', error);
    }
});