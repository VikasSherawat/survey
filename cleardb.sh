find . | grep -E "(pycache|.pyc|.pyo$)" | xargs rm -rf
rm db.sqlite3
python -c 'print("File removed")'
touch createpolls/migrations/__init__.py  
python -c 'print("init file created")'
python manage.py makemigrations createpolls
python -c 'print("Make Migrations run")'
python manage.py migrate 
python -c 'print("Migrate command run")'
