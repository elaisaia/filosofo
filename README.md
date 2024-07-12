# Tutorial di Installazione dell'App Python

Questo tutorial guida attraverso l'installazione passo dopo passo dell'applicazione Python. Segui attentamente ogni fase per assicurarti che l'installazione avvenga senza problemi.

## Prerequisiti

Prima di iniziare, assicurati di avere una connessione internet attiva per scaricare i file necessari.

## 1. Download di Python

Python è il linguaggio di programmazione necessario per eseguire l'applicazione. Segui questi passi per installarlo:

1. Vai al link per scaricare Python: [Python 3.9.8](https://www.python.org/ftp/python/3.9.8/python-3.9.8-amd64.exe)
2. Una volta scaricato il file `python-3.9.8-amd64.exe`, apri il file e segui le istruzioni di installazione.
3. Assicurati di selezionare l'opzione **"Add Python 3.9 to PATH"** durante l'installazione per facilitare l'esecuzione dei comandi Python dal terminale.

## 2. Download e Installazione di Ollama

Ollama è necessario per alcune funzionalità dell'applicazione. Segui questi passi per installarlo e preparare il modello necessario:

### Download di Ollama

1. Visita il sito [Ollama](https://ollama.com/download) per scaricare il software.
2. Segui le istruzioni per installare Ollama sul tuo computer.

### Download del Modello

1. Apri il terminale cmd di Windows.
2. Digita e invia il comando seguente per scaricare il modello necessario:
   ```
   ollama pull mistral
   ```
   
## 3. Installazione delle Librerie

Le librerie Python richieste dall'applicazione devono essere installate prima del suo utilizzo:

1. Apri un terminale.
2. Naviga nella cartella del progetto utilizzando il comando `cd`, ad esempio:
   ```
   cd Percorso/alla/cartella/del/progetto/local-rag-volterra
   ```
3. Installa le librerie richieste eseguendo il comando:
   ```
   pip install -r requirements.txt
   ```

## 4. Avviare l'Applicazione

Una volta completata l'installazione di Python, Ollama e delle librerie necessarie, puoi avviare l'applicazione:

1. Dal terminale, assicurati di essere nella cartella del progetto.
2. Lancia l'applicazione con il comando:
   ```
   streamlit run app.py
   ```
