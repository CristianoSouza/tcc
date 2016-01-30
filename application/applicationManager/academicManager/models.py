from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Rfid(models.Model):
    rfid_code = models.CharField(max_length=200)

    def __str__(self):
        return self.rfid_code

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=16, blank=True)
    data_nascimento = models.DateField(null=True,blank=True)
    email = models.EmailField(blank=True)
    nome_pai = models.CharField(max_length=200, null=True)
    nome_mae = models.CharField(max_length=200, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    rfid_code = models.ForeignKey(Rfid, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    rg = models.CharField(max_length=16, blank=True)
    data_nascimento = models.DateField(null=True,blank=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class AlunoDisciplina(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE )
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE )

    def __str__(self):
        return (self.aluno.nome + " - " + self.disciplina.nome )

class Arduino(models.Model):
    id_arduino = models.CharField(max_length=200)

    def __str__(self):
        return (self.id_arduino)

class Sala(models.Model):
    bloco = models.CharField(max_length=200)
    espaco = models.CharField(max_length=200)
    sala = models.CharField(max_length=200)
    arduino = models.ForeignKey(Arduino, on_delete=models.CASCADE)

    def __str__(self):
        return self.bloco + " - " + self.espaco + " - " + self.sala

class Aula(models.Model):
    data = models.DateField(null=True,blank=True)
    horario_inicio = models.TimeField(null=True,blank=True)
    horario_fim = models.TimeField(null=True,blank=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)

    def __str__(self):
        return self.disciplina.nome + " - " + self.data.strftime("%Y-%m-%d")

class Chamada(models.Model):
    PRESENCA_CHOICES = (
        ('P', 'Presença'),
        ('F', 'Falta'),
    )
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    horario_leitura = models.TimeField(null=True,blank=True)
    presenca = models.CharField(max_length=1, choices=PRESENCA_CHOICES)

    def __str__(self):
        return (self.aluno.nome)



