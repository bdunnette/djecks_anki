from django.db import models
from djecks.models import Deck

class AnkiDeck(models.Model):
    parent = models.ForeignKey(Deck, blank=True, null=True)
    apkg = models.FileField(upload_to="djecks_anki/apkg", blank=True)
    
    def __unicode__(self):
        if self.parent:
            return self.parent.title
        else:
            return str(self.id)