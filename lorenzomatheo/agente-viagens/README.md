<h1 align="center">
  <a href="https://github.com/lorenzomatheo/agente-viagens">
  </a>
</h1>

<div align="center">
  Agente de Viagens
  <br />
  <a href="#sobre"><strong>Explore a documentação »</strong></a>
  <br />
  <br />
  <a href="https://github.com/lorenzomatheo/agente-viagens/issues/new?assignees=&labels=bug&template=01_BUG_REPORT.md&title=bug%3A+">Reporte um bug</a>
  ·
  <a href="https://github.com//lorenzomatheo/agente-viagens/issues/new?assignees=&labels=enhancement&template=02_FEATURE_REQUEST.md&title=feat%3A+">Sugerir uma funcionalidade</a>
  .
  <a href="https://github.com/lorenzomatheo/agente-viagens/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+">Fazer uma pergunta</a>
</div>

<div align="center">
<br />

[![Project license](https://img.shields.io/github/license/lorenzomatheo/agente-viagens.svg?style=flat-square)](LICENSE)

[![Pull Requests welcome](https://img.shields.io/badge/PRs-welcome-ff69b4.svg?style=flat-square)](https://github.com/lorenzomatheo/agente-viagens/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
[![code with love by lorenzomatheo](https://img.shields.io/badge/%3C%2F%3E%20with%20%E2%99%A5%20by-lorenzomatheo-ff1414.svg?style=flat-square)](https://github.com/lorenzomatheo)

</div>

<details open="open">
<summary>Conteúdos</summary>

- [Sobre](#sobre)
- [Ferramentas](#ferramentas)
- [Início](#início)
- [Pré requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Suporte](#suporte)
- [Asistência de Projeto](#assistência-de-projeto)
- [Contribuição](#contribuição)
- [Autores & contribuidores](#autores-e-contribuidores)
- [Securança](#securança)
- [Licença](#license)
- [Agradecimentos](#acknowledgements)

</details>

---

## Sobre

> **[?]**
> O projeto "Travel Agent" foi desenvolvido para automatizar a criação de roteiros de viagem personalizados. Ele integra diversas fontes de dados, como preços de passagens e informações turísticas relevantes, proporcionando ao usuário um planejamento completo e detalhado para sua viagem.

> O objetivo principal é facilitar o planejamento de viagens, economizando tempo do usuário ao centralizar informações importantes em um único assistente virtual.

> O projeto surgiu da vontade do autor de criar algo que não existia na época.

### Ferramentas

> **[?]**
> Linguagem de Programação: Python

> APIs: OpenAI GPT-3.5 Turbo

>Frameworks e Bibliotecas:

> LangChain (openai, community, hub, text-splitters, core),
> BeautifulSoup (bs4),
> ChromaDB,
> DuckDuckGo Search API,
> Wikipedia API

> Infraestrutura: AWS Lambda (Docker)

> Outros: Docker, cURL


## Início

### Pré requisitos

> **[?]**
> Python 3.12

> Docker instalado

> Conta na OpenAI com chave de API

> Acesso ao AWS Lambda para deploy

### Instalação

> **[?]** **1. Clonagem de repositório**

> Baixe ou clone o repositório contendo os seguintes arquivos de projeto:

> `git clone https://github.com/lorenzomatheo/agente-viagens`

> `cd travel-agent`

> **Arquivos inclusos:**

> - travelAgent.py

> - chatComp.py

> - Dockerfile

> - requirements.txt

> - try.curl

> **2. API Configuration**

> Defina a variável de ambiente OPENAI_API_KEY com sua chave de API da OpenAI:

> `export OPENAI_API_KEY=your_openai_api_key`

> **3. Instalando as dependências**

> Rodando localmente:

> `pip install -r requirements.txt`

> Usando Docker:

> `docker build -t travelagent .`


## Uso

> **[?]** **Using the API with cURL**

> `curl -X POST "http://api-travelagent-2015849192.us-east-2.elb.amazonaws.com"
-H "Content-Type: application/json" \
-d '{
    "question": "Vou viajar para Londres em julho de 2025.Quero que faça para um roteiro de viagem para mim com eventos que irão ocorrer na data da viagem e com o preço de passagem de São Paulo para Londres."
}
`


## Roadmap

Consulte as [issues abertas](https://github.com/lorenzomatheo/agente-viagens/issues) para ver a lista de recursos propostos (e problemas conhecidos).

- [Principais Solicitações de Recursos](https://github.com/lorenzomatheo/agente-viagens/issues?q=label%3Aenhancement+is%3Aopen+sort%3Areactions-%2B1-desc) (Adicione seu voto usando a reação 👍)  
- [Principais Bugs](https://github.com/lorenzomatheo/agente-viagens/issues?q=is%3Aissue+is%3Aopen+label%3Abug+sort%3Areactions-%2B1-desc) (Adicione seu voto usando a reação 👍)  
- [Bugs Mais Recentes](https://github.com/lorenzomatheo/agente-viagens/issues?q=is%3Aopen+is%3Aissue+label%3Abug)

## Suporte

Entre em contato com o mantenedor em um dos seguintes canais:

- [Issues do GitHub](https://github.com/lorenzomatheo/agente-viagens/issues/new?assignees=&labels=question&template=04_SUPPORT_QUESTION.md&title=support%3A+)  
- Opções de contato listadas neste [perfil do GitHub](https://github.com/lorenzomatheo)

## Assistência de Projeto

Se você quiser dizer **obrigado** e/ou apoiar o desenvolvimento ativo do Agente de Viagens:

- Adicione uma [estrela no GitHub](https://github.com/lorenzomatheo/agente-viagens) ao projeto.  
- Tweet sobre o Agente de Viagens.  
- Escreva artigos interessantes sobre o projeto no [Dev.to](https://dev.to/), [Medium](https://medium.com/) ou no seu blog pessoal.  

Juntos, podemos tornar o Agente de Viagens ainda **melhor**!

## Contribuição

Antes de tudo, obrigado por dedicar seu tempo para contribuir! As contribuições são o que tornam a comunidade de código aberto um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer beneficiará a todos e será **muito apreciada**.


Por favor, leia as [nossas diretrizes de contribuição](docs/CONTRIBUTING.md) e obrigado por fazer parte!

## Autores e contribuidores

A configuração original deste repositório foi feita por [Lorenzo Matheo](https://github.com/lorenzomatheo).

Para uma lista completa de todos os autores e colaboradores, consulte [a página de colaboradores](https://github.com/lorenzomatheo/agente-viagens/contributors).

## Securança

O Agente de Viagens segue boas práticas de segurança, mas não é possível garantir 100% de segurança. 

O Agente de Viagens é fornecido **"no estado em que se encontra"**, sem qualquer **garantia**. Use por sua conta e risco.

_Para mais informações e para relatar problemas de segurança, consulte a nossa [documentação de segurança](docs/SECURITY.md)._

## Licença

Este projeto está licenciado sob a **licença MIT**.

Consulte o [LICENSE](LICENSE) para mais informações.

## Agradecimentos

Agradeço ao trabalho da [RocketSeat](https://github.com/Rocketseat) que fez essa idéia ser possível.
