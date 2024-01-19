
Desafio FastAPI - Paneas

Objetivo: Construir uma aplicação RESTful usando FastAPI, com foco em práticas de desenvolvimento, escalabilidade, segurança e integração com outras tecnologias.

Tempo Estimado: 4 dias
Nota: Os itens obrigatórios são 1, 2 e 3.

Requisitos do Desafio:

1. API de Gerenciamento de Usuários:
   - Implementar endpoints para criar, ler, atualizar e deletar (CRUD) usuários.
   - Usar autenticação baseada em tokens (JWT).
   - Implementar permissões de usuário (admin, usuário regular).

2. Integração com Banco de Dados:
   - Usar SQLAlchemy como ORM.
   - Integrar com um banco de dados PostgreSQL.
   - Implementar migrações de banco de dados usando Alembic.

3. Documentação da API:
   - Utilizar o Swagger para documentar todos os endpoints e modelos.
   - Incluir exemplos de requisições e respostas.

4. Dockerização da Aplicação:
   - Criar um Dockerfile para a aplicação.
   - Escrever um docker-compose para orquestrar a aplicação e o banco de dados.

5. Tarefa Assíncrona com Celery e RabbitMQ:
   - Implementar uma tarefa assíncrona para enviar e-mails de confirmação de cadastro.
   - Usar Celery como framework de tarefas assíncronas e RabbitMQ como broker de mensagens.

6. Logs e Monitoramento:
   - Integrar um sistema de logging (como ELK stack ou Graylog).
   - Implementar métricas e monitoramento com Prometheus e Grafana.

Critérios de Avaliação:

- Qualidade do Código: Clareza, organização, uso de padrões e boas práticas.
- Segurança: Implementação de medidas de segurança como sanitização de inputs, tratamento de erros e segurança de tokens.
- Performance: Otimização do código e uso eficiente de recursos.
- Completo e Funcional: Todos os requisitos devem estar implementados e funcionando como esperado.
- Documentação: Clareza e completude da documentação.

Entrega:

- O código deve ser disponibilizado em um repositório Git (público ou privado).
- Incluir um README detalhado com instruções para configurar e rodar a aplicação.

Faça o máximo que conseguir e boa sorte!
