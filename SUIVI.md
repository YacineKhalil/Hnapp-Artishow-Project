### Suivi du projet

> TH : tranche horaire (pour tout le groupe)
> TP : travail personnel

***14/02/2024*** TH 1 & 2 : 
- attribution du projet
- première réunion avec les encadrants
- (tout le groupe) premières réflexions sur ce vers quoi nous voulons faire aller le projet, qui offre beaucoup de degrés de liberté

***29/02/2024 - 23/02/2024***  TP:
- (Yacine) MOOC WEB 3.0 Inria semaines 1,2,3 et 4.
- (Yacine) découverte des ontologies et du language SPARQL.

***24/02/2024***  TP:
- (Yacine) test de certaines requêtes simples du language SPARQL sur le site de Wikidata (Wikidata Query Service).

***27/02/2024*** TH supplémentaire :
- (tout le groupe) recherche d'un terrain d'entente entre les membres du groupe quant à la visée du projet puis création de scénarios d'utilisation
- (tout le groupe) constitution du planning en conséquences : identification des tâches clefs, des dépendances entre celles-ci, mise au point sur les compétences déjà acquises par chacun (ou en voie d'acquisition), attribution des tâches, étalement dans le temps de ces dernières

***28/02/2024*** TH 3 & 4 :
- (tout le groupe) finalisation de la feuille de route de notre projet
- présentation aux encadrants

***03/03/2024*** TP :
- (etienne) MOOC WEB 3.0 Inria semaine 1 et 2

***05/03/2024*** TP :
- (etienne) documentation sur ce document du travail déjà effectué par le groupe, création d'un fichier Microsoft Planner (sur la base du planning déjà établi) pour organiser le travail en groupe

***07/03/2024*** TP :
- (Yacine) 1ère prise en main du module NLTK de python pour le NLP, test des fonctions de bases (word_tokenize(), sent_tokenize() pour la tokenisation de phrases/mots, fonctions pour la lemmatisation...etc.)

***11/03/2024*** TP :
- (etienne) recherche d'un module python pour la reconnaissance de texte puis premier programme le mettant en oeuvre

***13/03/2024*** TH :
- (Yacine) recherche d'une bibliothèque qui supporte la langue française (nltk comportait ceratines fonctions comme nltk.pos_tag qui ne supportaient que le russe et l'anglais), utilisation de Spacy et ses fonctions sur un texte simulant une requête en language naturel.
- (Daniel) prise en main de NLKT et de SPARQL : recherche de documentantions, prise en compte des documents fournis par les encadrants

***20/03/2024*** TH:
- (Yacine) programme qui prend une requête utilisateur et trouve les entitées nommées présentes dans cette dernière, puis cherche sur wikipédia le résumé correspondant à chacune de ces entitées nommées.
- (Yacine) programme qui prend un fichier pdf contenant un programme scolaire donné et retourne la liste des mots clés (liste des mots sans les stop words à laquelle on a appliqué la lemmatisation). 
- (Yacine) commencement du développement du Front-end du site.
- (Daniel) prise en main de NLKT et de SPARQL, suivi du MOOC WEB 3.0 Inria

