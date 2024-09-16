```python
download the todo folder and run the following commands
```

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations todoapp
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```