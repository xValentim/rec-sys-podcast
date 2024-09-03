# 🚀API de Recomendação de Vídeos no YouTube

## 🔎Contexto Geral

Esta API foi desenvolvida para fornecer recomendações de trechos relevantes de vídeos baseadas em queries fornecidas pelos usuários. Utilizando playlists do YouTube, o sistema analisa o conteúdo dos vídeos para sugerir partes que mais se alinham com os interesses do usuário. Este serviço é ideal para quem busca informações específicas dentro de grandes quantidades de conteúdo em vídeo, economizando tempo e aumentando a eficácia da busca por conhecimento ou entretenimento.

## 📈Técnicas Utilizadas

A API emprega a técnica de TF-IDF (Term Frequency-Inverse Document Frequency) para analisar a relevância de um segmento de texto em relação a uma query específica. Esta abordagem ajuda a identificar as partes mais pertinentes dos vídeos ao calcular a importância de uma palavra dentro de um vídeo em relação à sua frequência nos demais vídeos da playlist. Essa metodologia é amplamente usada em sistemas de recuperação de informações para destacar termos significativos em grandes conjuntos de dados textuais.

## 💡Uso da API do YouTube

A integração com a API do YouTube permite que nossa aplicação acesse diretamente as playlists e extraia os dados necessários dos vídeos, como transcrições e metadados. Isso é essencial para processar e analisar o conteúdo dos vídeos a fim de fazer as recomendações. 

## 📜Construção do Dataset para Preparação do Vestibular (ENEM)

Este dataset é uma coleção de transcrições de vídeos sobre o vestibular, especificamente focado no Exame Nacional do Ensino Médio (ENEM). Com conteúdo derivado de mais de 300 vídeos, o dataset abrange uma ampla gama de disciplinas fundamentais como Física, Química, História e Biologia. Cada transcrição é extraída de vídeos educativos disponíveis no YouTube, garantindo uma fonte diversificada de explicação e ensino dos tópicos.

#### Importância do Dataset

1. **Acesso Ampliado a Recursos de Aprendizagem**: Este dataset democratiza o acesso a recursos de qualidade para estudantes que estão se preparando para o vestibular, especialmente aqueles com acesso limitado a cursos preparatórios ou tutoria privada. Ao disponibilizar transcrições de vídeos educativos, alunos de diferentes regiões e contextos socioeconômicos podem estudar e revisar os conteúdos programáticos do ENEM de maneira gratuita e acessível.

2. **Personalização do Aprendizado**: Através da API que recomenda vídeos baseados em queries específicas dos usuários, o dataset permite uma personalização do estudo. Estudantes podem buscar explicações e conteúdos específicos que atendam às suas necessidades e lacunas de aprendizado, tornando o estudo mais eficiente e direcionado.

3. **Preparação Abrangente**: Cobrindo uma ampla gama de disciplinas, o dataset oferece uma preparação abrangente, permitindo aos estudantes uma revisão completa dos tópicos que são frequentemente abordados no ENEM. Isso é crucial para uma preparação eficaz, considerando a variedade de temas que o exame abrange.

4. **Engajamento e Retenção de Conteúdo**: As transcrições dos vídeos promovem não apenas a leitura e revisão, mas também estimulam o aprendizado ativo. Os alunos podem interagir com o conteúdo de formas variadas, como anotações e discussões baseadas no texto, o que é conhecido por melhorar a retenção de informações e facilitar o entendimento profundo dos temas.

5. **Suporte a Educadores e Programas Educacionais**: Educadores e programas de tutoria podem utilizar este dataset como uma ferramenta adicional para enriquecer suas metodologias de ensino. Oferecer trechos relevantes de vídeos como material de apoio ou como ponto de partida para discussões em sala de aula pode ser extremamente benéfico.

## 🚢Dockerização

Para facilitar a execução da API, o projeto foi dockerizado. Para rodar a aplicação em um container Docker, siga os passos abaixo:

1. **Construção da Imagem**:
   Para construir a imagem Docker, utilize o comando:
   ```bash
   docker build -t rec-sys .
   ```

2. **Execução do Container**:
   Para rodar a aplicação em um container, utilize o comando:
   ```bash
   docker run -d -p 1414:1414 rec-sys
   ```
   Isso irá iniciar o container e mapear a porta 1414 do host para a porta 1414 do container.

