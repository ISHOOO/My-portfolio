import streamlit as st
from PIL import Image
from base64 import b64encode
from io import BytesIO
from pyperclip import copy
from streamlit_option_menu import option_menu


def jpg_to_base64(path):
    img = Image.open(path)
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    return b64encode(buffered.getvalue()).decode()

def png_to_base64(path):
    img = Image.open(path)
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return b64encode(buffered.getvalue()).decode()

st.set_page_config(layout="wide", page_title="Portfolio Website")
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
pfpspace, biospace=st.columns([2,5])
pfp=jpg_to_base64("assets/pfp.jpg")
with pfpspace: 
    st.markdown(f"""
    <img src="data:image/jpeg;base64,{pfp}" style="border-radius: 50%; width: 250px; height: 250px; object-fit: cover; border: 15px solid #2c2c2c;">
    """,
    unsafe_allow_html=True,)
with biospace:
    st.title("ANANT GUPTA")
    st.write("A Data Science and Analytics enthusiast. Eager to solve real-world business problems by leveraging programming skills for statistical analysis, data visualization. Committed to upskilling and providing actionable insights for data-driven decision making to foster innovation and efficiency ")
    st.write("Here you'll find information about my skills, projects, and how to get in touch with me.")
    with open("Anant_Gupta_Data_analyst.pdf", "rb") as f:
        pdf_data = f.read()
    buttons=st.columns([19,26.5,60])
    with buttons[0]:
        if copied:=st.button("Copy Email"):
            copy("anantgupta08460@gmail.com")
            st.toast("Copied email address to clipboard. Now use it to contact me via email.")
            copied=False
    with buttons[1]:
        st.download_button(label="Download Resume", data=pdf_data, file_name="Anant_Gupta_Data_analyst.pdf",mime="application/pdf")   
st.write("##")
socialmedia = st.columns(6)
with socialmedia[0]: st.markdown("[![](https://img.shields.io/badge/-GitHub-181717?logo=github&style=flat-square)](https://github.com/ISHOOO)")
with socialmedia[1]: st.markdown("[![](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&style=flat-square&logoColor=white)](https://www.linkedin.com/in/ishan789/)")
with socialmedia[2]: st.markdown("[![](https://img.shields.io/badge/-x.com-000000?style=flat-square&logo=X&logoColor=white)](https://x.com/Gupta_8Anant)")
with socialmedia[3]: st.markdown("[![](https://img.shields.io/badge/Discord-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.com/users/1312679030025097269)")
with socialmedia[4]: st.markdown("[![](https://img.shields.io/badge/Telegram-2CA5E0?style=flat-square&logo=telegram&logoColor=white)](https://t.me/insightful_ishu)")
with socialmedia[5]: st.markdown("[![](https://img.shields.io/badge/-Kaggle-20BEFF?style=flat-square&logo=kaggle&logoColor=white)](https://www.kaggle.com/eeeeshugupta)")
st.write("##")
selection = option_menu(
    menu_title=None, 
    options=["Skills", "Education and Certifications", "Experience and Achievements", "Projects"],
    icons=["gear", "book", "briefcase", "code"],
    orientation="horizontal"
)

