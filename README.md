# aula-django-blog
Exemplo didático de uma aplicação django

# Como usar?
1 - Baixar os códigos no github:
https://github.com/tpipernob/aula-django-blog 
2 - Descompactar em uma pasta no seu computador
3 - Abrir o projeto no VsCode (ou de preferência)
4 - Criar o ambiente virtual
python -m venv venv
5 - Acessar o ambiente virtual
.\venv-projeto1\Scripts\activate
6 - Instalar dependências
 pip install -r requirements.txt
7 - Criar o banco de dados
python manage.py makemigrations
python manage.py migrate
8 - Subir o projeto
python manage.py runserver
