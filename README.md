# Birthday_bot
Bot per ricordarsi dei compleanni in famiglia

# Funzionamento
Il bot viene eseguito dal crontab del sistema su cui è ostato per notificare nell'arco della giornata la presenza di un compleanno.
Non sta quindi in ascolto per i messaggi mandati dall'utente, quindi li ignorerà.

# Implementazione
Per la realizzazione è stata utilizzata la libreria telepot e la libreria datatime

# Telepot
Una Libreria per Python che permette di gestire attraverso se stessa un bot di telegram fornendo delle funzioni che si appoggiano alle API di telegram stesso.
E' stata utilizzata per la gestione dei messaggi che un utente e il bot scambiano.

# Datatime
Una libreria che permette di gestire delle variabili di tipo date, è stata usata per prendere il giorno nel formato utile al controllo.

# Installazione e Utilizzo
Per poter eseguire lo script sarà necessario installare le opportune librerie indicate sopra.
Per usufruire del bot è necessario inserire il TOKEN del bot che si può facilmente ottenere tramite il BotFather (Nick: @BotFather) e inserire l'id della vostra chat facilmente visionabile lanciando lo script, mandando un messaggio al bot e leggendo dal terminale il campo chat valore id.
Fatti i dovuti cambiamenti basterà eseguire lo script python e il bot è pronto.
Per rendere il bot sempre attivo senza dover avere una sessione aperta sul pc remoto si può trasformare lo script in un servizio linux mediante la seguente guida: https://github.com/torfsen/python-systemd-tutorial
