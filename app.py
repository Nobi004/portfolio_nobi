from pathlib import Path

import streamlit as st
from PIL import Image


#______ PATH SETTINGS ______
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "cv.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Mahmudun Nobi"
PAGE_ICON = ":wave:"
NAME = "Mahmudun Nobi"
DESCRIPTION = """
AI Architect: Crafting Intelligent Solutions______, ML-DL Engineer.
"""
EMAIL = "mdmnb435@email.com"
SOCIAL_MEDIA = {
    #"YouTube": "https://youtube.com/c/codingisfun",
    "LinkedIn": "https://linkedin.com/in/nobi04",
    "GitHub": "https://github.com/nobi04",
    "Facebook": "https://Facebook.com/nobi04",
    "Kaggle" :  "https://www.kaggle.com/mdmahmudunnobi"
}
PROJECTS = {
    "🏆Resume-Screening-Web-APP": "https://github.com/Nobi004/Resume-Screening-Web-APP.git",
     #"🏆 Desktop Application - Excel2CSV converter with user settings & menubar": "https://youtu.be/LzCfNanQ_9c",
    # "🏆 MyToolBelt - Custom MS Excel add-in to combine Python & Excel": "https://pythonandvba.com/mytoolbelt/",
}



st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

st.title("Hello there!")


#_________LOAD CSS , PDF & PROFILE PIC __________
with open(css_file) as f :
    st.markdown("<style>{}<style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file :
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)



#________ HERO SECTION _________
col1,col2 = st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data= PDFbyte,
        file_name = resume_file.name,
        mime= "application/octet-stream",
    )
    st.write("📫", EMAIL)


#_____ SOCIAL LINKS _________
st.write("#")
col = st.columns(len(SOCIAL_MEDIA))
for index ,(platform,link) in enumerate(SOCIAL_MEDIA.items()):
    col[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Strong hands on experience and knowledge in Python and Excel
- ✔️ Good understanding of deep learnig ,computr vision ,NLP framework and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Numpy , Pandas )
- ‍💻 Deep learning Frame Work: (Tensorflow,PyTorch)
- ‍💻 Computer Vision : OpenCV ,Pillow
- ‍💻 Natural Language Processing : Nltk
- 📊 Data Visulization: Seaborn,Matplotlib
- 📚 Modeling: Logistic regression, linear regression, decition trees,Neural-Network
- 🗄 Webscriping : BeautifulSoup,Auto-scriper
#- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)



# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Data Analyst | Ross Industries**")
#st.write("02/2020 - Present")
st.write(
    """
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
- ► Redesigned data model through iterations that improved predictions by 12%
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
