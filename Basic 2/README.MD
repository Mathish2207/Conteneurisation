ENTRYPOINT = script toujours exécuté, CMD = arguments par défaut du serveur.

Réseaux Docker
Permettent aux conteneurs de communiquer entre eux de façon isolée.

Volumes Docker
Permettent de stocker les données hors des conteneurs, de façon persistante.

Résumé : réseaux = communication, volumes = persistance.

Stratégie de tagging : major.minor.patch pour versions stables, latest pour déploiement rapide, rollback pour revenir à une version précédente

CONTAINER ID   NAME       CPU %     MEM USAGE / LIMIT     MEM %     NET I/O         BLOCK I/O        PIDS
072d504a75b2   todo-api   0.00%     0B / 0B               0.00%     0B / 0B         0B / 0B          0
169580ad0838   todo-db    0.00%     20.01MiB / 15.54GiB   0.13%     1.26kB / 126B   6.09MB / 414kB   6

