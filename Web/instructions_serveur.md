### 1] Se connecter en ssh à la machine virtuelle hébergée chez Rezel

ssh -i .\.ssh\id_ed25519 root@137.194.13.176

ou

ssh -i .\.ssh\id_ed25519 root@hnapp-lxc.rezel.net

(remplacer le path de la clef par le vôtre si besoin)


### 2] Pull les codes sources actuels du projet (si besoin - si il y a eu modification de ce qui se trouve sur le git)

Naviguer vers root/hnapp (en utilisant la commande ls pour voir les fichiers présents dans le répertoire où vous vous trouvez et la commande cd [nom du répertoire] pour naviguer)

Utiliser la commande git pull


### 3] Créer un processus où tournera le serveur

Vous pouvez voir tous les processus qui tournent en faisant screen -ls

Vous pouvez vous rendre dans un processus en faisant screen -r (process id)

Naviguer vers root/hnapp/Web

Utiliser la commande screen

Lancer le serveur en tapant la commande node server.js

Faire ctrl a puis ctrl d