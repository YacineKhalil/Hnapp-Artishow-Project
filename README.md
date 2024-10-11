# Sommaire

1. Point de départ du projet
    1. Cadre et membres
    2. Présentation du sujet
    3. Attendus

2. Poster de présentation

3. Tester notre outil

## Cadre et membre

Ce projet a été réalisé en 2024 dans le cadre de la formation d'ingénieurs (première année) de Télécom Paris.

Adresse mail des participants :

etienne.pelissier@telecom-paris.fr

daniel.berda@telecom-paris.fr

yacine.khalil@telecom-paris.fr


## Présentation du sujet

La France bénéficie d’un riche héritage culturel, dont des musées et leurs oeuvres, monuments et sites
de réputation mondiale.

Mondialement, le secteur culturel a depuis une dizaine d’années entrepris de produire et diffuser
des données liées à ses activités, en particulier des données sur les oeuvres et les artistes.
Cela donne lieu à la publication de graphes de connaissances, mais aussi à de nombreuses données
de référence -comme celles de la Bibliothèque Nationale de France [1]-, à des données encyclopédiques
-comme Wikidata [3]- et à des bases d’images.

Des programmes scolaires sont publiés et peuvent être reliés à des resources culturelles. Par ailleurs,
de nombreuses activités pédagogiques sont organisées autour des richesses culturelles de nos territoires;
ces activités sont souvent décrites dans des fiches pédagogiques [2].

L’idée de ce projet est d’exploiter ces données -exprimées dans des graphes de connaissances-,
en relation avec les programmes scolaires, pour faciliter la production et la recherche de ressources
pédagogiques en lien avec les données décrivant notre héritage culturel. Cette exploitation cherchera
à tirer parti des évolutions des techniques les plus récentes de traitement des données: NLP (Natural
Language Processing), IA -génératives ou autres-, graphes de connaissances, analyses d’images...


## Attendus

Le but du projet est de mettre en place une plateforme web ou logicielle permettant de visualiser et
d’explorer des données culturelles, décrites ci-dessus et de les mettre en relation avec les programmes
scolaires et des fiches pédagogiques.
Le groupe de travail fera des expérimentations dans un premier temps pour prendre en main les
méthodes existantes, puis pourra, en concertation avec l’encadrant, développer une stratégie d’exploitation
de ces méthodes pour proposer des fonctionnalités utiles à des enseignants, à des étudiants ou à des
vulgarisateurs.
Le rendu prendra la forme d’une interface de recherche, de visualisation et éventuellement de production, en python ou en JavaScript, permettant de mettre en oeuvre tout ou partie des fonctionnalités
ci-dessus. Le groupe de travail utilisera git pour mettre le code en commun.


### Références

[1] Bnf. https://data.bnf.fr/. Accédé le: 2024-07-01.

[2] Resources pédagogiques du portail ’histoire des arts’. https://data.culture.gouv.fr/explore/dataset/ressources-pedagogiques-pour-lenseignement-de-lhistoire-des-arts/information/. Accédé le: 2024-07-01.

[3] Wikidata. https://www.wikidata.org/wiki/Wikidata:Main_Page. Accédé le: 2024-07-01.


## Poster de présentation de notre projet

![Poster HNApp](Documentation/Poster/Poster%20HNApp.jpg)

## Slides de présentation de notre projet

https://docs.google.com/presentation/d/1tayHOq1bl3JCxpBVEWiqWfeZHt3llslXKrG0hK0Q9Tk/edit?usp=sharing

## Tester notre outil

### Jusqu'au 01/07/2024

Utiliser votre moteur de recherche pour vous rendre sur hnapp.rezel.net

Vous pouvez tester notre outil !

### À partir du 01/07/2024

Vous pouvez toujours essayer notre outil en local !

Téléchargez le répertoire Web de notre projet au format zip

Décompressez le fichier téléchargé et naviguez vers le dossier Web

Ouvrez un terminal dans ce dossier (Windows 11: clic droit dans le dossier puis "Ouvrir dans le Terminal")

Entrez la commande node server.js dans ce terminal (si node n'est pas téléchargé sur votre pc, suivez les instructions ci-présentes https://nodejs.org/fr/download/package-manager)

Assurez-vous que vous avez bien python sur votre machine

Ouvrez votre moteur de recherches et rentrez dans la barre de recherche : localhost:3000

> Vous obtiendrez probablement des erreurs dûes au manque de certaines bibliothèques python sur votre machine
>
> Si c'est le cas : rouvrez votre onglet terminal et installez les packages nécessaires (python pip install nom_du_package)

Vous pouvez tester notre outil !