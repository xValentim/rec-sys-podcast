# 🚀API de Recomendação de Vídeos no YouTube

## 🔎Contexto Geral

Esta API foi desenvolvida para fornecer recomendações de trechos relevantes de vídeos baseadas em queries fornecidas pelos usuários. Utilizando playlists do YouTube, o sistema analisa o conteúdo dos vídeos para sugerir partes que mais se alinham com os interesses do usuário. Este serviço é ideal para quem busca informações específicas dentro de grandes quantidades de conteúdo em vídeo, economizando tempo e aumentando a eficácia da busca por conhecimento ou entretenimento.

## 📈Técnicas Utilizadas

A API emprega a técnica de TF-IDF (Term Frequency-Inverse Document Frequency) para analisar a relevância de um segmento de texto em relação a uma query específica. Esta abordagem ajuda a identificar as partes mais pertinentes dos vídeos ao calcular a importância de uma palavra dentro de um vídeo em relação à sua frequência nos demais vídeos da playlist. Essa metodologia é amplamente usada em sistemas de recuperação de informações para destacar termos significativos em grandes conjuntos de dados textuais.

## 💡Uso da API do YouTube

A integração com a API do YouTube permite que nossa aplicação acesse diretamente as playlists e extraia os dados necessários dos vídeos, como transcrições e metadados. Isso é essencial para processar e analisar o conteúdo dos vídeos a fim de fazer as recomendações. 

## 📜Construção do Dataset

(Doing)

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

Para fazer uma consulta à API, você pode usar o seguinte comando cURL:

```bash
curl -X POST http://localhost:1414/query -d '{"query": "como estudar renda fixa?"}'
```

### Playlists utilizadas