# Traduções Powered by LangChain

Este projeto foi desenvolvido com o objetivo de aplicar meus conhecimentos em **FastAPI**, **LangChain**, **OpenAI** e **API de Tradução**. O código foi projetado para realizar traduções automáticas de textos em diversos idiomas, com foco no uso de APIs e práticas modernas de desenvolvimento.

## Descrição

O sistema utiliza o modelo **GPT-3.5-turbo** da OpenAI para traduzir textos para diferentes idiomas. O backend é construído usando **FastAPI** para fornecer uma API RESTful para realizar as traduções. A comunicação entre o cliente e o servidor é feita utilizando o LangChain e a interface de rede do **langserve**.

## Arquitetura

O sistema é composto pelos seguintes componentes:

1. **Servidor (`servidor.py`)**: Implementa o servidor FastAPI, que expõe a API de tradução.
2. **Código (`codigo.py`)**: Define o pipeline de tradução utilizando LangChain e o modelo GPT-3.5 da OpenAI.
3. **Cliente (`cliente.py`)**: Envia requisições ao servidor para traduzir o texto em diferentes idiomas, utilizando a API RESTful criada.

## Dependências

- `FastAPI` para criar o servidor de API.
- `Uvicorn` como servidor ASGI para rodar o FastAPI.
- `LangChain` para orquestrar o uso de modelos de linguagem.
- `langserve` para facilitar a execução remota dos pipelines.
- `python-dotenv` para carregar variáveis de ambiente como a chave da API do OpenAI.
- `OpenAI` para interação com os modelos de linguagem.

## Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento:

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API do OpenAI:

   ```bash
   OPENAI_API_KEY=your-api-key
   ```

## Como Rodar

### Rodando o Servidor

Para rodar o servidor FastAPI localmente, execute o seguinte comando:

```bash
python servidor.py
```

O servidor estará disponível em `http://localhost:8000`.

### Exemplo de Uso com Cliente

Para utilizar a API de tradução, execute o arquivo `cliente.py`:

```bash
python cliente.py
```

O cliente enviará um texto e o servidor devolverá a tradução para o idioma especificado.

## Estrutura de Arquivos

```plaintext
.
├── servidor.py          # Código do servidor FastAPI
├── codigo.py            # Definição do pipeline de tradução com LangChain
├── cliente.py           # Cliente para testar a API de tradução
├── .env                 # Arquivo de variáveis de ambiente
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo
```

## Contribuições

Este projeto foi desenvolvido para fins de portfólio e estudos. Se você encontrar algum erro ou sugestão de melhoria, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