***25/03/2024*** TP:
- (Yacine) prise en main de Neo4j (https://neo4j.com/) qui permet de créer des graphes de connaissances et réfléxion sur la méthode à utiliser pour l'enrichir à partir de la sortie du traitement NLP (entités nommées par exemple) et l'interrogation de la base de donnée Wikidata (ou DBpedia).

***26/03/2024*** TH:
- (Yacine) programme qui permet de donner une liste des objets présents sur Wikidata liés à une entité nommée donnée.
- (Yacine et Etienne) Discussion sur la stratégie à suivre pour faire le lien entre les données externes sur les monuments d'une part, et les données extraites des programmes pédagogiques d'autre part (2 graphes de connaissances distincts liés par des relations)
- (Etienne) lecture de différents papiers sur le sujet du traitement de requêtes en langage naturel pour SPARQL. Réflexions sur un moyen de traiter plus simplement ces requêtes qu'en ayant à utiliser les outils avancés utilisés dans ces papiers.
- (Daniel) prise en main de SPARQLWrapper permettant de traiter les requêtes sparql avec python


***31/03/2024*** TP:
- (Yacine) Page de garde du site web et recherches sur des techniques de conversion d'une base de donnée de phrases en graphe de connaissances

***01/04/2024*** TP:
- (Yacine) Code qui permet de transformer un dataset de phrases en français (fichier csv) en graphe de connaissances, en extrayant les entités à relier et la relation qui les lie, notamment grâce à la définition d'une structure de base pour les phrases en français et qui peut être encore affinée.

***02/04/2024*** TH:
- (Etienne) Réunion avec l'encadrante du projet pour faire un bilan de nos avancements et de nos questionnements. Lecture de papiers sur la génération de requêtes SPARQL à partir du langage naturel.
- (Daniel) Essayer de construire des graphes de connaissances pour ensuite l'utiliser sur wikidata
- (Yacine) Test du code sur un dataset crée de manière manuelle puis recherche d'une manière de transformer un programme pdf en dataset de phrases dans l'optique de construire un graphe de connaissances à partir de ce dataset.

***09/04/2024*** TH:
- (Tout le groupe) Réunion avec l'encadrant du projet pour faire le point sur notre avancement/répartition des tâches et sur nos questionnements.
- (Yacine) Réalisation d'un code permettant l'obtention d'un dataset de phrases directement à partir d'un programme pédagogique en pdf afin d'utiliser le résultat comme entrée du code qui donne un graphe de connaissances à partir d'un dataset de phrases. (Le code est fonctionnel mais doit être affiné pour filter les phrases des titres,entêtes et bas de page...etc).

***24/04/2024*** TH:
- (Daniel) développement du serveur
- (Yacine) réflexion sur une méthode permettant de combiner les données issues de l'intérrogation de Wikidata d'une part et des données issues des programmes scolaires; afin de garantir l'inter-opérabilité et d'éviter certaines difficultés liées à la multitudes des formats des données. J'ai pensé à structurer les données des programmes pédagogiques en RDF (pour rester cohérent avec les données de Wikidata). J'ai commencé à coder le code qui permet de tester cela. 
- (Yacine) avancement sur le développement du Frontend, en attente du serveur fait avec Flask par Daniel pour tester.

***02/05/2024*** TH:
- (Tout le groupe) Réunion à mi-parcours avec les encadrants du projet:
	-Présentation de l'avancement du projet.
	-Discussion à propos de quelques difficultés rencontrées --> on a décidé d'organiser prochainement un
	rendez-vous pour faire un point sur entre autres le traitement automatique des Pdfs et le chapitre 10 du
	livre de NLTK (Analysing the meaning of sentences).
	-Discussion entre les membres du groupe sur les tâches à venir et celles à prioriser.

***14/05/2024*** TP:
- (Yacine et Daniel) Réunion avec l'encadrante qui nous a éclairé sur certains points notamment le chapitre 10 de NLTK (Analyzing the meaning of sentences) et nous a montré une bibliothèque alternative pour le traitement des pdfs.

***15/05/2024*** TH:
- (Yacine) 
	- Travail sur un code qui permet d'avoir un fichier sous format rdf à partir d'un dataset de phrases (.csv); de chaque phrase est extrait les 2 entités à relier par une relation puis le fichier .rdf est enrichi au fur et à mesure. Code fonctionnel.
	- Utilisation d'un site pour visualiser la sortie du code sous forme d'un graphe.

- (Yacine) Réflexion et tests de structures de requêtes SPARQL destinées à interroger le fichier .rdf
- (Daniel) Réflexion sur la conversion texte -> requête SPARQL à partir de la définition d'une grammaire formelle, tests effectués à partir des chapitre 9 et 10 du livre de NLTK

***29/05/2024*** TH:
- (Tout le groupe) Séance d'audits des projets
	Présentation de notre projet à deux groupes d'auditeurs distincts
	Réciproquement, audit de deux projets par chacun des membres de notre groupe.

***05/06/2024*** TH:
- (Yacine) Adaptation du serveur Flask au pages html du site Web et ajout des fichiers css.
- (Yacine) Test du serveur dans un autre appareil et écriture d'un petit guide qui récapitule comment faire.
- (Daniel) Lecture du livre NLTK et test des outils de NLTK pour des phrases en français grâce à Stanford PoS Tagger

***11/06/2024*** TP:
- (Yacine) étude d'une manière d'intégrer l'affichage des relations liant les noeuds du graphe de connaissances crée à partir du dataset de phrases (fichier rdf visualisé avec rdf grapher) mais plusieurs erreurs dans le nouveau code que je n'ai pas pu régler.

***12/06/2024*** TH:
- (Yacine) Suite du travail sur la nouvelle version du code (dossier dataset_en_rdf_new_version) et utilisation d'une partie d'un ancien code que j'avais réalisé (Developpement/graphe_de_connaissances/
construction_graphe.py) pour extraire les relations, correction des erreurs rencontrées hier après plusieurs tests. Le nouveau rendu pdf est aussi disponible dans le dossier dataset_en_rdf_new_version.
- (Daniel) Fabrication d'une première version du poster

