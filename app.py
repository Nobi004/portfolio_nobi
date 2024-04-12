from pathlib import Path

import streamlit as st
from PIL import Image


#______ PATH SETTINGS ______
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Ai engneer Resume (Nobi).pdf"
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
    "GitHub": "https://github.com/nobi004",
    "Facebook": "https://Facebook.com/nobi04",
    "Kaggle" :  "https://www.kaggle.com/mdmahmudunnobi"
}
PROJECTS = {
    "🏆Resume-Screening-Web-APP": "https://github.com/Nobi004/Resume-Screening-Web-APP.git",
    "🏆Simple-Python-Chat-App": "https://github.com/Nobi004/Simple-Python-Chat-App",
    "🏆Brain-Tumer-Classification": "https://github.com/Nobi004/Brain-Tumer-Classification",
    "🏆Diabetics-prediction": "https://github.com/Nobi004/Diabetics-prediction",
    "🏆Digit-Recognizer ": "https://github.com/Nobi004/Digit-Recognizer",
    "🏆Credit-Card-Fraud-Ditection": "https://github.com/Nobi004/Credit-Card-Fraud-Ditection",
    "🏆object-angle-ditection ": "https://github.com/Nobi004/object-angle-ditection",
    "🏆Hand Gesture/Face/Body-Pose/Iris Ditection": "https://github.com/Nobi004/Conmputer-Vision-openCV-",
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
    st.write("A B O U T M E")
    st.write("""An enthusiastic AI and ML enthusiast and electrical and
electronic engineer, dedicated to using engineering skills to
solve practical problems. Committed to staying on the cutting
edge of technology by studying neural networks and refining
algorithms. Eager to collaborate and contribute significantly
to the development of AI and ML.
""")
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
- ✔️ University of Dhaka
Faridpur Engineering College
Bachelor of Science: Electrical And
Electronics Engineering 4th year
- ✔️AI Quest/jan2024 to ......
Deep Learning And Ai specialization (Runnig)

- ✔️ National Academy for Computer Training
and Research (NACTAR) (Mar-Oct) 2023
Course:Machine Learing and Data Science
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python
- ‍💻Frameworks: TensorFlow, Keras, PyTorch
- ‍💻 Deep Learning: CNNs, RNNs, GANs
- ‍💻 Natural Language Processing : NLTK, GPT
- 📊 Computer Vision: OpenCV,
- 📚 Data Tools: Pandas, NumPy, matplotlib
#- 🗄️ Databases: Postgres, MongoDB, MySQL
"""
)



# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Deep Learning Engineer(Internship) | ArtificialIntelligenceResearch organization**")
st.write("01/04/2024 - Present")
#st.write(
#    """
#- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding marketing initiatives, and supplied recommendations to boost landing page conversion rate by 38%
#- ► Led a team of 4 analysts to brainstorm potential marketing and sales improvements, and implemented A/B tests to generate 15% more client leads
#- ► Redesigned data model through iterations that improved predictions by 12%
#""")


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


# --- L E A D E R S H I P & A W A R D A S ---
st.write('\n')
st.subheader("L E A D E R S H I P & A W A R D A S")
st.write(
    """
- ✔️Awarded 3rd prize at Sylhet Engineering College EEE Fest
2024 for poster presentation titled 'Bridging the gap
between traditional study and AI-enhanced learning'
among 27 competing teams

- ✔️ Joint Secretary at Research and Innovation, overseeing
200 members within the university campus.

- ✔️Senior Executive at Faridpur Engineering College Sports
Association, managing a 500+ member club.


"""
)
