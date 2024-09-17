# eliminar migraciones anteriores
sudo chmod +x delete_migrations.sh
./delete_migrations.sh

# generamos las migraciones
python manage.py makemigrations accounts
python manage.py makemigrations accounting companies crm inventary invoices warenhouses
python manage.py migrate
python manage.py sowseed


# linea a linea para unix
./manage.py makemigrations accounts
./manage.py makemigrations accounting companies crm inventary invoices warenhouses
./manage.py migrate
./manage.py sowseed

# un solo comando para unix
./manage.py makemigrations accounts &&
./manage.py makemigrations accounting companies crm inventary invoices warenhouses &&
./manage.py migrate &&
./manage.py sowseed