# My Web App for RSOI by Igor Borzunov IU7-11M

## Used services
* [Python 3.7](https://www.python.org/download/releases/3.0/)
* [Django](http://www.django-rest-framework.org)
* [myenv](https://pypi.org/project/myenv/)
* [Vue JS](https://vuejs.org)


Start project  

```
python project/manage.py flush
python project/manage.py makemigrations
python project/manage.py migration

Важно использовать команды выше при изменениях БД

python project/manage.py runserver

then - add to adress input - /api/ 
```
If you want to start only frontend app
```
cd project
cd apps
cd frontend
npm install
npm run build dev
```

Tests
```
python project/test .
```

Enjoy!