if selection=="Skills":
    st.markdown("## Technical skills")
    tools1= st.columns(5)
    with tools1[0]: st.image("assets\\python.png", width=100, caption="Python")
    with tools1[1]: 
        img= Image.open("assets\\mysql.png")
        image=img.crop((55,10,245,180)) #left, up, right, low
        st.image(image, width=100, caption= "MySQL")
    with tools1[2]: st.image("assets\\numpy.png", width=100, caption= "Numpy")
    with tools1[3]: st.image("assets\\pandas.png", width=100, caption="Pandas")
    with tools1[4]: st.image("assets\\matplotlib.png", width=100, caption="Matplotlib")

    tools2= st.columns(5)
    with tools2[0]: st.image("assets\\seaborn.png",width=100, caption="Seaborn")
    with tools2[1]: st.image("assets\\sklearn.png", width=100, caption="Scikit-Learn")
    with tools2[2]: st.image("assets\\tensorflow.png", width=100, caption="Tensorflow")
    with tools2[3]: st.image("assets\\git.png", width=100, caption="Git")
    with tools2[4]: st.image("assets\\excel.jpg", width=100, caption="Excel")
    
    st.divider()

    st.markdown("## Special Skills")

    spec1=st.columns(4)
    with spec1[0]: st.image("assets\\data wrangling.png", width=100, caption="Data Wrangling")
    with spec1[1]: st.image("assets\\eda.png", width=100, caption="Exploratory Data Analysis")
    with spec1[2]: st.image("assets\\dbms.png", width=100, caption="Database Management")
    with spec1[3]: st.image("assets\\kpi.png", width=100, caption="KPIs and Metrics")

    spec2=st.columns(4)
    with spec2[0]: st.image("assets\\data_viz.png", width=100, caption="Data visualisation")
    with spec2[1]: st.image("assets\\ML.png", width=100, caption="Machine Learning")
    with spec2[2]: 
        img= Image.open("assets\\AB_testing.png")
        image=img.crop((90,0,250,220))
        st.image(image, width=80, caption="A/B Testing")
    with spec2[3]: st.image("assets\\time_series.png", width=100, caption="Time Series Analysis")

    st.divider()

    st.markdown("## Soft Skills")
    soft= st.columns(6)
    with soft[0]: 
        st.image("assets\\solution oriented.png", width=80)
        st.caption("Solution oriented thinking")
    with soft[1]: st.image("assets\\presentation.png", width=110 ,caption="Presentation skills")
    with soft[2]: st.image("assets\\adaptability.png", width=100, caption="Adaptability")
    with soft[3]: st.image("assets\\critical.png", width=100, caption="Critical thinking")
    with soft[4]: st.image("assets\\collab.png", width=100, caption="Collaboration" )
    with soft[5]: st.image("assets\\second_order_thinking.png", width=100, caption="Second Order Thinking")
    st.divider()

