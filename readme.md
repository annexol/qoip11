##### 1) Клонировать проект:
<pre>
git clone https://github.com/annexol/qoip11.git
</pre>
##### 2) Cоздать виртуальное окружение используя зависимости (requirements.txt)

##### 3) В файле \...\qoip11\input\input\settings.py указать данные для Вашей базы данных
<pre>
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': your_name,
        'USER': your_user,
        'PASSWORD': your_password,
        'HOST': your_host,

    }
}
</pre>

##### 4) Выполнить миграции
<pre>
manage.py migarte
</pre>

##### 5) Запустить сервер
<pre>
manage.py runserver
</pre>
