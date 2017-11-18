# criptosorteio
Um site em Django para realizar sorteios auditáveis


Requerimentos:

django

# Instruções:

- pip3 install -r requirements.txt
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py runserver


# Cronjob

Template:

```
* * * * * source /home/apm/.virtualenvs/criptosorteio/bin/activate && python3 /home/apm/git/criptosorteio/criptosorteio/manage.py runcrons >> /home/apm/git/criptosorteio/logs.txt
* * * * * sleep 30 && source /home/apm/.virtualenvs/criptosorteio/bin/activate && python3 /home/apm/git/criptosorteio/criptosorteio/manage.py runcrons >> /home/apm/git/criptosorteio/logs.txt
```