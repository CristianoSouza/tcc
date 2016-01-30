from django.contrib import admin

from .models import Aluno
from .models import Professor
from .models import Curso
from .models import Disciplina
from .models import Aula
from .models import Chamada
from .models import Rfid
from .models import AlunoDisciplina
from .models import Sala
from .models import Arduino


class ChamadaInline(admin.TabularInline):
    model = Chamada

class AulaAdmin(admin.ModelAdmin):
    inlines = [ChamadaInline,]

    def save_model(self, request, obj, form, change):
        print ("ID aula: ", obj.id)
        print ("ID DISCIPLINA: ", obj.disciplina.id)

        obj.save()

        alunoDisciplina = AlunoDisciplina.objects.filter(disciplina= obj.disciplina)
       
        for al in alunoDisciplina:
            print ("AlunoDisciplina:", al.aluno)

            chamada = Chamada.objects.filter(aula= obj, aluno= al.aluno)
            print ("Chamada:", chamada)
            if (chamada):
                print ("Aluno jah esta presente na chamada!")                
            else:
                chamada = Chamada(aula=obj, aluno= al.aluno, presenca = 'F')
                chamada.save()
                print ("Salvo presença do aluno:", al.aluno)

class AulaInline(admin.TabularInline):
    model = Aula

class DisciplinaAdmin(admin.ModelAdmin):
    inlines = [AulaInline,]

class DisciplinaInline(admin.TabularInline):
    model = Disciplina

class CursoAdmin(admin.ModelAdmin):
    inlines = [DisciplinaInline,]

class AlunoDisciplinaInline(admin.TabularInline):
    model =AlunoDisciplina

class AlunoAdmin(admin.ModelAdmin):
    inlines = [AlunoDisciplinaInline,]

class ProfessorAdmin(admin.ModelAdmin):
    inlines = [DisciplinaInline,]

class ChamadaAdmin(admin.ModelAdmin):
    readonly_fields = ('aula','aluno')

class ArduinoAdmin(admin.ModelAdmin):
    model = Arduino

class SalaAdmin(admin.ModelAdmin):
    model = Sala

admin.site.register(Curso, CursoAdmin)
admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Professor)
admin.site.register(Disciplina, DisciplinaAdmin)
admin.site.register(Aula, AulaAdmin)
admin.site.register(Chamada, ChamadaAdmin)
admin.site.register(Rfid)
admin.site.register(AlunoDisciplina)
admin.site.register(Arduino, ArduinoAdmin)
admin.site.register(Sala, SalaAdmin)


