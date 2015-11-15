from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

def main(request):
    quesiton = " This is poll website !"
    return render(request, 'polls/results.html', { 'question': question })
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ return the last five published question """
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """ return only published questions till now """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

"""def index(request):
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)
    template = loader.get_template('polls/index.html')
    context = RequestContext(request, {
        'latest_question_list': latest_question_list,
        })
    return HttpResponse(template.render(context))
    output = ', '.join([p.question_text for p in latest_question_list])
    return HttpResponse(output) 
    return HttpResponse("Hello World,  you are at polls index")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question })
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DeosNotExist :
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
    return HttpResponse("You are looking at question %s." % question_id)

def results(request,  question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
"""
def vote(request,  question_id):
    q = get_object_or_404(Question,  pk=question_id)
    try :
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError,  Choice.DoesNotExist):
# redisplay polling form
        return render(request, 'polls/detail.html', { 
            'question':q, 
            'error_message': "you didn't select a choice.", 
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(q.id, )))
