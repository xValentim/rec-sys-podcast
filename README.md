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

Para fazer uma consulta à API, você pode usar o seguinte comando cURL:

```bash
curl -X POST http://localhost:1414/query -d '{"query": "como estudar renda fixa?"}'
```

### Playlists utilizadas