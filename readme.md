# Observatoire Immobilier DVF

Projet d'apprentissage Data Engineering - Analyse des transactions immobilières en France à partir des données DVF (Demandes de Valeurs Foncières).

## Objectif du projet

Construire un pipeline de données complet (ingestion → transformation → qualité → API → visualisation) pour analyser les prix immobiliers en France.

**Compétences développées :**
- Data Engineering (Python, PostgreSQL, dbt, Airflow)
- Analytics Engineering (modélisation de données, qualité)
- Backend API (Node.js/NestJS)
- Visualisation (Grafana)

## Stack technique

- **Base de données :** PostgreSQL 15
- **Transformation :** dbt Core
- **Orchestration :** Apache Airflow
- **Ingestion :** Airbyte
- **API :** Node.js / NestJS
- **Visualisation :** Grafana
- **Conteneurisation :** Docker & Docker Compose

## Architecture des données

### Approche ELT (Extract, Load, Transform)

1. **Extract & Load (Python)** : Lecture des fichiers DVF → Chargement en base brute
2. **Transform (dbt)** : Transformation SQL → Modèles analytiques

### Structure des données
```
raw_dvf              (données brutes chargées depuis les fichiers)
├─> staging_dvf      (nettoyage et validation)
├─> dim_communes
├─> fact_transactions
├─> fact_locaux
└─> mart_prix_m2     (métriques calculées)
```

## Installation

### Prérequis

- Docker Desktop installé et démarré
- Git

### Lancement de l'environnement
```bash
# Cloner le projet
git clone [URL_DU_REPO]
cd DVF

# Démarrer les services
docker-compose up -d

# Vérifier que PostgreSQL tourne
docker-compose ps
```

### Connexion à PostgreSQL
Avec DBeaver ou tout client SQL :

- Host : localhost  
- Port : 5432  
- Database : dvf  
- Username : user  
- Password : root  

## Source des données

Les données proviennent du jeu de données officiel **Demandes de valeurs foncières** publié par la DGFiP.  

Caractéristiques :
- Couverture : France métropolitaine et DOM-TOM (hors Alsace, Moselle, Mayotte)
- Période : 5 dernières années (2020-2024)
- Mise à jour : Semestrielle (avril et octobre)
- Format : TXT avec séparateur pipe `|`

## Roadmap d'apprentissage

### Phase 1 : Fondations (Mois 1-2)
- Setup environnement Docker + PostgreSQL
- Exploration et compréhension des fichiers DVF
- Premier script Python d'ingestion
- Création table raw_dvf

### Phase 2 : Transformation (Mois 3-4)
- Setup dbt Core
- Modèles staging
- Modèles marts (transactions/locaux)
- Tests de qualité dbt

### Phase 3 : Orchestration (Mois 5-6)
- Setup Airflow
- DAG d'ingestion mensuel
- Intégration dbt dans Airflow

### Phase 4 : API & Visualisation (Mois 7-10)
- API NestJS pour exposer les données
- Dashboards Grafana
- Monitoring de la qualité des données

### Phase 5 : Production (Mois 11-12)
- CI/CD GitHub Actions
- Optimisations performance
- Documentation complète

## Objectifs d'analyse

- Calculer le prix au m² par commune/département
- Suivre l'évolution des prix dans le temps
- Scoring de quartiers
- Détection d'anomalies (prix aberrants)
- Analyse des types de biens (appartements, maisons, terrains)

## Ressources

- Documentation dbt  
- Documentation Airflow  
- Guide data.gouv.fr sur DVF  

## Auteur

Projet réalisé dans le cadre d'un apprentissage du Data Engineering.

## Licence

Données sous Licence Ouverte / Open Licence version 2.0
