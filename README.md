# API Node.js com swagger documentação

Esta é uma API Node.js criada com o `tsoa`, um gerador de OpenAPI (Swagger) para aplicativos Node.js escritos em TypeScript.

## Requisitos

Certifique-se de ter instalado em sua máquina:

- Node.js (versão LTS recomendada)
- npm (ou yarn)

## Configuração

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/jacksonwsaguiar/p1-m10.git

2. **Instale as depedências:**

   ```bash
   cd p1-m10
3. **Execute as apis:**

   ```bash
   docker compose up

## Documentação Swagger

A documentação Swagger está disponível em http://localhost:3000/docs, onde você pode explorar e testar os endpoints da API interativamente.

## Coleção Insomnia

Arquivo "nodejs/Insomnia_collection.json" que se encontra na raiz do repositório.

## Comparação
No geral não diferenças significativas, apenas na primeira requisição(valores a esquerda) os valores eram elevados para a api em nodejs.

| Método   | Framework | Tempo médio (ms) |
|----------|-----------|------------------|
| GET All  | FastAPI   | 16 / 3           |
| POST     | FastAPI   | 17.2 / 20        |
| UPDATE   | FastAPI   | 4.14 / 2.1       |
| DELETE   | FastAPI   | 4.33 /2.2        |
| POST     | Node.js   | 38.5 / 6         |
| GET All  | Node.js   | 8 / 2.78         |
| DELETE   | Node.js   | 19 / 4.90        |
| UPDATE   | Node.js   | 11.5 / 7.71      |