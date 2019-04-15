# AgentX

### Зависимости
- docker version 18.06.3-ce
- docker-compose version 1.21.0
- postgres 10.6
- pip==19.0.3
- pipenv==2018.11.26

### Запуск в docker-compose
```
cp conf/.env-example conf/.env
cp devops/.env-example devops/.env
cd devops && docker-compose -p agentx up
```

### Ручной запуск
1. Настроить переменные из conf/.env
2. Установить зависимости 
```
pipenv shell --python 3.6
pipenv install
```
3. Провести миграции
```
python manage.py migrate
```
4. Запустить сервер
```
python manage.py runserver
```

### API
**Получение сотрудника по pk**
GET http://localhost:8000/geo/employee/1/

**Получение перемещения сотрудника по pk**
GET http://localhost:8000/geo/employee/1/history/

**Генерация тестовых перемещений сотрудника по pk**
GET http://localhost:8000/geo/employee/1/generate/?created_at__gte=2019-04-15 20:17:32&created_at__lt=2019-04-15 20:30:23&latitude=55.231123&longitude=56.231123

**Создание сотрудника**
POST http://localhost:8000/geo/employee/
```
{
	"first_name": "Ришат",
	"last_name": "Шарафиев",
	"gender": 0,
	"birth_day": "1994-05-25",
	"email": "rishatsharafiev@ya.ru"
}
```

**Обновление сотрудника по pk**
PATCH http://localhost:8000/geo/employee/1/
```
{
	"first_name": "Ришат",
	"last_name": "Шарафиев",
	"gender": 0,
	"birth_day": "1994-05-25",
	"email": "rishatsharafiev@ya.ru"
}
```

**Удаление сотрудника по pk**
DELETE http://localhost:8000/geo/employee/1/
