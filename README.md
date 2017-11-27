![Criptosorteio logo][https://github.com/alepmaros/criptosorteio/blob/master/criptosorteio/static/img/criptosorteio_logo.png]

# criptosorteio

Um site em Django para realizar sorteios auditáveis

# Instruções:

- pip3 install -r requirements.txt
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py runserver


# Cronjob

Template:

```
* * * * * . /home/ubuntu/.envs && /home/ubuntu/virtualenv/criptosorteio/bin/python3 /home/ubuntu/criptosorteio/criptosorteio/manage.py runcrons >> /home/ubuntu/cron_log.txt 2> /home/ubuntu/cron_error_log.txt
* * * * * sleep 30 && . /home/ubuntu/.envs && /home/ubuntu/virtualenv/criptosorteio/bin/python3 /home/ubuntu/criptosorteio/criptosorteio/manage.py runcrons >> /home/ubuntu/cron_log.txt 2> /home/ubuntu/cron_error_log.txt
```
