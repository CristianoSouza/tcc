from django.http import HttpResponse

from .models import Aluno

def index(request):
    lateste_aluno_list = Aluno.objects.order_by('-pub_date')[:5]
    template = loader.get_template('academicManager/index.html')
    context = {
        'latest_aluno_list': latest_aluno_list,
    }
    return HttpResponse(template.render(context,request))

def detail(request, aluno_id):
    return HttpResponse("You're looking at question %s." % aluno_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % aluno_id)

