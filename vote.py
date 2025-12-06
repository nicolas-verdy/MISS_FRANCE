import streamlit as st
import pandas as pd

# -----------------------
# Données Miss intégrées en JSON
# -----------------------
miss_data = [
  {"Région":"Alsace","Nom_Prénom":"Julie Decroix","Âge":20,"Taille":1.75,"Profession_ou_Études":"Étudiante en psychologie","photo":"Alsace.jpg"},
  {"Région":"Aquitaine","Nom_Prénom":"Aïnhoa Lahitete","Âge":19,"Taille":1.73,"Profession_ou_Études":"Étudiante en droit","photo":"Aquitaine.jpg"},
  {"Région":"Auvergne","Nom_Prénom":"Alice De Lima Guimaraes","Âge":19,"Taille":1.72,"Profession_ou_Études":"Prépa littéraire / étudiante","photo":"Auvergne.jpg"},
  {"Région":"Bourgogne","Nom_Prénom":"Charlène Laurin","Âge":22,"Taille":1.82,"Profession_ou_Études":"Préparatrice en pharmacie","photo":"Bourgogne.jpg"},
  {"Région":"Bretagne","Nom_Prénom":"Ninon Crolas","Âge":18,"Taille":1.71,"Profession_ou_Études":"Étudiante infirmière / ex-sapeur-pompier","photo":"Bretagne.jpg"},
  {"Région":"Centre-Val de Loire","Nom_Prénom":"Anna Valero","Âge":19,"Taille":1.74,"Profession_ou_Études":"Étudiante en médecine","photo":"CentreValLoire.jpg"},
  {"Région":"Champagne-Ardenne","Nom_Prénom":"Ynès Lallemand","Âge":19,"Taille":1.72,"Profession_ou_Études":"Étudiante en droit","photo":"ChampagneArdennes.jpg"},
  {"Région":"Corse","Nom_Prénom":"Manon Mateus","Âge":23,"Taille":1.71,"Profession_ou_Études":"Entrepreneuse (gelateria)","photo":"Corse.jpg"},
  {"Région":"Côte d’Azur","Nom_Prénom":"Luna Maiolino","Âge":19,"Taille":1.75,"Profession_ou_Études":"Étudiante en techniques de commercialisation","photo":"CoteAzur.jpg"},
  {"Région":"Franche-Comté","Nom_Prénom":"Jade Cholley","Âge":19,"Taille":1.77,"Profession_ou_Études":"Étudiante BTS professions immobilières","photo":"FrancheComte.jpg"},
  {"Région":"Guadeloupe","Nom_Prénom":"Naomi Torrent","Âge":30,"Taille":1.77,"Profession_ou_Études":"Double master en management & ingénierie financière","photo":"Guadeloupe.jpg"},
  {"Région":"Guyane","Nom_Prénom":"Alicia Mertosetiko","Âge":20,"Taille":1.73,"Profession_ou_Études":"Étudiante BTS professions immobilières & handballeuse","photo":"mettre url miss + Guyane"},
  {"Région":"Île-de-France","Nom_Prénom":"Mareva Michel","Âge":21,"Taille":1.78,"Profession_ou_Études":"Étudiante école de commerce (ESSEC)","photo":"mettre url miss + Île-de-France"},
  {"Région":"Languedoc","Nom_Prénom":"Lou Lambert","Âge":19,"Taille":1.72,"Profession_ou_Études":"Étudiante en droit","photo":"mettre url miss + Languedoc"},
  {"Région":"Limousin","Nom_Prénom":"Aloïce Sejotte","Âge":24,"Taille":1.74,"Profession_ou_Études":"Maroquinerie de luxe / ex-BTS mode","photo":"mettre url miss + Limousin"},
  {"Région":"Lorraine","Nom_Prénom":"Camille L’Étang","Âge":23,"Taille":1.72,"Profession_ou_Études":"Infirmière en cancérologie","photo":"mettre url miss + Lorraine"},
  {"Région":"Martinique","Nom_Prénom":"Léaline Patry","Âge":21,"Taille":1.71,"Profession_ou_Études":"Étudiante stylisme-modélisme","photo":"mettre url miss + Martinique"},
  {"Région":"Mayotte","Nom_Prénom":"Kamillat Hervian","Âge":24,"Taille":1.73,"Profession_ou_Études":"—","photo":"mettre url miss + Mayotte"},
  {"Région":"Midi-Pyrénées","Nom_Prénom":"Léa Chabrel","Âge":24,"Taille":1.7,"Profession_ou_Études":"Ostéopathe / ancienne sportive","photo":"mettre url miss + Midi-Pyrénées"},
  {"Région":"Nord-Pas-de-Calais","Nom_Prénom":"Lola Lacheré","Âge":20,"Taille":1.74,"Profession_ou_Études":"Étudiante marketing / ex-volleyball","photo":"mettre url miss + Nord-Pas-de-Calais"},
  {"Région":"Normandie","Nom_Prénom":"Victoire Dupuis","Âge":19,"Taille":1.7,"Profession_ou_Études":"Étudiante en communication","photo":"mettre url miss + Normandie"},
  {"Région":"Nouvelle-Calédonie","Nom_Prénom":"Juliette Collet","Âge":23,"Taille":1.7,"Profession_ou_Études":"Étudiante (sciences)","photo":"mettre url miss + Nouvelle-Calédonie"},
  {"Région":"Pays de la Loire","Nom_Prénom":"Lola Winter","Âge":19,"Taille":1.71,"Profession_ou_Études":"Étudiante en droit","photo":"mettre url miss + Pays de la Loire"},
  {"Région":"Picardie","Nom_Prénom":"Emma Boivin","Âge":24,"Taille":1.77,"Profession_ou_Études":"Étudiante infirmière / danseuse","photo":"mettre url miss + Picardie"},
  {"Région":"Poitou-Charentes","Nom_Prénom":"Agathe Michelet","Âge":26,"Taille":1.74,"Profession_ou_Études":"Chirurgien-dentiste","photo":"mettre url miss + Poitou-Charentes"},
  {"Région":"Provence","Nom_Prénom":"Julie Zitouni","Âge":26,"Taille":1.72,"Profession_ou_Études":"Entrepreneuse / mannequin","photo":"mettre url miss + Provence"},
  {"Région":"Réunion","Nom_Prénom":"Priya Padavatan","Âge":19,"Taille":1.7,"Profession_ou_Études":"Étudiante en droit","photo":"mettre url miss + Réunion"},
  {"Région":"Rhône-Alpes","Nom_Prénom":"Noémie Baiamonte","Âge":21,"Taille":1.71,"Profession_ou_Études":"Étudiante cinéma / maquilleuse envisagée","photo":"mettre url miss + Rhône-Alpes"},
  {"Région":"Roussillon","Nom_Prénom":"Déborah Adelin-Chabal","Âge":18,"Taille":1.75,"Profession_ou_Études":"Étudiante en langues / danseuse pro","photo":"mettre url miss + Roussillon"},
  {"Région":"Tahiti","Nom_Prénom":"Hinaupoko Deveze","Âge":23,"Taille":1.82,"Profession_ou_Études":"Secrétaire administrative / organisatrice de séjours / mannequin","photo":"mettre url miss + Tahiti"}
]

