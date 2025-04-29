import random
from django.core.management.base import BaseCommand
from faker import Faker
from eventin.models import Evento, Participante, Inscricao
from validate_docbr import CPF

class Command(BaseCommand):
    help = "Popula o banco de dados com dados ficticios para eventos e participantes"
    
    def handle(self, *args, **kwargs):
        faker = Faker()
        cpf_validator = CPF()
        
        eventos_titulos = [
            'Conferência de Desenvolvimentos Web'
            'Workshop de Análise de Dados',
            'Seminário de inteligência Artificial',
            'Palestra sobre Marketing Digital',
            'Curso de Gestão de projetos',
            'Aulas de Programação em Python',
            "Evento de Segurança de Informação",
            'Exposição de Designer Gráfico',
            "Hackaton de Desenvolvimeto Mobile",
            "Forum de Banco de Dados"            
        ]
        #Popular eventos
        eventos = []
        for _ in range(10):
            evento = Evento(
                titulo = random.choice(eventos_titulos),
                descricao = faker.text(max_nb_chars=20),
                local = faker.city(),
                data_evento = faker.date_time_between(start_date='now', end_date='+30d'),
                capacidade = random.randint(50,200)
            )
            eventos.append(evento)
        Evento.objects.bulk_create(eventos)
        
        participantes = []
        for _ in range(100):
            cpf = cpf_validator.generate()
            participante = Participante(
                nome = faker.name(),
                cpf = cpf,
                email = faker.unique.email(),
                telefone = faker.phone_number()
            )
            participantes.append(participante)
        Participante.objects.bulk_create(participantes)
        
        participantes_ids = Participante.objects.values_list('id', flat=True)
        eventos_ids = Evento.objects.values_list('id', flat=True)
        
        inscricoes = []
        for participante_id in participantes_ids:
            for _ in range(random.randint(1,3)):
                inscricao = Inscricao(
                    evento_id = random
                    .choice(eventos_ids),
                    participante_id = participante_id
                )
                inscricoes.append(inscricao)
        Inscricao.objects.bulk_create(inscricoes)
        
        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))
