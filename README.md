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
BANK-MARKETING-CAMPAIGN/
│
├── 📁 data/
│   ├── 📁 external/
│   │   └── .gitkeep
│   ├── 📁 processed/
│   │   ├── bank_clean.csv
│   │   ├── bank_scored.csv
│   │   └── bank_segmented.csv
│   └── 📁 raw/
│       ├── .gitkeep
│       └── bank.csv
│
├── 📁 docs/
│   ├── Connex_postgreSql.md
│   └── Connexion_github.md
│
├── 📁 notebooks/
│   ├── 01_eda_partie1.ipynb
│   ├── 02_eda_partie2.ipynb
│   ├── 03_eda_partie3.ipynb
│   └── 04_dashboard_prep.ipynb
│
├── 📁 outputs/
│   ├── 📁 figures/
│   │   └── Bank_Marketing_Campaign.png
│   └── 📁 tables/
│
├── 📁 reports/
│   ├── dashboard.pbix
│   └── Dashboard_Marketing_Campaign.pdf
│
├── 📁 scripts/
│   ├── data_loader.py
│   └── viz_helpers.py
│
├── 📁 sql/
│   └── 01_exploration.sql
│
├── 📄 requirements.txt
└── 📄 README.md
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

| Insight | Résultat | Impact business |
|---|---|---|
| Scoring de propension | Le modèle (Gradient Boosting, AUC = 0,78 en validation croisée 5 folds) classe efficacement les leads : **16 %** de conversion dans le décile le plus bas, **90 %** dans le plus haut | Les 30 % de clients les mieux scorés concentrent **52 %** des conversions |
| Anciens souscripteurs | Les clients ayant souscrit lors d'une campagne précédente convertissent à **91 %**, soit 1,9 fois la moyenne (47 %) | Liste prioritaire à contacter dès le lancement (1 071 clients) |
| Point de saturation | 53 % de conversion au 1er contact, plateau autour de 46 % aux 2e et 3e, puis **41 %** dès le 4e et moins de 30 % au-delà de 8 | Limiter les relances à 3 contacts par prospect |
| Timing | Mai concentre **25 %** des appels mais affiche le pire taux (33 %). Mars, septembre, octobre et décembre dépassent 80 %, mais sur seulement 10 % des contacts | Mieux étaler les appels au lieu de concentrer l'effort sur mai |
| Profil client | Étudiants (75 %) et retraités (66 %) convertissent le mieux ; le profil « étudiant / secondaire / célibataire » atteint **80 %** | Adapter le discours et le ciblage à ces profils |
| Valeur client | Les clients au solde bancaire élevé (quartile supérieur) convertissent à **57 %**, contre 36 % pour le quartile inférieur | Le solde est un critère de priorisation simple à utiliser |

## Recommandations marketing

1. **Prioriser les appels selon le score** : commencer par les 3 déciles supérieurs (30 % des clients, 52 % des conversions), puis descendre dans le classement tant que le coût par appel reste rentable.
2. **Contacter en priorité absolue les anciens souscripteurs** : 91 % de conversion, c'est le levier le plus fort et le moins coûteux de la campagne.
3. **Limiter les relances à 3 contacts** : au-delà, le taux de conversion baisse nettement et chaque appel supplémentaire coûte plus qu'il ne rapporte.
4. **Rééquilibrer le calendrier** : réduire la concentration des appels en mai (25 % du volume, 33 % de conversion) et tester des vagues d'appels sur les mois plus performants.
5. **Privilégier le mobile** : le canal cellulaire convertit légèrement mieux que le fixe (54 % vs 50 %), et c'est le canal majoritaire de la campagne.

## ⚠️ Limites

- **Dataset rééquilibré** : cette version Kaggle compte 47 % de conversions, contre environ 12 % dans le dataset UCI d'origine. Les taux absolus sont donc gonflés ; ce sont les écarts entre segments qui comptent.
- **Durée d'appel exclue du modèle** : elle n'est connue qu'après l'appel et fausserait le scoring (fuite de données).
- **Scores calculés hors échantillon** (validation croisée) : chaque client est scoré par un modèle entraîné sans lui.
- **Biais de sélection possible sur les mois** : les mois peu sollicités ont pu cibler des clients déjà chauds. Leur taux élevé ne garantit pas le même résultat à plus grande échelle.
- **Pas de données de coûts** : le ROI est estimé à partir des taux de conversion, pas d'un calcul financier réel.

---

## 🛠️ Stack technique

| Domaine | Outils |
|--------|--------|
| Langage | Python 3.12.7 |
| Manipulation données | Pandas, NumPy |
| Visualisation | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| SQL | PostgreSQL / BigQuery |
| Dashboard | Power BI / Looker Studio |
| Environnement | Jupyter Notebook |

---

## Lancer le projet

```bash
# Cloner le repo
git clone https://github.com/light971/Bank-Marketing-Campaign.git
cd Bank-Marketing-Campaign

# Installer les dépendances
pip install -r requirements.txt

# Lancer le notebook
jupyter notebook notebooks/01_eda_partie1.ipynb
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