df_miss = pd.DataFrame(miss_data)

# -----------------------
# Initialisation session_state
# -----------------------
if "favorites" not in st.session_state:
    st.session_state.favorites = []

if "vote_12" not in st.session_state or not isinstance(st.session_state.vote_12, list):
    st.session_state.vote_12 = []

# -----------------------
# Sidebar / navigation
# -----------------------
option = st.sidebar.selectbox("Navigation", ["Accueil", "Les miss", "Mes favorites", "Mon vote"])

# -----------------------
# Page Accueil
# -----------------------
if option == "Accueil":
    st.title("Bienvenue à la soirée Miss France 2026 ! 🎉")
    st.image("photogroupe.png", use_container_width=True)
    st.markdown("""
    Bonjour à tous et bienvenue à notre soirée spéciale **Miss France 2026** !  
    Merci à **Mag et Cédric** pour leur accueil chaleureux.  
    Bonne chance à tous les votants ! Amusez-vous bien !
    """)
    st.balloons()
    if st.button("Commander à boire 🍹"):
        st.snow()
        st.success("Votre commande imaginaire est en route ! Profitez bien 😉")

# -----------------------
# Option 1 : Les miss
# -----------------------
elif option == "Les miss":
    st.header("Liste des candidates Miss France 2026")
    
    df_miss_sorted = df_miss.sort_values(by="Région").reset_index(drop=True)
    
    for idx, row in df_miss_sorted.iterrows():
        cols = st.columns([1,3,3,2,2])
        with cols[0]:
            st.image(row['photo'], use_container_width=True)
        with cols[1]:
            st.write(f"**{row['Nom_Prénom']}**")
        with cols[2]:
            st.write(f"Région: {row['Région']}")
        with cols[3]:
            st.write(f"Âge: {row['Âge']}")
        with cols[4]:
            st.write(f"Taille: {row['Taille']} m\n{row['Profession_ou_Études']}")
        
        label = "❤️ Retirer" if row['Région'] in st.session_state.favorites else "🤍 Ajouter"
        if st.button(label, key=f"fav_{idx}"):
            if row['Région'] in st.session_state.favorites:
                st.session_state.favorites.remove(row['Région'])
            else:
                st.session_state.favorites.append(row['Région'])

# -----------------------
# Option 2 : Mes favorites
# -----------------------
elif option == "Mes favorites":
    st.header("Mes régions favorites")
    if st.session_state.favorites:
        for region in st.session_state.favorites:
            st.write(f"❤️ {region}")
    else:
        st.info("Vous n'avez pas encore ajouté de favorites.")

# -----------------------
# Option 3 : Mon vote simplifié
# -----------------------
elif option == "Mon vote":
    st.header("Mon vote par région (sélection libre)")

    cols = st.columns(6)
    for idx, region in enumerate(df_miss['Région'].unique()):
        label = f"✅ {region}" if region in st.session_state.vote_12 else region
        if cols[idx % 6].button(label, key=f"vote_{idx}"):
            if region in st.session_state.vote_12:
                st.session_state.vote_12.remove(region)
            else:
                st.session_state.vote_12.append(region)
    
    st.write(f"Nombre de régions sélectionnées : {len(st.session_state.vote_12)}")
    
    if st.button("Réinitialiser mon vote"):
        st.session_state.vote_12 = []
        st.success("Vote réinitialisé !")




# -----------------------
# Fin
# -----------------------     streamlit run vote.py
