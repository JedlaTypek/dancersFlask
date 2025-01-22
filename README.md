# Aplikace pro správu databáze tanečníků
## Inicializace aplikace pomocí dockeru
 - Naklonuj repozitář: `git clone https://github.com/JedlaTypek/dancersFlask/`
 - Buildni docker container: `docker build -t flask-app .`
 - Nastartuj docker container: `docker run -p 5000:5000 flask-app`
 - Aplikace běží na localhost:5000 (více v Používání aplikace)
`
## Inicializace aplikace bez použití dockeru
 - Naklonuj repozitář: `git clone https://github.com/JedlaTypek/dancersFlask/`
 - Nainstaluj requirements: `pip install -r requirements.txt`
 - Inicializuj databázi: `alembic -c migrations/alembic.ini -x db=dev upgrade head`
 - Spusť: `flask run`
 - Aplikace běží na localhost:5000 (více v Používání aplikace)

## Updatování databázového schema
Pokud chceš udělat změnu v models.py po změně spusť tyto dva příkazy:
- `./scripts/db_revision_autogen.sh "nazev_zmeny"`
- `alembic -c migrations/alembic.ini -x db=test upgrade head`

## Používání aplikace
### Zobrazení tanečníků
Toto je možné na adrese localhost:5000.
### Přidání tanečníka
Je to možné na adrese localhost:5000/add nebo kliknutím na tlačítko Přidat tanečníka
### Smazání tanečníka
Je možné smazat tanečníka kliknutím na tlačítko smazat na stránce hlavní stránce (localhost:5000)
### Úprava tanečníka
Je možné změnit údaje o tanečníkovi kliknutím na tlačítko upravit. Zobrazí se formulář stejně jako při přidávání tanečníka, akorát jsou šedě zapsána původní data. Pokud nějaké pole nevyplníte zůstane nezměněno.
