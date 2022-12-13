# build_files.sh
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
# export DJANGO_SUPERUSER_EMAIL=admin@admin.com
# export DJANGO_SUPERUSER_PASSWORD=test@pass1234
# export DJANGO_SUPERUSER_FIRST_NAME=admin
# export DJANGO_SUPERUSER_LAST_NAME=admin
# export DJANGO_SUPERUSER_PHONE_NUMBER=0123456789
# python3.9 manage.py createsuperuser --no-input