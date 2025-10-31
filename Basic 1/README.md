Serveur version : 28.5.1
Storage Driver: overlayfs
  driver-type: io.containerd.snapshotter.v1
 Logging Driver: json-file
 Cgroup Driver: cgroupfs
Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 0

CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
DRIVER    VOLUME NAME

REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
quotegen     1.0.0     878d8f267bb9   36 seconds ago   199MB

stop -> arrêter un conteneur en cours d’exécution.
rm -> supprimer un conteneur.
prune -> nettoyage automatique des éléments inutilisés.

copy -> copie dans un Dockerfile des fichiers ou dossiers depuis le PC vers l’image Docker au moment du build.

-v –mount -> monte un fichier ou dossier de ton PC directement dans le conteneur au moment du run.

tags -> Permet de revenir à une version antérieure si un nouveau build casse quelque chose.

ENTRYPOINT et CMD : ENTRYPOINT spécifie le programme principal du conteneur et sa modification n'est pas aisée, alors que CMD propose des paramètres par défaut ou une commande susceptible d'être substituée lors de l'exécution.

Avec une variable d'environnement il est possible d'examiner les variables d'un conteneur actif pour comprendre sa configuration ou ses paramètres.

Assurez-vous que le conteneur a accès à Internet et configurez le proxy de manière appropriée afin que Docker puisse récupérer les images et les dépendances.

Espace disque Docker : Docker met à disposition des outils pour surveiller l'espace que ses images, conteneurs, volumes et caches consomment sur le disque.

--rm fonctionnalité élimine le conteneur après son exécution, empêchant ainsi l'accumulation de conteneurs stoppés et rendant les tests plus aisés.







