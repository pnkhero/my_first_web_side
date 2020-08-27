from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.shortcuts import redirect

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur mon blogizi !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol izi !</p>
    """)

def view_articles(request):
    """
    Vue qui affiche un article selon sin identifiant (ou ID, ici un numero)
    """
    return HttpResponse(
        """vous avez demandé l'article n°izi"""
    )

def view_boy(request):
    return redirect(view_redirection)

def view_redirection(request):
    return HttpResponse("vous avez éte tej")

def date_act(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})

def addition(request, nb1, nb2):
    total = nb1 + nb2
    return render(request, 'blog/addition.html', locals())

def view_test(request):
    return render(request, 'blog/reference.html')

def view_luck(request):
    return render(request, 'blog/luck.html')