3. **Acessando a API**:
   Acesse a API através do endereço `http://localhost:1414`.

## Como usar a API

### Endpoints

A API possui os seguintes endpoints:

- `/query`: Recebe uma query do usuário e retorna os trechos de vídeos recomendados.

### Exemplos de Consultas

Para realizar testes, você pode acompanhar o notebook `testes.ipynb` que contém exemplos de consultas à API. Lá também é testado a qualidade das recomendações feitas pela API. Foram elaborados 3 testes, cada um com uma query diferente:


#### 1. **Teste 1**: ``Query = Como é calculado o módulo de um vetor na física do movimento (mecânica)?`` 
> Retorna 10 documentos relevantes (Acima de 0.1 de relevance)
> Um dos vídeos relevantes retornados (Com um trecho específico) ["Física | ENEM - Estática I - Ponto Material | CURSO GRATUITO COMPLETO | CURSO GRATUITO COMPLETO"](https://www.youtube.com/watch?v=yAUa4kazVoE)

Você pode mandar um ``get`` para o endpoint `/query` com a query acima para testar a API.

```bash
curl -X GET "http://10.103.0.28:1414/query?input_content=Como%20%C3%A9%20calculado%20o%20m%C3%B3dulo%20de%20um%20vetor%20na%20f%C3%ADsica%20do%20movimento%20%28Mec%C3%A2nica%29"
```

#### 2. **Teste 2**: ``Query = Me explique sobre o tratado de versalhes.``
> Retorna 6 documentos relevantes (Acima de 0.1 de relevance)
> Um dos vídeos relevantes retornados (Com um trecho específico) ["HISTÓRIA GERAL #23 TRATADO DE VERSALHES"](https://www.youtube.com/watch?v=T-sajvY_F4Y)

Você pode mandar um ``get`` para o endpoint `/query` com a query acima para testar a API.

```bash
curl -X GET "http://10.103.0.28:1414/query?input_content=Me%20explique%20sobre%20o%20tratado%20de%20versalhes"
```

#### 3. **Teste 3**: ``Query = nem toda proteína é uma enzima claro que existe a sessão existem raríssima as enzimas que não são proteínas``
> Essa query é não trivial pois é um trecho específico de um vídeo, não é uma pergunta direta. Ele retornou o trecho exato de onde foi tirado.
> Um dos vídeos relevantes retornados (Com um trecho específico) ["PROTEÍNAS - COMPOSTOS ORGÂNICOS - BIOQUÍMICA | Biologia com Samuel Cunha"](https://www.youtube.com/watch?v=ryW0698xdyY)

Você pode mandar um ``get`` para o endpoint `/query` com a query acima para testar a API.

```bash
curl -X GET "http://10.103.0.28:1414/query?input_content=nem%20toda%20prote%C3%ADna%20%C3%A9%20uma%20enzima%20claro%20que%20existe%20a%20sess%C3%A3o%20existem%20rar%C3%ADssima%20as%20enzimas%20que%20n%C3%A3o%20s%C3%A3o%20prote%C3%ADnas"
```

Para mais detalhes sobre a execução dos testes, consulte o notebook `testes.ipynb`.

### Playlists utilizadas

Para consultar melhor a construção do dataset, vá na branch de experimentos e veja o notebook `get_dataset_ENEM.ipynb`. Lá é feita a extração das transcrições dos vídeos das playlists utilizadas, o local da definição das playlist se encontra no trecho seguinte:

```python
playlist_link_list = ['https://www.youtube.com/playlist?list=PLMra4G0-Z7pMYLE-D-ptnHt1IW_Y1hn8H', # Parabolica
                      'https://www.youtube.com/playlist?list=PL8vXuI6zmpdj_YFEHTaBDccdSCC1LVNH0', # Quimica Kultivi
                      'https://www.youtube.com/playlist?list=PL8vXuI6zmpdiG6QR-LpXXbUYzPz5rOhF2', # Fisica Kultivi
                      'https://www.youtube.com/playlist?list=PLufADJj3qLe9PlyOZVXTV-URSDEmKgHPy'] # Biologia Thaisefinish
```
