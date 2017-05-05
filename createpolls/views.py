from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, Http404
from django.urls import reverse

from polls import settings
from util import EmailThread
from .models import Question, Choice

from django.contrib import messages
# Create your views here.


def send_html_mail(to_email,myurl):
    url = '%s%s' % (settings.HOSTNAME, myurl)
    print('sending email-->' + url)
    message = 'Dear User,<br/>' \
              'You are invited to take part in the poll.<br/>' \
              'Please access the poll using following link.<br/>' \
              '<a href="'+url+'" role="button">Participate</a>' \
               '<br><br>Regards,<br/>' \
               'Poll Survey'
    EmailThread(to_email,message).start()


def index(request):
    if request.method=='POST':
        question = request.POST.get('question')
        q = Question()
        q.question = question
        emails = request.POST.get('email')
        to = [x.strip() for x in emails.split(',')]
        q.save()
        for i in range(1,21):
            choice = request.POST.get('textbox'+str(i))
            if choice is None or len(choice)==0:
                break
            else:
                c = Choice()
                c.question =q
                c.choice = choice
                c.save()
        #send link for people to vote
        try:
            q.save()
            #send_html_mail(to,request.get_full_path()+q.q_num)
        except:
            messages.error(request,'Error occured in saving poll')
            #raise Http404("Error occured in saving poll")
            return render(request, 'createpolls/createpoll.html')
        else:
            return HttpResponseRedirect(reverse('polls:detail',args=[q.q_num]))

    return render(request,'createpolls/createpoll.html')


def detail(request,q_num):
    context = {}
    q = get_object_or_404(Question, q_num=q_num)
    context['question'] = q
    return render(request,'createpolls/polldetails.html',context)


def vote(request,q_num):
    context = {}
    q = get_object_or_404(Question, q_num=q_num)
    try:
        selected_choice = q.choice_set.get(pk= request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        messages.error(request, "You didn't select a choice.")
        return render(request, 'createpolls/polldetails.html', {
            'question': q,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result',args=[q_num]))


def result(request,q_num):
    q = get_object_or_404(Question, q_num=q_num)
    context = dict()
    context['question'] = q
    return render(request,'createpolls/results.html',context)