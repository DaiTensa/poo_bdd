# Projet Orienté Objet et Base de Données

## Introduction

Ce projet vise à découvrir et utiliser SQLite et SQLAlchemy pour gérer une base de données de livres. 
- Apprendre à créer des tables
- Importer des données
- Exécuter des requêtes SQL via SQLAlchemy
- Développer des fonctionnalités avancées telles que le calcul de statistiques et la gestion de prêts de livres.

## 1. Découverte de SQLite

### 1.1. Différences entre SQLite et les autres moteurs SQL

- **Qu'est ce qui distingue SQLite de la plupart des autres moteurs SQL (PostgreSQL, Oracle, MySQL) ?**
  - SQLite est un moteur de base de données intégré, autonome, sans serveur, et transactionnel. Contrairement à PostgreSQL, Oracle, et MySQL qui nécessitent un serveur séparé, SQLite stocke directement les bases de données dans des fichiers sur le disque.

### 1.2. Avantages et Limitations de SQLite

- **Avantages en termes d'usage :**
  - Simplicité : facile à configurer et utiliser.
  - Portabilité : les bases de données sont stockées dans un seul fichier.
  - Performances : bon pour les applications légères et les environnements embarqués.
  
- **Limitations en termes d'usage :**
  - Concurrence : moins performant pour les applications à haute concurrence.
  - Taille : moins adapté aux très grandes bases de données.

- **Richesse du langage SQL :**
  - SQLite supporte une grande partie de SQL92, mais certaines fonctionnalités avancées des SGBD comme les procédures stockées, les triggers complexes, et les types de données personnalisés peuvent manquer.

### 1.3. Outils recommandés

- **Extension VSCode : "SQLite Viewer"**
  - Permet de visualiser vos tables SQLite directement depuis VSCode.

## 2. Découverte de SQLAlchemy

### 2.1. Qu'est-ce qu'un ORM ?

- **ORM (Object-Relational Mapping)**
  - Un ORM est un outil qui permet de mapper des objets de la programmation orientée objet à des tables de bases de données relationnelles. Il facilite les interactions entre le code et la base de données en fournissant une interface haut niveau.

### 2.2. Avantages de SQLAlchemy

- **Pourquoi utiliser SQLAlchemy par rapport à pymysql, psycopg2 ou sqlite3 ?**
  - SQLAlchemy offre une abstraction plus élevée et facilite les opérations complexes sur les bases de données. Il permet de travailler avec les bases de données de manière déclarative, simplifiant ainsi les opérations CRUD et réduisant la quantité de code boilerplate.

### 2.3. Connecteurs bas niveau vs. haut niveau

- **Différence entre un connecteur de bas niveau (engine) et un connecteur de haut niveau (session) :**
  - `engine` est le point d'entrée bas niveau qui établit la connexion avec la base de données.
  - `session` est une abstraction de plus haut niveau qui gère les transactions et le cycle de vie des objets persistants.

## 3. Créer la table `book` et importer des données

### 3.1. Compléter le code

- **Compléter le code de `code_to_update.py` pour :**
  - Importer les données dans une table SQLite.
  - Définir `ISBN` comme clé primaire.

### 3.2. Vérifications et affichage

- **Vérifier l'importation de 50000 livres avec SQLAlchemy.**
- **Modifier l'affichage d'un livre :**
  - Format : `titre[Auteur](année_publication)`
- **Afficher les livres dont le titre comporte "The Hobbit".**

## 4. Créer les tables `ratings` et `users`

### 4.1. Création et importation de données

- **Créer et importer les données des tables `users` et `ratings`.**

### 4.2. Méthodes statistiques

- **Créer des méthodes pour `Ratings` :**
  - Calculer la moyenne des notes et leur écart type.
- **Créer des méthodes pour `Users` :**
  - Obtenir le nombre de notes, leur moyenne et leur écart type.
- **Créer des méthodes pour `Books` :**
  - Obtenir les statistiques des notes.

## 5. Créer la table `author`

### 5.1. Création de la table des auteurs

- **Créer la table `author` à partir de la table `book`.**
- **Utiliser la librairie `faker` pour ajouter des informations sur les auteurs (année de naissance, de mort, et nationalité).**

### 5.2. Modifier le schéma de la table `book`

- **Faire de l'auteur une clé étrangère pointant vers la table `author`.**

### 5.3. Méthode pour afficher les livres d'un auteur

- **Créer une méthode dans `Author` pour afficher tous les livres d'un auteur.**

## 6. Créer un système de prêts

### 6.1. Création de la table `loan`

- **Créer la table `loan` avec les contraintes suivantes :**
  - ID auto-incrémenté.
  - Référence à un livre s'il est disponible.
  - Référence à un utilisateur s'il n'a pas plus de 5 prêts en cours.
  - Date de début du prêt (date de création du prêt).

### 6.2. Méthode de retour de prêt

- **Créer une méthode pour retourner un prêt :**
  - Statut du prêt passe de "En cours" à "Rendu".
  - Mise à jour de la date de retour.
  - Le livre devient disponible.
  - L'utilisateur a un prêt en moins.

### 6.3. Tests

- **Écrire des tests pour toutes les méthodes créées.**

## 7. Bonus : Système de réservation

### 7.1. Système de réservation

- **Créer un système de réservation.**

## Ressources

- **Documentation SQLAlchemy :**
  - [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)
- **Données :**
  - [Kaggle Books Dataset](https://www.kaggle.com/datasets/saurabhbagchi/books-dataset)


