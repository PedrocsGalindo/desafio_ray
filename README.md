# Desafio Ray

## Visão Geral

 O objetivo é explorar os dados dos vídeos de highlights das corridas de Fórmula 1 de 2024 e apresentar insights relevantes através de uma visualização interativa.

---

## Como Rodar

1. **Criação do Ambiente Virtual:**
   - Certifique-se de ter o Python 3.12.4 instalado.
   - Crie um ambiente virtual:
     ```bash
     python -m venv venv
     ```
   - Ative o ambiente virtual:
     - Windows: `venv\Scripts\activate`
     - Unix/Mac: `source venv/bin/activate`

2. **Instalação das Dependências:**
   - Instale os pacotes necessários:
     ```bash
     pip install -r requirements.txt
     ```

3. **Configuração da API:**
   - Obtenha uma chave válida para a YouTube Data API v3 no [Google Cloud Console](https://console.cloud.google.com/).
   - Configure a chave de API:
     - Crie um arquivo `.env` na raiz do projeto com a linha:
       ```env
       API_KEY=SUA_CHAVE_DE_API
       ```
     - Alternativamente, atribua diretamente no arquivo `youtube_API.py`.

4. **Execução do Projeto:**
   - Execute o script principal para iniciar o dashboard:
     ```bash
     python app.py
     ```
   - Acesse o link que aparece no teminal

---

## Decisões Técnicas

1. **Plotagem de Crescimento:**
   - Focou-se em uma visualização que demonstrasse a tendência de crescimento ou declínio das estatísticas ao longo do tempo.
   - Optou-se por gráficos de média móvel para facilitar a compreensão, descartando séries temporais não tratadas.

2. **Análise de Correlações:**
   - Buscou-se identificar correlações entre variáveis (data, visualizações, curtidas, comentários e duração dos vídeos).
   - Nenhuma correlação significativa foi encontrada, o que redirecionou o foco da análise.

3. **Métrica de Engajamento:**
   - Desenvolve-se uma métrica para identificar os vídeos mais impactantes:
     Engajamento = (Curtidas + Comentários) / Visualizações
   - Essa abordagem destacou os vídeos com maior engajamento.

---

## Recursos Utilizados

- **Linguagem de Programação:**
  - Python 3.12.4
- **Bibliotecas Principais:**
  - Dash 2.18.2
  - Pandas 2.2.3
  - googleapiclient
- **Ferramentas Adicionais:**
  - API do YouTube Data v3

---

## Maiores Desafios

1. **Criação de Métricas Relevantes:**
   - Identificar formas de medir impacto e engajamento sem correlações diretas.
2. **Storytelling Visual:**
   - Construir gráficos intuitivos e impactantes que transmitissem informações relevantes.

---

