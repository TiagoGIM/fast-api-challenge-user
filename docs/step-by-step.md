# Documentação do processo

## Uso de Docker desde o Início
Ao iniciar este projeto, optei por adotar uma abordagem Dockerizada desde o princípio, visando proporcionar um ambiente de desenvolvimento consistente e facilmente replicável. Para isso, desenvolvi a aplicação utilizando um contêiner Docker dedicado para a API, o qual já possui um volume compartilhado previamente configurado no arquivo docker-compose.yaml.

Na ocasião, não possuía o Python instalado localmente em minha máquina, o que motivou a escolha de salvar as dependências do projeto em um arquivo requirements.txt. Vale ressaltar que essa decisão foi tomada devido à circunstância específica, e que uma abordagem mais convencional envolveria o uso de ambientes virtuais (venv) ou ferramentas modernas como o Poetry. Essas alternativas oferecem métodos automáticos e eficazes para gerenciar as dependências do projeto, tornando o desenvolvimento mais ágil e organizado.

## Padrão do Projeto
Para garantir uma estrutura organizada e aderente às melhores práticas, o projeto adota o padrão de arquitetura MVC (Model-View-Controller), com um foco especial no domain **user** e **authentication**. Aqui estão algumas decisões arquiteturais adotadas:

### Estrutura do Projeto
- Repository Pattern: Implementamos o padrão repository para lidar com a persistência de dados, proporcionando um desacoplamento eficaz entre a lógica de negócios e o acesso aos dados.
Segregação em Camadas: Dividimos o projeto em camadas distintas, como service, route e models. Isso facilita a manutenção, teste e compreensão do código.
### Práticas MVC
- Entities e DTOs: As entidades e DTOs (Data Transfer Objects) ficarão em ***_schemas.py**. Aqui, definimos nossos modelos de dados e objetos de transferência de dados para interação com a API.
Service Layer: A camada de serviço (service) contém a lógica de negócios, manipulação de dados e regras de aplicação específicas do domínio.
Rotas (Routes): As rotas da API estão em ***_route.py**, garantindo uma separação clara entre a manipulação de solicitações HTTP e a lógica de negócios.

### SOLID
- Desacoplamento e SOLID: Embora Python não seja uma linguagem estritamente orientada a objetos, busquei promover o desacoplamento e seguir princípios do SOLID sempre que possível.

## Testes 
Criei um docker para testar a aplicaçao com pytest e pytest-cov, esse docker foi adicionado ao meu workflow e com isso a cada merge ou commit a esteira de testes executa uma rotina de testes no repositorio.

## Permissões 
Para a gestão de permissões, adotei uma estratégia simples baseada no token de sessão e na função (role) do usuário. Obtive inspiração a partir deste -> [artigo](https://dev.to/moadennagi/role-based-access-control-using-fastapi-h59).


## ROAD MAP

1. **API de Gerenciamento de Usuários**
   - ✅ CRUD User
   - ✅ Autenticação baseada em tokens (JWT) 
   - ✅ Permissões de Usuário (admin, usuário regular)

2. **Integração com Banco de Dados**
   - ✅ SQLAlchemy como ORM
   - ✅ Integração com PostgreSQL
   - ✅ Migrações de Banco de Dados com Alembic

3. **Documentação da API**
   - ✅ Utilização do Swagger
   - ✅ Documentação de Endpoints e Modelos
   - ✅ Exemplos de Requisições e Respostas

4. **Dockerização da Aplicação**
   - ✅ Dockerfile fornecido
   - ✅ docker-compose fornecido
   - ✅ Orquestração eficiente da aplicação e banco de dados

5. **Tarefa Assíncrona com Celery e RabbitMQ**
   - ❌ Tarefa assíncrona para enviar e-mails
   - ❌ Utilização do Celery como framework
   - ❌ RabbitMQ como broker de mensagens

6. **Logs e Monitoramento**
   - ❌ Sistema de logging integrado (ELK stack ou Graylog)
   - ❌ Métricas e monitoramento com Prometheus e Grafana