from django_cron import CronJobBase, Schedule
from django.utils import timezone

from .models import Sorteio

from datetime import datetime
from utils.rbeacon import RBeacon

import hashlib

class SortearVencedoresCronJob(CronJobBase):
    RUN_EVERY_MINS = 0

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'sorteios.soterar_vencedores'

    def do(self):

        rbeacon = RBeacon()
        sorteios = Sorteio.objects.filter(string_nist__isnull=True).filter(hora_sorteio__lte=timezone.now())

        for s in sorteios:
            value = rbeacon.get_output_value( s.hora_sorteio.timestamp() )

            # If the NIST string is already availabe, draw the winner,
            # otherwise wait for the next execution
            if value['valid']:
                # If there is participants, choose one winner, otherwise just fill the nist string
                if s.participantes.all().count() > 0:
                    participants = []
                    for p in s.participantes.all():
                        conc_username = p.username + value['output_value']
                        hashed = hashlib.sha256(str.encode(conc_username)).hexdigest()
                        participants.append((p, hashed))

                    participants = sorted(participants, key=lambda participants: participants[1])

                    s.id_ganhador = participants[0][0]

                s.string_nist = value['output_value']
                s.save()

            else:
                pass
