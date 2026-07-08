"""
Dashboard Streamlit : Présentation du projet Big_data_project
Présente les 3 livrables réalisés sur l'environnement collaboratif
JupyterHub déployé sur Azure (VM LIVEcorpsServer) :

1. Configuration de l'environnement data science (VM Azure + JupyterHub)
2. Modèle ML | Prédiction du cancer du sein
3. Modèle ML | Prédiction de maladie basée sur l'expression de gènes
4. Pipeline de collecte de flux RSS (France Info) vers CSV

    
"""

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Big_data_project | Dashboard",
    page_icon="",
    layout="wide",
)


# Sidebar :navigation

st.sidebar.title("Big_data_project")
page = st.sidebar.radio(
    "Sections",
    [
        "Vue d'ensemble",
        "Environnement (Azure + JupyterHub)",
        "Modèle 1 : Cancer du sein",
        "Modèle 2 : Maladie génétique",
        "Pipeline flux RSS",
    ],
)

st.sidebar.markdown("---")
st.sidebar.caption("Projet réalisé sur une VM Azure (Brazil South) "
                    "avec JupyterHub collaboratif, authentification GitHub OAuth.")


# Page 1 : Vue d'ensemble
if page == "Vue d'ensemble":
    st.title("Big_data_project : Vue d'ensemble")
    st.write(
        "Ce projet répondait à quatre objectifs : mettre en place un "
        "environnement collaboratif de data science sur une VM Azure, "
        "puis produire deux modèles de Machine Learning et un pipeline "
        "de collecte de données."
    )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Environnement", "VM Azure", "JupyterHub")
    col2.metric("Modèle cancer du sein", "97.37 %", "accuracy")
    col3.metric("Modèle maladie génétique", "98.82 %", "accuracy")
    col4.metric("Flux RSS collectés", "3", "économie / société / sciences")

    st.markdown("### Les 4 livrables")
    st.markdown(
        """
        1. **Infrastructure** : VM Ubuntu sur Azure, JupyterHub multi-utilisateurs
           avec authentification GitHub OAuth.
        2. **Modèle 1** : Random Forest pour prédire si une tumeur est bénigne
           ou maligne, à partir de 30 caractéristiques médicales.
        3. **Modèle 2** : Random Forest pour prédire la présence d'un cancer
           à partir de l'expression de plus de 20 000 gènes.
        4. **Pipeline RSS** : Collecte continue d'articles France Info
           (économie, société, sciences) vers des fichiers CSV.
        """
    )


# Page 2 : Environnement Azure / JupyterHub
elif page == "Environnement (Azure + JupyterHub)":
    st.title(" Environnement collaboratif |Azure & JupyterHub")

    st.markdown("### Infrastructure déployée")
    col1, col2, col3 = st.columns(3)
    col1.metric("Fournisseur", "Microsoft Azure")
    col2.metric("Région", "Brazil South")
    col3.metric("OS", "Ubuntu 22.04")

    st.markdown("### Étapes clés de la mise en place")
    st.markdown(
        """
        - Création de la VM (`LIVEcorpsServer`) et configuration SSH
        - Installation de JupyterHub dans un environnement virtuel Python dédié
          (pour éviter les conflits avec les paquets système Debian)
        - Mise en place du proxy HTTP obligatoire (`configurable-http-proxy`)
        - Configuration d'un service `systemd` pour un démarrage automatique
        - Authentification via **GitHub OAuth**, avec création automatique
          des comptes système au premier login
        """
    )

    st.markdown("### Logique d'accès")
    access_df = pd.DataFrame(
        {
            "Utilisateur": [
                "Membre de l'organisation GitHub",
                "Externe ponctuel (liste blanche)",
                "Personne non listée",
            ],
            "Membre de l'org GitHub ?": ["Oui", "Non", "Non"],
            "Dans allowed_users ?": ["Non", "Oui", "Non"],
            "Accès": ["Autorisé", "Autorisé", "Refusé"],
        }
    )
    st.table(access_df)

    st.markdown("### Difficultés rencontrées et résolues")
    with st.expander("Voir le détail des problèmes techniques résolus"):
        st.markdown(
            """
            - **Restrictions de région Azure for Students** : seules 5 régions
              étaient autorisées par la politique de l'abonnement.
            - **Conflit pip / paquets Debian** : résolu via un environnement
              virtuel Python isolé (`/opt/jupyterhub-env`).
            - **Permissions sur le cookie secret** : fichier recréé avec les
              bons droits (`chmod 600`, propriétaire `root`).
            - **Création automatique des comptes système** : un hook
              `pre_spawn_hook` crée l'utilisateur Linux dès la première
              connexion GitHub réussie.
            """
        )


