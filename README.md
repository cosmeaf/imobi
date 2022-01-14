# Agendamento de Visitas para Imobiliária Com Django

<h2 align="center">
    O projeto se destina a ser usado por imóveis ou vendedores de imóveis
</h2>
<hr>

<p align="center">
    Pagina de Cadastro/Registro
</p>
<div align="center">
    <img src="https://user-images.githubusercontent.com/45183265/149579697-8c188ddb-1e65-4452-8ad6-975996968c3e.png" width="600px"/>
</div>

<p align="center">
    Pagina de Login / Acesso
</p>
<div align="center">
    <img src="https://user-images.githubusercontent.com/45183265/149579653-c0b1484a-f5c5-4204-9742-d52b68162ff1.png" width="600px"/>
</div>

<p align="center">
    Pagina de Imóveis disponiveis para Alugar ou Vender
</p>
<div align="center">
    <img src="https://user-images.githubusercontent.com/45183265/149579690-01fd2ba5-6ba8-4f7c-a50d-ee374f043265.png" width="600px"/>
</div>

<p align="center">
    Pagina de informação sobre o Imóvel
</p>
<div align="center">
    <img src="https://user-images.githubusercontent.com/45183265/149579695-1b006253-c1d8-43f4-91fc-3b84095fd4aa.png" width="600px"/>
</div>

<p align="center">
    Pagina de informação sobre o Imóvel
</p>
<div align="center">
    <img src="https://user-images.githubusercontent.com/45183265/149579695-1b006253-c1d8-43f4-91fc-3b84095fd4aa.png" width="600px"/>
</div>
## Começando

Primeiro vamos criar o ambiente virtual e ativa-lo
```
# Criar
	# Linux
		python3 -m venv venv
	# Windows
		python -m venv venv

#Ativar
	# Linux
		source venv/bin/activate
	# Windows
		venv/Scripts/Activate
		
```
### Pré-requisitos

Conhecimento em Python / Django / Html / CSS / Bootstrap / Banco de Dados

Editor de Codigo (Pychar, VsCode, Sublime-Text)


### Agora deve-se instalar as bibliotecas necessárias

```
pip install django
pip install pillow
```

## Crie seu projeto django
Após realizar instalação das bibliotecas do DJANGO, iremos criar um projeto conforme comando
abaixo:

```
django-admin startproject imobi .

```
Em seguida criaremos a nossa aplicação:
``` 
python manage.py startapp autenticacao

```

### Configure os arquivos estáticos em settings.py

Neste passo deve-se ter muita atenção, pois iremos adicionar e alterar alguns parametros no arquivo
de settigns do DJANGO
Cada configuração abaixo, representão uma funcionalida para o django, para demais informação, basta acessar
o link do django: https://docs.djangoproject.com/en/4.0/

```
import os

ALLOWED_HOSTS = ['*']

'DIRS': [os.path.join(BASE_DIR, 'templates')],

INSTALLED_APPS = [ 
    'autenticacao',
    'app_platform'
],

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
STATIC_ROOT = os.path.join('static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

THOUSAND_SEPARATOR = '.',
USE_THOUSAND_SEPARATOR = True

```

### Vamos então criar o nosso app para trabalharmos com cadastro e login de usuário

Nesta etapa, iremos criar a rotas e as views para acesso a pagina de sua aplicação

### Aqui alteramos o arquivo urls.py do projeto
```
path('auth/', include('autenticacao.urls')),
```

### Abaixo alteramos o arquivo de urls.py da aplicação
```
path('cadastro/', views.cadastro, name='cadastro'),
path('logar/', views.logar, name='logar'),

```
### Faça que a view cadastro renderize uma página em html

Aqui voce criar suas views para acessar as paginas de seu projeto

```
def cadastro(request):
    return render(request, 'cadastro.html')

def logar(request):
    pass

```

### Observação:
Demais informações sobre o source, basta acessar o source code.
Está foi uma breve descrição de como foi realizado a construção deste pequeno projeto
## Construído com

* [PYSTACK WEEK 2.0](https://pythonando.com.br/) - PYSTACK WEEK 2.0
* [Django](https://docs.djangoproject.com/en/4.0/) - Django documentation
* [Python](https://docs.python.org/3/) - Python 3.10.1 documentation

## Versão

Usamos [SemVer](http://semver.org/) para controle de versão. Para as versões disponíveis, consulte as [tags neste repositório](https://github.com/your/project/tags).

## Autores

* **Cosme Alves** - [Github](https://github.com/cosmeaf/Data-Science-Python-Developer)
* **Cosme Alves** - [Linkedin](https://www.linkedin.com/in/cosme-alves-desenvolvedor/)

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes

## Agradecimentos

* Smart Mecanico
* PYSTACK WEEK 2.0
* Geek university
