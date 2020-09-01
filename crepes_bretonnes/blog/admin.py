from django.contrib import admin
from django.utils.text import Truncator

from .models import Categorie, Article

class ArticleAdmin(admin.ModelAdmin):
    list_display    = ('titre', 'auteur', 'date', 'apercu_contenu')
    list_filter     = ('auteur', 'categorie',)
    date_hierarchy  = 'date'
    ordering        = ('date', )
    search_fields   = ('titre', 'contenu')

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
       ('Général', {
            'classes': ['collapse', ],
            'fields': ('titre', 'auteur', 'categorie')
        }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article', {
           'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
           'fields': ('contenu', )
        }),
    )

    def apercu_contenu(self, article):
        """
        retourne les 40 premiers cara du contenu de l'article,
        suivi de points de suspension si le text est plus long.
        """
        return Truncator(article.contenu).chars(40, truncate='...')

    apercu_contenu.short_description = 'Apercu du contenu'    

admin.site.register(Categorie)
admin.site.register(Article, ArticleAdmin)