# Page 3 : Modèle Cancer du sein
elif page == "Modèle 1 : Cancer du sein":
    st.title("Modèle 1 : Prédiction du cancer du sein")

    st.markdown(
        "**Objectif** : prédire si une tumeur est bénigne (B) ou maligne (M) "
        "à partir de caractéristiques médicales mesurées sur des cellules."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Patients", "569")
    col2.metric("Variables (features)", "30")
    col3.metric("Accuracy du modèle", "97.37 %")

    st.markdown("### Répartition des diagnostics")
    repartition_df = pd.DataFrame(
        {"Diagnostic": ["Bénin (B)", "Malin (M)"], "Nombre de patients": [357, 212]}
    )
    st.bar_chart(repartition_df.set_index("Diagnostic"))
    st.caption("357 tumeurs bénignes (62.7 %) contre 212 malignes (37.3 %).")

    st.markdown("### Méthodologie")
    st.markdown(
        """
        - **Algorithme** : Random Forest (100 arbres)
        - **Sélection de variables** : `SelectKBest` (toutes les 30 variables
          conservées, le dataset étant déjà compact)
        - **Découpage** : 80 % entraînement / 20 % test, stratifié sur le diagnostic
        """
    )

    st.markdown("### Performance du modèle")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Matrice de confusion**")
        cm_df = pd.DataFrame(
            [[72, 0], [3, 39]],
            index=["Réel : Bénin", "Réel : Malin"],
            columns=["Prédit : Bénin", "Prédit : Malin"],
        )
        st.dataframe(cm_df, use_container_width=True)
    with col2:
        st.markdown("**Rapport de classification**")
        report_df = pd.DataFrame(
            {
                "Classe": ["Bénin (B)", "Malin (M)"],
                "Précision": [0.96, 1.00],
                "Rappel": [1.00, 0.93],
                "F1-score": [0.98, 0.96],
            }
        )
        st.dataframe(report_df, use_container_width=True)

    st.markdown("### Top 10 des variables les plus déterminantes")
    st.write(
        "radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, "
        "compactness_mean, concavity_mean, concave points_mean, symmetry_mean, "
        "fractal_dimension_mean"
    )



# Page 4 : Modèle Maladie génétique
elif page == "Modèle 2 : Maladie génétique":
    st.title("Modèle 2 : Prédiction de maladie basée sur les gènes")

    st.markdown(
        "**Objectif** : prédire si un patient est atteint d'un cancer à "
        "partir de son profil d'expression génique (foie)."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Patients", "422")
    col2.metric("Gènes (avant sélection)", "20 530")
    col3.metric("Accuracy du modèle", "98.82 %")

    st.markdown("### Répartition des patients")
    repartition_df = pd.DataFrame(
        {
            "Statut": ["Atteints d'un cancer", "Non atteints"],
            "Nombre de patients": [372, 50],
        }
    )
    st.bar_chart(repartition_df.set_index("Statut"))
    st.caption("372 patients atteints (88.15 %) contre 50 non atteints (11.85 %).")

    st.markdown("### Méthodologie")
    st.markdown(
        """
        - **Algorithme** : Random Forest (200 arbres, `class_weight="balanced"`
          pour compenser le déséquilibre des classes)
        - **Sélection de variables** : `SelectKBest` : réduction de 20 530 à
          **100 gènes** les plus pertinents
        - **Découpage** : 80 % entraînement (337 patients) / 20 % test
          (85 patients), stratifié
        """
    )

    st.markdown("### Performance du modèle")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Rapport de classification**")
        report_df = pd.DataFrame(
            {
                "Classe": ["Non atteint (0)", "Atteint (1)"],
                "Précision": [0.91, 1.00],
                "Rappel": [1.00, 0.99],
                "F1-score": [0.95, 0.99],
            }
        )
        st.dataframe(report_df, use_container_width=True)
    with col2:
        st.markdown("**Résultat global**")
        st.success("84 patients sur 85 correctement classés sur le jeu de test.")

    st.markdown("### Top 10 des gènes les plus déterminants")
    st.write(
        "HMGCLL1, CFP, FBXL18, NDC80, PLVAP, SPC25, TUBE1, CCL23, CDC45, MARCO"
    )

# Page 5 : Pipeline flux RSS

elif page == "Pipeline flux RSS":
    st.title("Pipeline de collecte de flux RSS : France Info")

    st.markdown(
        "**Objectif** : collecter en continu les articles de trois flux RSS "
        "France Info et les stocker dans des fichiers CSV, sans doublons."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Flux suivis", "3")
    col2.metric("Fréquence", "Toutes les 5 min")
    col3.metric("Format de sortie", "CSV")

    st.markdown("### Flux collectés")
    flux_df = pd.DataFrame(
        {
            "Catégorie": ["Économie", "Sciences", "Société"],
            "Source": [
                "franceinfo.fr/economie.rss",
                "franceinfo.fr/sciences.rss",
                "franceinfo.fr/societe.rss",
            ],
            "Fichier de sortie": ["economy.csv", "science.csv", "society.csv"],
        }
    )
    st.table(flux_df)

    st.markdown("### Logique du pipeline")
    st.markdown(
        """
        - Lecture du flux RSS avec `feedparser`
        - Si le fichier CSV existe déjà, comparaison avec la dernière date
          enregistrée pour n'ajouter que les **nouveaux articles** (pas de doublons)
        - Sinon, création du CSV avec toutes les entrées du flux
        - Boucle infinie avec une pause de 5 minutes (`sleep(300)`) entre
          chaque cycle de collecte
        """
    )

    st.markdown("### Explorer un CSV déjà collecté")
    uploaded = st.file_uploader(
        "Glissez un fichier CSV produit par le pipeline (economy.csv, science.csv ou society.csv)",
        type="csv",
    )
    if uploaded is not None:
        df = pd.read_csv(uploaded)
        st.success(f"{len(df)} articles chargés.")
        st.dataframe(df, use_container_width=True)
    else:
        st.info("Aucun fichier chargé pour le moment : uploadez un CSV pour l'explorer ici.")
