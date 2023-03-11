# Bloxs Bank (Back-End) - Documentação

## Sumário

- [Bloxs Bank (Back-End) - Documentação](#bloxs-bank-back-end---documentação)
  - [Sumário](#sumário)
  - [1. Resumo](#1-resumo)
  - [2. Diagrama de entidades e relacionamentos](#2-diagrama-de-entidades-e-relacionamentos)
  - [3. Preparativos](#3-preparativos)
    - [3.1. Instalando Dependências](#31-instalando-dependências)
    - [3.2. Variáveis de ambiente](#32-variáveis-de-ambiente)
    - [3.3. Entrando no ambiente virtual](#33-entrando-no-ambiente-virtual)
    - [3.4. Instale as dependências](#34-instale-as-dependências)
    - [3.4. Execute as migrações para realizar a persistência de dados](#34-execute-as-migrações-para-realizar-a-persistência-de-dados)
  - [4. Autenticação](#4-autenticação)
  - [5. Rotas](#5-rotas)
    - [Documentação da API](#documentação-da-api)
  - [Após abrir o servidor local, basta acessar ```http://127.0.0.1:8000/docs/``` para informações detalhadas sobre o funcionamento da API.](#após-abrir-o-servidor-local-basta-acessar-http1270018000docs-para-informações-detalhadas-sobre-o-funcionamento-da-api)

---

## 1. Resumo

API estruturada guiada pelo teste técnico feito pela Bloxs.

Tecnologias usadas nesse projeto:

- [DJango](https://www.djangoproject.com/)
- [DJango Rest Framework](https://www.django-rest-framework.org/)
- [Psycopg2-binary](https://pypi.org/project/psycopg2-binary/)
- [Black](https://pypi.org/project/black/)
- [IPython](https://pypi.org/project/ipython/)
- [IPDB](https://pypi.org/project/ipdb/)

## 2. Diagrama de entidades e relacionamentos

[ Voltar ao topo ](#sumário)

![ERD](<[[/diagram-er.png](https://drive.google.com/file/d/1E7HWnj8lBfhXLGLWDmS0lR7gwxZYrFDR/view](https://drive.google.com/file/d/1vz1GH9YgzzlMv16QOuOEu6a1GiQaWujp/view?usp=sharing))>)

---

## 3. Preparativos

[ Voltar ao topo ](#sumário)

### 3.1. Instalando Dependências

Clone o projeto em sua máquina local e instale o ambiente virtual VENV:

```shell
python -m venv venv
```

### 3.2. Variáveis de ambiente

Crie um arquivo **.env** no diretório raiz do projeto, copiando o exemplo do **.env.example**:

```shell
cp .env.example .env
```

Atribua suas variáveis de ambiente às credenciais do seu PostgreSQL à um database da sua escolha.

### 3.3. Entrando no ambiente virtual

Entre no ambiente virtual com o comando:

**Windows**

```shell
source venv/Scripts/activate # terminal BASH
```

ou

```shell
.\venv\Scripts\activate # terminal powershell
```

**Linux**

```shell
source venv/bin/activate
```

### 3.4. Instale as dependências

Dependências necessárias para rodar o projeto:

```shell
pip install -r requirements.txt
```

### 3.4. Execute as migrações para realizar a persistência de dados

**Windows**

```shell
.\manage.py migrate # terminal BASH
```

ou

```shell
python manage.py migrate # terminal powershell
```

**Linux**

```shell
./manage.py migrate
```

---

## 4. Autenticação

[ Voltar ao topo ](#sumário)

## 5. Rotas

[ Voltar ao topo ](#sumário)

### Documentação da API

É possível acessar à documentação completa para poder utilizar a API.

Nessa mesma documentação é possível adquirir informações sobre os requests, como chaves necessárias do request para algumas rotas.

Após abrir o servidor local, basta acessar ```http://127.0.0.1:8000/docs/``` para informações detalhadas sobre o funcionamento da API.
---