from wizard_app.models import Wizard

Wizard.objects.create(name="Harry Potter", house="Gryffindor", pet="Hedwig", year=5)
Wizard.objects.create(name="Hermione Granger", house="Gryffindor", pet="Crookshanks", year=5)
Wizard.objects.filter(id=1)
Wizard.objects.filter(house="Gryffindor")
edit=Wizard.objects.get(id=1)
edit.year=6
edit.save()