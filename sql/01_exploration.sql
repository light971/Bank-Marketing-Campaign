-- ============================================
-- BANK MARKETING CAMPAIGN — Exploration SQL
-- ============================================

SELECT *
FROM bank;
-- 1. Vue d'ensemble
SELECT COUNT(*) AS total_contacts,
        SUM(CASE WHEN subscribed = 'yes' THEN 1 ELSE 0 END) AS total_conversions,
       ROUND(AVG(CASE WHEN subscribed = 'yes' THEN 1.0 ELSE 0 END) * 100, 2) AS taux_conversion_pct
FROM bank;

-- 2. Taux de conversion par job
SELECT job,
        COUNT(*) AS nb_contacts,
        SUM(CASE WHEN subscribed = 'yes' THEN 1 ELSE 0 END) AS conversions,
       ROUND(AVG(CASE WHEN subscribed = 'yes' THEN 1.0 ELSE 0 END) * 100, 2) AS taux_conversion_pct
FROM bank
GROUP BY job
ORDER BY taux_conversion_pct DESC;

-- 3. Taux de conversion par mois
SELECT month,
        COUNT(*) AS nb_contacts,
       ROUND(AVG(CASE WHEN subscribed = 'yes' THEN 1.0 ELSE 0 END) * 100, 2) AS taux_conversion_pct
FROM bank
GROUP BY month
ORDER BY taux_conversion_pct DESC;

-- 4. Efficacité selon le nb de contacts (point de saturation)
SELECT campaign AS nb_contacts,
        COUNT(*) AS nb_clients,
       ROUND(AVG(CASE WHEN subscribed = 'yes' THEN 1.0 ELSE 0 END) * 100, 2) AS taux_conversion_pct
FROM bank
GROUP BY campaign
HAVING COUNT(*) > 50
ORDER BY campaign;

-- 5. Profil du client idéal (top segments)
SELECT job, marital, education,
        COUNT(*) AS nb_contacts,
       ROUND(AVG(CASE WHEN subscribed = 'yes' THEN 1.0 ELSE 0 END) * 100, 2) AS taux_conversion_pct
FROM bank
GROUP BY job, marital, education
HAVING COUNT(*) > 100
ORDER BY taux_conversion_pct DESC
LIMIT 20;

-- 6. Impact de la campagne précédente
SELECT poutcome AS resultat_campagne_precedente,
        COUNT(*) AS nb_clients,
       ROUND(AVG(CASE WHEN subscribed = 'yes' THEN 1.0 ELSE 0 END) * 100, 2) AS taux_conversion_pct
FROM bank
GROUP BY poutcome
ORDER BY taux_conversion_pct DESC;