***13/06/2024*** TP:
- (Daniel) Réunion avec l'encadrante pour faire le point sur les grammaires et voir comment générer du code intermédiaire python afin de compléter les grammaires.

***18/06/2024*** TP:
- (Tout le groupe) Préparation de deux posters pour la présentation du projet lors de la semaine finale.

***19/06/2024*** TP:
- (Etienne) Finalisation du poster de présentation du projet.

***21/06/2024*** TP:
- (Yacine) Amélioration du code de traitement des requêtes en language humain et correction de certaines erreurs.
- (Yacine) Recherche de manuels scolaires au format Pdf et d'une technique pour obtenir des tables de phrases (.csv) à partir de ces derniers.

***23/06/2024*** TP:
- (Yacine) Ajout des manuels scolaires et extraction des données dans des fichiers .txt, puis tokenisation pour obtenir des phrases séparées dans les tables .Csv.

***24/06/2024*** TH:
- (Tout le groupe) Réunion entre membres puis avec Maria Boritchev (encadrante du projet) pour discuter des avancées du projet et se fixer sur les objectifs de la dernière semaine. Création en conséquence d'un planning.
- (Yacine) Nettoyage du dataset relatif au manuel d'histoire du CM1 et gestion de plusieurs erreurs.
- (Yacine) Génération du graphe de connaissance représentant toutes les données présentes dans le manuel de CM1
- (Etienne) Analyse des données des fichiers RDF proposés dans la présentation du projet. Ecriture de requêtes SPARQL pour les fonctionnalités interactives du site web (barre de recherches) et intégration à Python. Recherche de manuels scolaires en libre accès. Travail sur le graphisme du front end.
- (Daniel) Ajout d'outils pour l'exploration des données au format RDF. Pour obtenir les données connexes à une notion particulière, j'ai ajouté une fonction qui permet de parcourir le graphe au format RDF en profondeur (DFS) et qui retourne les sommets visités sous la forme d'un graphe rdf.


***25/06/2024*** TH et TP:
- (Etienne) Reprise du site, en particulier du serveur - Travail sur le traitement de requêtes côté serveur - Ajout de fonctionnalités d'esthétique pour le front end - Implémentation de reprise sur erreur pour les requêtes mal orthographiées.
- (Yacine) Finalisation des 2 graphes de connaissances des programmes de CM1 et CM2 - Correction de certains programmes et gestions des erreurs et des exceptions.
- (Yacine et Etienne) Tests du serveur et réflexion sur les fonctions supplémentaires à implémenter par la suite.
- (Daniel) Préparation du diaporama pour la présentation finale du projet
- (Daniel) réflexion sur des outils pour exploiter les données au format rdf

***26/06/2024*** TH et TP:
- (Tout le groupe) Réunion avec Maria Boritchev (encadrante du projet) pour faire le point sur nos résultats et pour comprendre ce qui est attendu de nous pour l'évaluation finale.
- (Yacine et Etienne) Redesign/design complet du site - redesign de la page du moteur de recherche et réglages de plusieurs bugs d'affichage - tests d'intégration d'un wrapper pour l'API Gallica (pyGallica) dans notre site (non concluants malheureusement).
- (Yacine) Ajout d'une page qui permet d'afficher au choix les graphes de connaissances des programmes pédagogiques présents dans la base de données - Implémentation de la fonctionnalité qui permet lors de l'affichage des résultats en dessous de la barre de recherche de cliquer sur un mot donnée (ie noeud du graphe de connaissance) et qui ouvre la page correspondante sur Wikidata pour avoir plus d'informations sur ledit mot -  ajout de la fonctionnalité d'affichage des courts descriptifs pour chaque mot de la liste déroulante de résultats au survol de ce dernier par la souris.
- (Etienne) Reprise de la gestion de requêtes avec ajout de nouvelles fonctionnalités, notamment pour la reprise sur erreur afin de permettre un système de requêtes plus interactif - en conséquence, réflexion et écriture de nouvelles requêtes SPARQL - réflexions sur une manière adéquate d'afficher les résultats pour l'utilisateur.

***27/06/2024*** TH et TP:
- (Etienne) Mise en place d'un serveur tournant en continu pour le site - rendez-vous avec les membres de Rezel pour nous aider à utiliser leur solution (hosting.rezel.net)
- (Yacine et Etienne) Tests finaux du site web. 
- (Tout le groupe) Finalisation des slides de la présentation du projet.