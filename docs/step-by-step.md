# Documentação do processo

## Uso de Docker desde o Início
Ao iniciar este projeto, optei por adotar uma abordagem Dockerizada desde o princípio, visando proporcionar um ambiente de desenvolvimento consistente e facilmente replicável. Para isso, desenvolvi a aplicação utilizando um contêiner Docker dedicado para a API, o qual já possui um volume compartilhado previamente configurado no arquivo docker-compose.yaml.

Na ocasião, não possuía o Python instalado localmente em minha máquina, o que motivou a escolha de salvar as dependências do projeto em um arquivo requirements.txt. Vale ressaltar que essa decisão foi tomada devido à circunstância específica, e que uma abordagem mais convencional envolveria o uso de ambientes virtuais (venv) ou ferramentas modernas como o Poetry. Essas alternativas oferecem métodos automáticos e eficazes para gerenciar as dependências do projeto, tornando o desenvolvimento mais ágil e organizado.

## ROAD MAP

1. **API de Gerenciamento de Usuários**
   - ✅❌ CRUD User
   - ✅❌ Autenticação baseada em tokens (JWT) 
   - ✅❌ Permissões de Usuário (admin, usuário regular)

2. **Integração com Banco de Dados**
   - ✅❌ SQLAlchemy como ORM
   - ✅❌ Integração com PostgreSQL
   - ✅❌ Migrações de Banco de Dados com Alembic

3. **Documentação da API**
   - ✅❌ Utilização do Swagger
   - ✅❌ Documentação de Endpoints e Modelos
   - ✅❌ Exemplos de Requisições e Respostas

4. **Dockerização da Aplicação**
   - ✅ Dockerfile fornecido
   - ✅ docker-compose fornecido
   - ✅❌ Orquestração eficiente da aplicação e banco de dados

5. **Tarefa Assíncrona com Celery e RabbitMQ**
   - ❌ Tarefa assíncrona para enviar e-mails
   - ❌ Utilização do Celery como framework
   - ❌ RabbitMQ como broker de mensagens

6. **Logs e Monitoramento**
   - ❌ Sistema de logging integrado (ELK stack ou Graylog)
   - ❌ Métricas e monitoramento com Prometheus e Grafana