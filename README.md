Desafio ray

Como rodar:
Necessario que crie um ambiente virtual python ative-o e instale as dependencias corretas com o comando "pip freeze > requirements.txt", então adicionar uma chave de api validade para o YouTube Data API v3 usando um arquivo .env, ou atribuindo valor diretamente no aquivo youtube_API.py

Decisões técnicas:
Primeiramente foi visado uma plotagem que mostrasse o crescimento ou declinio das estatisticas ao longo do tempo. Foi descartado a opção de uma series temporal sem tratamento especifico, assim sendo optou-se por um grafico de media movel, para mais facil compreensao.

Então tentou-se achar correlações entre as variasveis (data, vizualizações, curtidas, comentarios e duração dos videos), afim de um insgth importante, infelizmente nenhma correlação foi satisfatoria.

Com isso surgiu a ideia de analisar uma forma de mediar os videos com mais impacto, então foi usada a metrica de engajamento (curtidas + numero de comnetarios / vizualizações). Assim sendo possivel destacar os videos com mais engajamento

Recursos:
python 3.12.4
Dash 2.18.2
Pandas 2.2.3
googleapiclient
