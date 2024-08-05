<h1 align="center" style="font-weight: bold;">Box Bank</h1>


<img src="image.png">

<h2 id="technologies">💻 Tecnologias utilizadas</h2>

- Django WEB Framework
- JavaScript
- Bootstrap

<h2 id="started">🚀 Como utilizar</h2>

O projeto tem como objetivo simular um Intenet Banking, sendo suas principais funcionalidades:

- PIX
- Geração e pagamento de Boletos
- Transferências via TED

<h3>Pré requisitos</h3>

- Django 4.0+
- Bootstrap

<h3>Clone</h3>

Para clonar o projeto digite o código abaixo no terminal

```bash
git clone git@github.com:thiagoedus/BoxBank.git
```


<h3>Starting</h3>

Crie um ambiente virtual para controlar as dependências do projeto

```bash
# No linux
python3 -m venv nome_do_ambiente
source nome_do_ambiente/bin/activate
pip install -r requirements.txt

# No Windows
python -m venv nome_do_ambiente
venv\Scripts\activate
pip install -r requirements.txt
```

Siga as instruções para iniciar a aplicação

```bash
# No linux
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver

# No Windows
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
