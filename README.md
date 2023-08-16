# Model Prediction API

Este repositório contém uma API de previsão de modelo que utiliza o framework FastAPI para fazer previsões com base em um modelo treinado. O modelo é carregado durante o início do aplicativo e as previsões podem ser feitas por meio de chamadas POST para o endpoint '/predict'. A autenticação é necessária para acessar esse endpoint, e um token de autorização deve ser fornecido.

## Configuração

Antes de começar a usar a API, certifique-se de ter todas as dependências instaladas. Você pode fazer isso executando o seguinte comando:

```bash
pip install -r requirements.txt
```

## Executando a API

Para executar a API, execute o seguinte comando, entrando na pasta src:

```bash
uvicorn main:app --reload
```

Isso iniciará o servidor e o API estará disponível em http://localhost:8000.

## Autenticação

Para acessar o endpoint '/predict', você deve fornecer um token de autorização válido no cabeçalho de autenticação da solicitação. O token atualmente aceito é "abc123". Você pode modificar a função get_username_for_token para validar tokens diferentes, se necessário.

## Fazendo Previsões

Para fazer uma previsão, faça uma chamada POST para http://localhost:8000/predict. Certifique-se de incluir os dados da pessoa no corpo da solicitação. Aqui está um exemplo de dados JSON que você pode usar:

```json
{
  "age": 42,
  "job": "entrepreneur",
  "marital": "married",
  "education": "primary",
  "balance": 558,
  "housing": "yes",
  "duration": 186,
  "campaign": 2
}
```

## Estrutura do Projeto

main.py: Contém o código principal do FastAPI, incluindo os endpoints e a lógica de autenticação.
entities.py: Definição da classe Person para representar os dados de entrada.
model.py: Funções para carregar o modelo treinado e o codificador necessário.
requirements.txt: Lista de dependências do Python.

## Contribuição

Sinta-se à vontade para contribuir para este repositório, abrindo problemas ou enviando solicitações pull. Todas as contribuições são bem-vindas!

Espero que isso ajude! Lembre-se de personalizar as informações do README de acordo com o seu projeto e suas necessidades específicas.
