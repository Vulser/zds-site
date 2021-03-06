# coding: utf-8

from zds.forum.models import get_last_topics
from zds.tutorial.models import get_last_tutorials
from zds.article.models import get_last_articles
from zds.utils import render_template
from zds.member.decorator import can_read_now

@can_read_now
def home(request):
    '''
    Display the home page with last topics added
    '''
    return render_template('home.html', {
        'last_topics': get_last_topics(request.user),
        'last_tutorials': get_last_tutorials(),
        'last_articles': get_last_articles(),
    })

@can_read_now
def index(request):
    return render_template('pages/index.html')

@can_read_now
def help_markdown(request):
    '''
    Display a page with a markdown helper
    '''
    return render_template('pages/help_markdown.html')

@can_read_now
def about(request):
    '''
    Display many informations about the website
    '''
    return render_template('pages/about.html')

@can_read_now
def roadmap(request):
    '''
    Display roadmap of the website
    '''
    return render_template('pages/roadmap.html')
