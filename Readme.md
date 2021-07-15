# Dove Giocare (a Roma)</br>

Semplice programma python per scaricare una mappa dei punti per il gioco a quota fissa autorizzati </br>
L'applicazione si basa sui dati forniti al pubblico da ADM tramite l'applicazione [dove si gioca](https://www.adm.gov.it/portale/monopoli/giochi/giochi_sport/scommesse_fissa/quota-fissa_dove) . </br>
Per utilizzare l'applicazione vanno prima scaricati i dati dei punti relativi alla provincia di Roma, per farlo utilizzare: </br>
`python3 main.py ` </br>
QUesto creerà il file data.json all'interno della cartella del progetto, all'interno del file possiamo trovare per ogni comune (indicato tramite il codice catastale) l'indirizzo dei punti vendita riconosciuti da ADM. </br>
Oltre al download e la compilazione dei dati in data.json è previsto un servizio per farsi restituire queste informazioni. </br>
Per farlo vi è un servizio esposto tramite Flask sulla porta 5000 al path `/` del server. Per avviare il servizio eseguire: </br>
`python3 app.py` </br>
Dopo di che con un client si possono eseguire una `GET` per avere indietro il data.json precedentemente calcolato.

# TO-DO
1. Predisporre main.py per essere eseguito come un cronjob per l'aggiornamento del file data.json (che dovrebbe cambiare lentamente nel tempo)
2. Refactoring per calcolare i punti vendita di regioni e province diverse