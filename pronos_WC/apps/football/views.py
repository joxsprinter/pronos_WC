from __future__ import (print_function, division, absolute_import, unicode_literals)

from django.views.generic import TemplateView, ListView, DetailView
from .models import Joueur, Match


class JoueurClassementView(ListView):
    template_name = 'joueur/classement.html'
    model = Joueur

    def get_queryset(self):
        return Joueur.objects.order_by('-points')

class MatchView(ListView):
    template_name = 'match/next.html'
    model = Match

    def get_queryset(self):
        return Match.objects.order_by('-date').filter(traite=0)

class MatchOldView(ListView):
    template_name = 'match/old.html'
    model = Match

    def get_queryset(self):
        return Match.objects.order_by('-date').filter(traite=1)