if selection=="Education and Certifications":
    st.toast("Note: Please click on the images for official websites of the related institutions ")
    st.markdown("## My Education")
    st.subheader("Bachelor of Computer Applications (BCA)")
    bcamsi=st.columns([1,7])
    with bcamsi[0]: 
        st.markdown(f"""
        <a href="http://www.ipu.ac.in" target="_blank">
            <img src="data:image/jpeg;base64,{png_to_base64("assets/ggsipulogo.png")}" width=235" style="cursor:pointer;" />
        </a>    """, unsafe_allow_html=True)
        st.markdown("[![](https://msijanakpuri.com/wp-content/uploads/2019/06/logo2x.png)](https://www.msijanakpuri.com)")
    with bcamsi[1]:
        st.markdown(""" 
            *Specialization: Data Science & Machine Learning*  
            🏫 **Maharaja Surajmal Institute**, Janakpuri, Delhi, India  
            📍 Affiliated with **Guru Gobind Singh Indraprastha University (GGSIPU)**
            - 🧠 Developed strong foundations in `Programming`, `Data Structures`, `Data Analysis`, `Data Visualization`, `Database Management` and `Machine Learning`.
            - 📊 Worked on hands-on data science projects using Python, MySQL, Pandas, Scikit-learn, TensorFlow, and more.
            - 🤝 Participated in seminars, workshops, hackathons and collaborative projects across the 3-year program.
            """
            )
    st.subheader("Senior Secondary Education (Class 12)")
    sr_sec=st.columns([1,7])
    with sr_sec[0]:
        st.markdown(f"""
        <a href="http://www.jmjdelhi.in" target="_blank">
            <img src="data:image/jpeg;base64,{png_to_base64("assets/jmjlogo.png")}" width=235" style="cursor:pointer;" />
        </a>    """, unsafe_allow_html=True)
        st.markdown(f"""
        <a href="https://www.cbse.gov.in" target="_blank">
            <img src="data:image/jpeg;base64,{png_to_base64("assets/cbselogo.png")}" width=235" style="cursor:pointer;" />
        </a> 
        """, unsafe_allow_html=True)
    with sr_sec[1]:    
        st.markdown(
            """
            🏫 **Jesus Mary Joseph School**, New Delhi, Delhi, India  
            📝 **Board:** Central Board of Secondary Education (CBSE)  

            - 📚 Subjects: `Mathematics`, `English`, `Physics`, `Chemistry`, `Computer Science`
            - 🎓 Developed a strong academic foundation with focus on analytical and logical thinking.
            - 💡 Built early interest in coding and technology through computer science curriculum.
            """
        )
    
    st.subheader("Secondary Education (Class 10)")
    secondary=st.columns([1,7])
    with secondary[0]:
        st.markdown(f"""
        <a href="http://www.jmjdelhi.in" target="_blank">
            <img src="data:image/jpeg;base64,{png_to_base64("assets/jmjlogo.png")}" width=235" style="cursor:pointer;" />
        </a>    """, unsafe_allow_html=True)
        st.markdown(f"""
        <a href="https://www.cbse.gov.in" target="_blank">
            <img src="data:image/jpeg;base64,{png_to_base64("assets/cbselogo.png")}" width=235" style="cursor:pointer;" />
        </a>    """, unsafe_allow_html=True)

    with secondary[1]: st.markdown(
            """
            🏫 **Jesus Mary Joseph School**, New Delhi, Delhi, India  
            📝 **Board:** Central Board of Secondary Education (CBSE)  

            - 📚 Subjects: `Mathematics`, `English`, `Hindi`, `Social Studies`, `General Science`
            - 🧠 Strengthened fundamental concepts across all core disciplines.
            - 🏅 Balanced academics with participation in school-level events and competitions.
            """)

    st.divider()

    st.subheader("📋 My certifications and coursework")
    row1, row2, row3, row4 =st.columns(2, gap="large"), st.columns(2, gap="large"), st.columns(2, gap="large"), st.columns(2, gap="large")
    with row1[0] :
        st.markdown("#### Introduction to Machine Learning, IIT Kharagpur")
        img = Image.open("assets\\NPTELML.jfif")
        st.image(img.resize((400, 300)), use_container_width=True, caption="certificate of accomplishment issued by NPTEL upon successful clearance of an exam")
    with row1[1] :
        st.markdown("#### SQL(Advanced), HackerRank")
        img = Image.open("assets\\SQLadvanced.jfif")
        st.image(img.resize((400, 300)), use_container_width=True, caption="certificate of accomplishment issued by HackerRank upon successful clearance of an online exam")

    with row2[0]:
        st.markdown("#### Python(Basic), HackerRank")
        img = Image.open("assets\Pythonbasic.jfif")
        st.image(img.resize((400, 300)), use_container_width=True, caption="certificate of accomplishment issued by hacker rank upon successful clearance of an online exam")
    with row2[1]:
        st.markdown("#### SQL(Intermediate), HackerRank")
        img = Image.open("assets\\SQLintermediate.jfif")
        st.image(img.resize((400, 300)), use_container_width=True, caption="certificate of accomplishment issued by HackerRank upon successful clearance of an online exam")
    
    with row3[0]:
        st.markdown("#### Silver medal in International English Olympiad, SOF")
        img = Image.open("assets/IEO_2016.jpeg")
        st.image(img.resize((400, 300)), use_container_width=True, caption="Silver medal and certificate of accomplishment issued by Science Olympiad Foundation upon successful clearance of an exam")
    with row3[1]:
        st.markdown("#### SQL(Basic), HackerRank")
        img=Image.open("assets\\SQLbeginner.jfif")
        st.image(img.resize((400, 300)), use_container_width=True, caption="certificate of accomplishment issued by HackerRank upon successful clearance of an online exam")
        
    with row4[0]: 
        st.markdown("#### International Maths Olympiad, SOF")
        img=Image.open("assets\\IMO.jpeg")
        st.image(img.rotate(90).resize((400,300)), use_container_width=True, caption= "certificate of participation issued by Science Olympiad Foundation upon successful clearance of an exam")
    

if selection=="Experience and Achievements":
    import streamlit as st

