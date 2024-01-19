# FastAPI User API Com Login e Permissões

Este projeto é uma solução para o Desafio FastAPI proposto pela Paneas. O objetivo é construir uma aplicação RESTful utilizando o framework FastAPI, com ênfase em práticas de desenvolvimento, escalabilidade, segurança e integração com outras tecnologias.

Leia o [Desafio FastAPI - Paneas](./docs/desafio_fastAPI_Paneas.md) para obter mais detalhes.

## Nivéis Implementados

4. **Dockerização da Aplicação**
   - ✅ Dockerfile fornecido
   - ✅ docker-compose fornecido

---

## Entrega

O código-fonte está disponível neste [repositório Git](https://github.com/tiagoGIM/fast-api-challenge-user). Siga as instruções abaixo para configurar e executar a aplicação.

Uma documentação detalhada e justificativa de abordagens de desenvolvimento estão disponíveis em um [passo a passo](./docs/step-by-step.md) que usei para registrar o desenvolvimento.

## Pré-requisitos 

Antes de iniciar a execução do projeto, certifique-se de ter as seguintes ferramentas instaladas:

- **Docker:** O projeto utiliza Docker para facilitar a execução em diferentes máquinas e também por ser um dos critérios do desafio.
    -- [Site Oficial para instalar o Docker](https://docs.docker.com/engine/install/)

### Configuração e Execução

1. Clone o repositório:
```bash
$ git clone https://github.com/tiagoGIM/fast-api-challenge-user
 ```


2. Navegue até o diretório do projeto:

```bash
 $ cd fast-api-challenge-user
```

3. Execute o Docker Compose:

```bash
 $ docker-compose up --build

```

O Docker Compose criará os contêineres necessários para a aplicação e o banco de dados PostgreSQL. Após a conclusão, a aplicação estará acessível em http://localhost:8000 e a documentação da API em http://localhost:8000/docs.


## Authors

- [@tiagoGIM](https://www.github.com/tiagoGIM)


## 🔗 Links

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tiaho-hs-almeida)



## License

[MIT](https://choosealicense.com/licenses/mit/)

