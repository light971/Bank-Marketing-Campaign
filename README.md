# Optimisation du Ciblage d'une Campagne de Télémarketing Bancaire

> **Problématique business** : Comment identifier les profils clients les plus susceptibles de souscrire un dépôt à terme, optimiser le timing des contacts et maximiser le ROI d'une campagne de télémarketing ?

---

## Contexte

Une banque portugaise a mené plusieurs campagnes de télémarketing (appels téléphoniques) pour proposer des dépôts à terme à ses clients. Les données couvrent **45 211 contacts** réalisés entre 2008 et 2010.

**Objectif** : Transformer les données brutes de campagne en recommandations marketing actionnables pour améliorer le taux de conversion et réduire le coût par acquisition.

---

## Questions auxquelles ce projet répond

1. Quel est le profil socio-démographique du client qui convertit le mieux ?
2. Quel est le moment optimal pour contacter un prospect (mois, canal) ?
3. À partir de combien de contacts la campagne devient-elle contre-productive ?
4. Quels segments clients prioriser pour maximiser le ROI ?
5. Comment scorer les leads pour guider les équipes commerciales ?

---

## Structure du projet

```
eda_project/
│
├── 📓 notebooks/
│   └── 01_eda_template.ipynb       ← Analyse complète (EDA + scoring)
│
├── 🐍 scripts/
│   ├── data_loader.py              ← Chargement & nettoyage des données
│   └── viz_helpers.py              ← Fonctions de visualisation réutilisables
│
├── 🗄️ sql/
│   └── 01_exploration.sql          ← Requêtes SQL d'exploration business
│
├── 📁 data/
│   ├── raw/                        ← Données brutes originales (non modifiées)
│   ├── processed/                  ← Données nettoyées
│   └── external/                   ← Référentiels et enrichissements
│
├── 📤 outputs/
│   ├── figures/                    ← Graphiques exportés (.png)
│   └── tables/                     ← Tableaux exportés (.csv)
│
└── 📋 reports/                     ← Rapport final + dashboard
```

---

## Méthodologie

### 1. Audit qualité des données
- Détection et traitement des valeurs manquantes (`unknown`)
- Identification des outliers (durée de contact, âge)
- Vérification de la cohérence des variables temporelles

### 2. Analyse Exploratoire (EDA)
- Distribution des variables clés et leur relation avec la conversion
- Analyse bivariée : impact de chaque segment sur le taux de souscription
- Identification des variables les plus discriminantes

### 3. Analyse de la performance campagne
- Taux de conversion par canal, mois et jour de contact
- Courbe d'efficacité selon le nombre de relances (point de saturation)
- Impact des campagnes précédentes sur la conversion actuelle

### 4. Segmentation & Scoring
- Segmentation clients par profil socio-démographique
- Modèle de scoring de propension (Régression Logistique / Random Forest)
- Traduction du score en segments actionnables (Chaud / Tiède / Froid)

### 5. Dashboard de pilotage
- Tableau de bord Power BI avec KPI de suivi de campagne
- Visualisation des segments prioritaires et du ROI estimé

---

## Principaux insights

| Insight | Détail | Impact estimé |
|--------|--------|---------------|
| Timing optimal | Les mois de **mars, septembre et decembre** affichent les meilleurs taux de conversion | +48,30 % vs moyenne |
| Point de saturation | Au-delà de **3 contacts**, le taux de conversion chute drastiquement | Réduction du coût/lead |
| Profil idéal | Clients **retraités et étudiants**, sans défaut de crédit, contactés en cellulaire | Taux de conv. 47% |
| Levier campagne précédente | Les clients ayant **déjà souscrit** lors d'une campagne précédente convertissent 3x plus | Ciblage prioritaire |
| ROI par segment | Le segment "score élevé" représente 0,47% des contacts pour 47% des conversions | Optimisation budget |

---

## 🛠️ Stack technique

| Domaine | Outils |
|--------|--------|
| Langage | Python 3.11 |
| Manipulation données | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| SQL | PostgrSQL / BigQuery |
| Dashboard | Power BI / Looker Studio |
| Environnement | Jupyter Notebook |

---

## Lancer le projet

```bash
# Cloner le repo
git clone https://github.com/light971/bank-marketing-analysis.git
cd bank-marketing-analysis

# Installer les dépendances
pip install -r requirements.txt

# Lancer le notebook
jupyter notebook notebooks/01_eda_template.ipynb
```

**Source des données** : [UCI Machine Learning Repository — Bank Marketing Dataset](https://archive.ics.uci.edu/ml/datasets/Bank+Marketing)  
Le dataset est également disponible sur [Kaggle](https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset).

---

## Recommandations marketing (synthèse)

À l'issue de l'analyse, 5 recommandations concrètes ont été formulées pour l'équipe marketing :

1. **Prioriser les contacts en mars, septembre et octobre** — taux de conversion significativement supérieurs
2. **Limiter les relances à 3 contacts maximum** par prospect pour préserver le ROI
3. **Cibler en priorité les anciens souscripteurs** et les clients sans défaut de crédit
4. **Déployer le score de propension** pour segmenter les leads en 3 niveaux d'effort commercial
5. **Privilégier le canal téléphonie mobile** (cellulaire) au détriment du téléphone fixe

---

## 👤 Auteur

**Malcom Closse** — Marketing Data Analyst | SEO · GEO · Web Analytics

[![LinkedIn](https://img.shields.io/badge/LinkedIn-malcom--closse-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/malcom-closse/)
[![GitHub](https://img.shields.io/badge/GitHub-light971-black?style=flat&logo=github)](https://github.com/light971)
[![Portfolio](https://img.shields.io/badge/Site-Cuisine%20Caribéenne%20Atlas-green?style=flat)](https://cuisine-caribeenne-atlas.fr)

---

*Projet réalisé dans le cadre du développement de mon expertise en Marketing Data Analytics.*
