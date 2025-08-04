# To-Do App Completa

# Backend (Flask API)

1. Entra nella cartella `backend`
2. Crea un virtualenv
   python3 -m venv myenv
   Questo crea una cartella myenv con un ambiente Python pulito.

3. attivalo
   source myenv/bin/activate
   Ora il prompt del terminale dovrebbe cambiare per indicarti che sei dentro myenv

4. Installa le dipendenze:
   pip install -r requirements.txt

5. Avvia il server:
   python app.py

6. Il backend gira su `http://127.0.0.1:5000`

---

### Frontend

Apri il file `frontend/index.html` con un browser moderno.

L'app frontend comunica con il backend in Flask per leggere e modificare le attività.

---

### Funzionalità

- Creare attività
- Visualizzare tutte le attività
- Segnare attività come completate / non completate
- Eliminare attività

---

Apri terminale, entra in backend/
Installa Python 3.8+ e dipendenze
Avvia python app.py
Apri frontend/index.html nel browser
Aggiungi, spunta, elimina task e vedi tutto aggiornato in tempo reale

# Problemi

Una nuova protezione di macOS e Homebrew blocca le installazioni di pacchetti Python sul sistema globale per evitare problemi (vedi PEP 668).
Per risolvere in modo semplice e sicuro si usa un virtual environment:
Crea un virtual environment (cartella isolata con Python e pip)

python3 -m venv myenv
Questo crea una cartella myenv con un ambiente Python pulito.

Attiva il virtualenv:

source myenv/bin/activate
Ora il prompt del terminale dovrebbe cambiare per indicarti che sei dentro myenv

Ora installa i pacchetti che ti servono dentro il virtualenv:

pip install --upgrade pip
pip install flask flask-cors flask-sqlalchemy

Esegui il tuo script (es. app.py) dentro questo ambiente
Ogni volta che vuoi lavorare, attiva myenv con:

source myenv/bin/activate
e poi esegui python.

5. Se vuoi uscire dall’ambiente virtuale (da terminale (myenv)):
   deactivate

In questo modo non tocchi Python e pip di sistema (eviti conflitti e permessi) e hai un ambiente isolato con le librerie che ti servono solo per il progetto

# Per inviare le richieste se non si usa Postman

curl -X POST http://127.0.0.1:5000/todos -H "Content-Type: application/json" -d '{"task": "Prova backend"}'

curl -X PUT http://127.0.0.1:5000/todos/1 \
 -H "Content-Type: application/json" \
 -d '{"task":"Comprare il latte fresco","done":true}'
