DB_NAME = wedding
DB_USER = postgres
DB_HOST = localhost

start:
	python manage.py runserver 0.0.0.0:8000

db_migrate:
	python manage.py migrate

db_makemigrations:
	python manage.py makemigrations wedding

db_drop:
	- rm ./db.sqlite3

db_reset: db_drop db_migrate db_seed

db_seed:
	python manage.py runscript db_seed

shell:
	python manage.py shell_plus

deploy:
	ssh-add keypairs/wedding.pem
	ansible-playbook -v -i provision/inventories/prod/hosts provision/main.yml