if selection == "Experience and Achievements":
    
    st.subheader("📊 Data Science Intern — Tech-A-Intern (Jul 2023 – Aug 2023)")
    st.markdown("""
    - An enriching endeavour full of mentorship and collaboration.
    - Analyzed and visualized IMDb dataset focusing on **genre, author, ratings, popularity, release date, country**, etc.
    - Built **Multiple Linear Regression** models to predict housing prices based on **rooms, bathrooms, furnishing, storage area, parking area, and address**.
    """)

    st.subheader("🧠 Data Science Intern — ICT Academy (Aug 2023 – Oct 2023)")
    st.markdown("""
    - Completed a Data Science virtual internship using Open Weaver Studio.
    - Built **Sentisense**, a sentiment analysis app for classifying customer feedback and performing **Named Entity Recognition (NER)**.
    - Created **collaborative filtering-based recommendation systems** as part of the capstone project.
    """)

    st.subheader("🚀 GSoC 2025 Contributor — NumFOCUS (May 2025 – Present)")
    st.markdown("""
    - Selected for Google Summer of Code 2025 under the umbrella organization **aeon** (NumFOCUS).
    - Contributing to the **aeon** time series library by adding new clustering methods like **DBSCAN, Density Peaks, and Hierarchical Clustering**.
    - Leveraging distance functions such as **Dynamic Time Warping (DTW)** for more effective time series grouping and pattern exploration.
    """)

    st.subheader("💻 Competitive Programming and Problem Solving")
    st.markdown("[![](https://img.shields.io/badge/-LeetCode-FFA116?style=flat-square&logo=LeetCode&logoColor=black)](https://leetcode.com/u/ishubest90/)")
    st.write("Solved **91** problems, Rank: **1,282,170**, Languages used: **MySQL, Pandas, Python**.")
    st.markdown("[![HackerRank](https://img.shields.io/badge/-HackerRank-2EC866?style=flat-square&logo=HackerRank&logoColor=white)](https://www.hackerrank.com/profile/ishuthebest9999)")
    st.write("""
        - 🟢 Python: **5 stars (32%)**, 37/115 challenges solved.
        - 🟢 MySQL: **5 stars (79%)**, 46/58 challenges solved.
        - 🟡 Problem Solving: **4 stars (85%)**, 56.42 points toward Gold badge.
    """)

    st.subheader("🌍 Open Source and Community Contributions")
    st.markdown("""
    - **Kaggle.com** Contributor:
        - Competitions
        - Datasets
        - Notebooks
        - Discussions
    """)


teslalogo=jpg_to_base64("assets\\tesla.jpg")
supermarketlogo=jpg_to_base64("assets\\supermarket.jpg")
imdblogo=jpg_to_base64("assets\\imdb.JPG")

if selection=="Projects":
    st.toast("Note: please click on the images for the corresponding demo")
    st.subheader("Project 1:  Anidex image classifier")    
    demo, desc=st.columns([1,3])
    with demo:
        st.markdown(f"""
        <a href="https://huggingface.co/spaces/goofyishu/Anidex" target="_blank">
            <img src="data:image/jpeg;base64,{jpg_to_base64("assets/anidexlogo.jpg")}" width=235" style="cursor:pointer;" />
        </a>    """, unsafe_allow_html=True)
        st.markdown("[![](https://img.shields.io/badge/Click_here_for_source_code-black?logo=github)](https://github.com/ISHOOO/Anidex-Image-Classifier)")
    with desc: st.markdown("""
        The Anidex Image Classifier project aims to classify images of various animal species using deep learning techniques. 
        Inspired by the concept of the Pokédex from Pokémon, this model can predict the species of an animal from an input image.
                        
        - A Convolutional Neural Network model built using TensorFlow, Keras, NumPy, and Matplotlib libraries in Python
        - It can predict among 90 different animal species, including antelope, badger, bat, bear, and many others.
        - The model achieves a validation accuracy of 37.04%.
        """)
    st.divider()

    st.subheader("Project 2: Tesla stock price Analysis")
    st.markdown(f"""
    <a href="" target="_blank">
        <img src="data:image/jpeg;base64,{teslalogo}" width="200" style="cursor:pointer;" />
    </a>    """, unsafe_allow_html=True)
    st.markdown("[![](https://img.shields.io/badge/Click_here_for_source_code-black?logo=github)](https://github.com/ISHOOO/Tesla-stock-price-EDA-and-forecasting)")

    st.divider()

    st.subheader("Project 3: Supermarket sales Analysis")
    st.markdown(f"""
    <a href="" target="_blank">
        <img src="data:image/jpeg;base64,{supermarketlogo}" width="200" style="cursor:pointer;" />
    </a>    """, unsafe_allow_html=True)
    st.markdown("[![](https://img.shields.io/badge/Click_here_for_source_code-black?logo=github)](https://github.com/ISHOOO/Supermarket-sales-analysis)")

    st.divider()
    
    st.subheader("Project 4: Movie data Analysis")
    st.markdown(f"""
    <a href="" target="_blank">
        <img src="data:image/jpeg;base64,{imdblogo}" width="200" style="cursor:pointer;" />
    </a>    """, unsafe_allow_html=True)
    st.markdown("[![](https://img.shields.io/badge/Click_here_for_source_code-black?logo=github)](https://github.com/ISHOOO/TAIRP/tree/main/Task%201)")

