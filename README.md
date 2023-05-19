# MartySecure
Persoonlijk Onderzoek Project

- Instructies voor het downloaden en toepassen van een bestaand Django-project vanaf GitHub
Om een bestaand Django-project vanaf GitHub te downloaden en toe te passen, volg je de onderstaande instructies:

- Download en installeer Git:
Als je Git nog niet op je systeem hebt geïnstalleerd, ga dan naar de officiële Git-website (https://git-scm.com/) en download de versie die geschikt is voor jouw besturingssysteem. Volg de installatie-instructies om Git correct te installeren.

- Clone het GitHub-project:
Open een terminal of de Git Bash en navigeer naar de gewenste locatie waar je het Django-project wilt opslaan. Gebruik het onderstaande commando om het project van GitHub te klonen:

- Copy code
```bash
git clone <repository-url>
```
Vervang <repository-url> door de URL van het GitHub-project dat je wilt downloaden. Dit vind je op de GitHub-pagina van het project onder de knop "Code".

- Navigeer naar het project:
Ga naar de gekloonde map van het project met het volgende commando:

- Copy code
cd <project-directory>
Vervang <project-directory> door de naam van de map van het gekloonde project.

- Maak een virtuele omgeving:
Het is sterk aanbevolen om een virtuele omgeving te maken om de afhankelijkheden van het Django-project geïsoleerd te houden. Voer het volgende commando uit om een virtuele omgeving te maken:

```bash
Copy code
python -m venv myenv
```
Hier wordt myenv vervangen door de naam die je wilt geven aan de virtuele omgeving.

Activeer de virtuele omgeving:
Activeer de virtuele omgeving met het volgende commando:

```bash
Copy code
source myenv/bin/activate
```
Op Windows-systemen is het commando voor het activeren van de virtuele omgeving myenv\Scripts\activate.

Installeer projectafhankelijkheden:
Nu moet je alle projectafhankelijkheden installeren. Typ het volgende commando:

```bash
Copy code
pip install -r requirements.txt
```
Dit commando installeert alle vereiste pakketten en bibliotheken die in het project zijn gespecificeerd.

Voer database migraties uit:
Voer de database migraties uit met behulp van het volgende commando:

```bash
Copy code
python manage.py migrate
```
Dit commando zal de database-schema's maken op basis van de aanwezige migratiebestanden.
  
- Pas settings.py aan
Voeg uw eigen Mailgun accountgegevens toe in settings.py

- Start de ontwikkelingsserver:
Start de ontwikkelingsserver met het volgende commando:

```bash
Copy code
python manage.py runserver
```

De ontwikkelingsserver zal worden gestart op http://localhost:8000/ (of een ander poortnummer indien bezet). Je kunt deze URL openen in een webbrowser om het Django-project in actie te zien.

Gefeliciteerd! Je hebt succesvol een bestaand Django-project gedownload van GitHub en het lokaal opgezet. Je kunt nu aanpassingen maken
