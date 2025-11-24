import streamlit as st
from PIL import Image, ImageEnhance
from base64 import b64encode
from io import BytesIO
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

st.set_page_config(layout="wide", page_title="Portfolio Website", initial_sidebar_state="expanded")
with open("styles.css") as f: st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title(":green-background[ANANT GUPTA]")
st.write("A Data Science and Analytics enthusiast looking for opportunities to solve real-world business problems by leveraging programming skills for :orange-background[Statistical Analysis], :orange-background[Graphical Visualization], :orange-background[Database management] and :orange-background[Predictive Modelling]. Committed to upskilling and providing actionable insights for data-driven decision making to foster innovation and efficiency.")
with open("Resume.pdf", "rb") as f: pdf_data = f.read()
mail, resume, download,_ = st.columns([1.2,2,2.4,5]) 
with mail: st.link_button(label="Hire Me", url="https://mail.google.com/mail/u/1/#inbox?compose=CllgCJNvwPFQXdsrTTFwqVQjFZtcsVMswwnsZxsCDnsWgxHxcDNgFpgQlWDTqznrFqDLmnsGGVB") 
with resume: st.link_button(label="Preview Resume", url= "https://drive.google.com/file/d/18ueGxvXJZW0wv8hNYWsttRajy9-FVrKx/view?usp=sharing")
with download: st.download_button(label="Download Resume", data=pdf_data, file_name="Anant_Gupta_Data_Analytics_Resume.pdf",mime="application/pdf")

selection = option_menu(
    menu_title=None, 
    options=["Skills", "Education", "Experience", "Projects"],
    icons=["gear", "book", "briefcase", "code"],
    orientation="horizontal"
    )

with st.sidebar:
    # Profile pic
    pfp=jpg_to_base64("assets/pfp.JPG")
    st.markdown(f"""
    <img src="data:image/jpeg;base64,{pfp}" style="border-radius: 50%; width: 215px; height: 215px; object-fit: cover; border: 15px solid #b2b2be71;">
    """,
    unsafe_allow_html=True,)
#------------------------------------------------Contact section------------------------------------------------#

    st.title("Contact Me:")
    telegram=st.columns([1,4])
    with telegram[0]:st.image("assets/telegram.png")
    with telegram[1]:st.write("[@insightful_ishu](https://t.me/insightful_ishu)") 

    discord=st.columns([1,4])
    with discord[0]:st.markdown("![](https://pngimg.com/d/discord_PNG7.png)") 
    with discord[1]:st.write("[@theinsightfinder](https://discord.com/users/1312679030025097269)") 

    github=st.columns([1,4])
    with github[0]: st.image("assets/github.png", use_container_width=True)
    with github[1]:st.write("[@ISHOOO](https://github.com/ISHOOO)")     
    
    linkedin=st.columns([1,4])
    with linkedin[0]:st.markdown("![](https://static.vecteezy.com/system/resources/previews/023/986/926/non_2x/linkedin-logo-linkedin-logo-transparent-linkedin-icon-transparent-free-free-png.png)")
    with linkedin[1]:st.write("[@anantg789](https://www.linkedin.com/in/anantg789)") 

    x=st.columns([1,4])
    with x[0]: st.image("assets/twitterX.png",  use_container_width=True)
    with x[1]: st.write("[@Gupta_8Anant](https://x.com/Gupta_8Anant)")                                 

#---------------------------------------------Skills------------------------------------------------------------#

if selection=="Skills":
    st.header(" :red-background[TECHNICAL SKILLS]")
    tools1= st.columns(5,gap="large")
    with tools1[0]: st.image("assets/python.png", use_container_width=True, caption="Python")
    with tools1[1]: st.image("assets/mysql.png", use_container_width=True,  caption= "MySQL")
    with tools1[2]: st.image("assets/tableau.png", use_container_width=True,caption="Tableau")
    with tools1[3]: st.image("assets/excel.jpg", use_container_width=True, caption="Excel") 
    with tools1[4]: st.image("assets/git.png", use_container_width=True, caption="Git")

    tools2= st.columns(5,gap="large")
    with tools2[0]: st.image("assets/numpy.png", use_container_width=True, caption= "Numpy")
    with tools2[1]: st.image("assets/pandas.png", use_container_width=True, caption="Pandas")
    with tools2[2]: st.image("assets/matplotlib.png", use_container_width=True, caption="Matplotlib")
    with tools2[3]: st.image("assets/seaborn.png", use_container_width=True, caption="Seaborn")     
    with tools2[4]: st.image("assets/sklearn.png", use_container_width=True, caption="Scikit-Learn")

    tools3= st.columns(5,gap="large")
    with tools3[0]: st.image("assets/tensorflow.png", use_container_width=True, caption="Tensorflow")
    with tools3[1]: st.image("assets/jupnotebook.png", use_container_width=True, caption="Jupyter Notebook")
    
    "---"

    st.header(":red-background[SPECIAL SKILLS]")

    spec1=st.columns(4, gap="large")
    with spec1[0]: st.image("assets/data wrangling.png", use_container_width=True, caption="Data Wrangling")
    with spec1[1]: st.image("assets/eda.png",  use_container_width=True, caption="Exploratory Data Analysis")
    with spec1[2]: st.image("assets/dbms.png",  use_container_width=True, caption="Database Management")
    with spec1[3]: st.image("assets/kpi.png", use_container_width=True, caption="KPIs and Metrics")

    spec2=st.columns(4, gap="large")
    with spec2[0]: st.image("assets/data_viz.png", use_container_width=True, caption="Data visualisation")
    with spec2[1]: st.image("assets/ML.png", use_container_width=True, caption="Machine Learning")
    with spec2[2]: st.image("assets/AB_testing.png", use_container_width=True, caption="A/B Testing")
    with spec2[3]: st.image("assets/time_series.png", use_container_width=True, caption="Time Series Analysis")

    "---"

    st.header(":red-background[SOFT SKILLS]")
    soft= st.columns(6)
    with soft[0]: st.image("assets/solution oriented.png", width=100, caption="Solution oriented")
    with soft[1]: st.image("assets/presentation.png", caption="Presentation skills")
    with soft[2]: st.image("assets/adaptability.png", width=100, caption="Adaptability")
    with soft[3]: st.image("assets/critical.png", width=100, caption="Critical thinking")
    with soft[4]: st.image("assets/collab.png", width=100, caption="Collaboration" )
    with soft[5]: st.image("assets/second_order_thinking.png", width=100, caption="Second Order Thinking")
    "---"

#------------------------------------Educations and Certifications---------------------------------------------------#

if selection=="Education":
    st.toast("Note: Please click on the images for official websites of the related institutions ")
    st.header(":violet-background[MY EDUCATION]")
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
    "---"
    st.subheader("Senior Secondary Education (12th standard)")
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
    
    "---"

    st.header(":violet-background[MY CERTIFICATIONS AND COURSEWORK]")
    cert1, cert2, cert3, cert4 =st.columns(2, gap="large"), st.columns(2, gap="large"), st.columns(2, gap="large"), st.columns(2, gap="large")
    with cert1[0] :
        st.markdown("#### Introduction to Machine Learning, IIT Kharagpur")
        img = Image.open("assets/NPTELML.jfif")
        st.image(img.resize((400, 300)), use_container_width=True, caption="certificate of accomplishment issued by NPTEL upon successful clearance of an exam")
    with cert1[1] :
        st.markdown("#### SQL(Advanced), HackerRank")
        img = Image.open("assets/SQLadvanced.jfif")
        st.image(img.resize((400, 300)), use_container_width=True, caption="certificate of accomplishment issued by HackerRank upon successful clearance of an online exam")

    with cert2[0]:
        st.markdown("#### Python(Basic), HackerRank")
        img = Image.open("assets/Pythonbasic.jfif")
        st.image(img.resize((400, 300)), use_container_width=True, caption="certificate of accomplishment issued by hacker rank upon successful clearance of an online exam")
    with cert2[1]:
        st.markdown("#### SQL(Intermediate), HackerRank")
        img = Image.open("assets/SQLintermediate.jfif")
        st.image(img.resize((400, 300)), use_container_width=True, caption="certificate of accomplishment issued by HackerRank upon successful clearance of an online exam")
    
    with cert3[0]:
        st.markdown("#### Silver medal in International English Olympiad, SOF")
        img = Image.open("assets/IEO_2016.jpeg")
        st.image(img.resize((400, 300)), use_container_width=True, caption="Silver medal and certificate of accomplishment issued by Science Olympiad Foundation upon successful clearance of an exam")
    with cert3[1]:
        st.markdown("#### SQL(Basic), HackerRank")
        img=Image.open("assets/SQLbeginner.jfif")
        st.image(img.resize((400, 300)), use_container_width=True, caption="certificate of accomplishment issued by HackerRank upon successful clearance of an online exam")
        
    with cert4[0]: 
        st.markdown("#### International Maths Olympiad, SOF")
        img=Image.open("assets/IMO.jpeg")
        st.image(img.rotate(90).resize((400,300)), use_container_width=True, caption= "certificate of participation issued by Science Olympiad Foundation upon successful clearance of an exam")
    
#------------------------------Experience and Achievements---------------------------------------------#

if selection == "Experience":
    st.header(":blue-background[📊INTERNSHIPS]")
    st.subheader("Data Science Intern — Tech-A-Intern (Jul 2023 – Aug 2023)")
    taiintern=st.columns([1.75,5])
    with taiintern[0]:
        st.image("assets/taiintern.JPG")
    with taiintern[1]:
        st.markdown("""
        - An enriching endeavour full of mentorship and collaboration.
        - Analyzed and visualized IMDb dataset focusing on **genre, author, ratings, popularity, release date, country**, etc.
        - Built **Multiple Linear Regression** models to predict housing prices based on **rooms, bathrooms, furnishing, storage area, parking area, and address**.
        """)

    st.subheader("Data Science Intern — ICT Academy (Aug 2023 – Oct 2023)")
    ictintern=st.columns([1.75,5])
    with ictintern[0]:
        st.image("assets/ictintern.JPG")
    with ictintern[1]:    
        st.markdown("""
        - Completed a Data Science virtual internship using Open Weaver Studio.
        - Built **Sentisense**, a sentiment analysis app for classifying customer feedback and performing **Named Entity Recognition (NER)**.
        - Created **collaborative filtering-based recommendation systems** as part of the capstone project.
        """)
    
    "---"

    st.header(":blue-background[💻 COMPETITIVE PROGRAMMING]")
    st.subheader("[Leetcode (click to view profile)](https://leetcode.com/u/ishubest90)")
    st.write(""" 
        - Solved **100** problems 
        - Rank: **Top 1 million**
        - Languages used: **MySQL, Pandas, Python**
        """)
    
    hackerrank=st.columns([1,8])
    st.subheader("[HackerRank (click to view profile)](https://www.hackerrank.com/profile/ishuthebest9999)")
    st.write("""
        - 🟢 Python: **5 stars**, 37/115 challenges solved.
        - 🟢 MySQL: **5 stars**, 46/58 challenges solved.
        - 🟡 Problem Solving: **4 stars**, 82% towards Gold badge.
    """)
    "---"

    st.subheader(":blue-background[🌍 OPEN SOURCE AND COMMUNITY CONTRIBUTIONS]")

    st.subheader("[Kaggle (click to view profile)](https://www.kaggle.com/eeeeshugupta)")
    st.markdown("""
        - Competitions: Contributor 
        - Datasets:  Contributor
        - Notebooks: Contributor
        - Discussions: Contributor
    """)
    "---"

#----------------------------------Projects-------------------------------------------------#

if selection=="Projects":
    st.header(":orange-background[Project 1: Smart Attendance Management App]")
    code,desc=st.columns([1.1,2.9])
    with code:
        st.image("assets/attendance_mgmt.png")
        st.link_button("Source Code", "https://github.com/ISHOOO/Smart-Attendance-App")
    with desc:
        st.write("""
            This application registers and fills student attendance smartly through Face Detection and Recognition.
            - Use Advanced Computer Vision algorithms such as HAAR Cascade clasifier and LBPH algorithm 
            - Implemented in collaboration with fellow Tech enthusiasts using python libraries such as open-cv, tkinter, numpy, pandas, pyttsx3 and  pillow
            - Automates `76%` of human effort
            """)

    "---"
        
    st.header(":orange-background[Project 2: Anidex: Animal image classifier]")    
    code,desc=st.columns([1.1,2.9])
    with code:
        st.image("assets/anidexlogo.jpg")
        demo, src_code=st.columns([1.28,2.3])
        with demo: st.link_button("Demo", "https://huggingface.co/spaces/goofyishu/Anidex")
        with src_code: st.link_button("Source Code", "https://github.com/ISHOOO/Anidex-Image-Classifier")
    with desc: 
        st.markdown("""
        The Anidex Image Classifier project aims to classify images of various animal species using deep learning techniques. 
        Inspired by the concept of the Pokédex from Pokémon, this model can predict the species of an animal from an input image.
                        
        - A Convolutional Neural Network model built using TensorFlow, Keras, NumPy, and Matplotlib libraries in Python
        - It can predict among 90 different animal species, including antelope, badger, bat, bear, and many others.
        - The model achieves a validation accuracy of `37.04%`.
        """)

    "---"
        
    st.header(":orange-background[Project 3: Financial Fraud Detection]")
    code,desc=st.columns([1.1,2.9])
    with code:
        st.image("assets/fraud_detection.png")
        st.link_button("Source Code", "https://github.com/ISHOOO/Financial-Fraud-Detection")
    with desc:
        st.write("""
            The Financial Fraud Detection project identifies fraudulent transactions using a hybrid model of Random Forests and rule-based heuristics.
            - Ensemble of 15 decision trees with entropy-based splitting.
            - Rule-driven bias flags transactions exceeding 200,000 units.
            - Key features: transaction amount, payer/receiver type, account balances.
            - Achieves `~98%` validation accuracy.
            - Built in Python with scikit-learn, pandas, matplotlib, and seaborn.
        """)

    "---"    

    st.header(":orange-background[Project 4: Tesla stock price EDA and Forecasting]")
    code,desc=st.columns([1.1,2.9])
    with code:
        st.image("assets/Tesla.JPG")
        st.link_button("Source code", "https://github.com/ISHOOO/Tesla-stock-price-EDA-and-forecasting") 
    with desc:
        st.write("""
            The Tesla Stock Price Prediction and Forecasting project leverages **time series modeling** to forecast future stock prices for Tesla Inc.
            - Conducted in-depth Exploratory Data Analysis (EDA) and feature tuning to optimize model performance.
            - Developed a SARIMA (Seasonal AutoRegressive Integrated Moving Average) model to accurately capture trends and seasonality in stock price data.
            - Implemented using Python with libraries including pandas, matplotlib, and statsmodels.
            - Achieved a Mean Absolute Percentage Error (MAPE) of `0.001`, indicating high forecasting accuracy.
            """)

    "---"

    st.header(":orange-background[Project 5: Exploratory Data Analysis of Layoffs dataset]")
    code,desc=st.columns([1.1,2.9])
    with code:
        st.image("assets/tech-layoff-analysis.JPG")
        st.link_button("Source code", "https://github.com/ISHOOO/layoffs-data-analysis-SQL")
    with desc:
        st.write("""
                This project aims to clean and analyze the Tech Layoffs dataset to uncover trends and insights related to layoffs in the technology sector across the entire globe.
                - The dataset was cleaned and transformed by removing duplicates, null values and inconsistencies in the values.
                - The analysis report contained insights such as:
                    - The top 10 companies with the highest number of layoffs
                    - Companies which laid off all the employees at once
                    - The amount of funds raised by the companies through layoffs
                    - Companies with highest number of layoffs per year. 
                - The analysis was done using SQL queries in MySQL Workbench.
            """)
        
    "---"

    st.header(":orange-background[Project 6: Social Media Recommendation Engine]")
    code,desc=st.columns([1.1,2.9])
    with code:
        st.image("assets/artsper.jfif")
        st.link_button("Source Code", "https://github.com/ISHOOO/Social-Media-FYP")
    with desc:
        st.write("""
                The Social Media Recommendation System was built for *Artsper*, a social media platform for artists.
                - Recommends relevant content creators to users based on their interests and engagement patterns.
                - Enhances content discoverability and user experience on the platform.
                - Developed collaboratively using Python and MERN stack in Javascript.
            """)

    "---"

    st.header(":orange-background[Project 7: Supermarket sales Analysis]")
    code,desc=st.columns([1.1,2.9])
    with code:
        st.image("assets/supermarket.JPG")
        st.link_button("Source Code", "https://github.com/ISHOOO/Supermarket-sales-analysis")
    with desc:
        st.write("""
                 This project analyses sales data and extracts insights to optimize marketing campaigns.
                    - Various types of insights were gained through the project such as: 
                        - Customer behavior insights
                        - Membership insights
                        - Product performance insights
                        - Customer Satisfaction 
                        - Optimal marketing campaign timings
                    - Used python modules such as numpy, pandas, matplotlib and seaborn to perform Data cleaning and visualisation
                 """)

    "---"
    
    st.header(":orange-background[Project 8: Tableau Seattle Airbnb Dashboard]")
    code,desc=st.columns([1.1,2.9])
    with code:
        st.image("assets/seattle airbnb dashboard.JPG")
        st.link_button("Live dashboard Link", "https://public.tableau.com/app/profile/ishan.gupta7148/viz/Seattleairbnbdataviz/Dashboard1")
    with desc:
        st.write("""
                This is an insightful and interactive dashboard made to visualise the Seattle Airbnb dataset to answer a real-world business question:
                > :blue-background["Where should I invest in Seattle to start a profitable Airbnb business?"] 
                - It was made using `Tableau 2025.1`
                - Helps identify the most profitable neighborhoods and factors influencing listing success for an Airbnb business in Seattle.
                - Uses graphical visuals such as Bar graph, Line plots and mapbox. 
            """)
    
    "---"

    st.header(":orange-background[Project 9: Automobile sales Dashboard]")
    code,desc=st.columns([1.1,2.9])
    with code:
        st.image("assets/automobile sales dashboard.JPG")
        with open("bike dataset.xlsx", "rb") as f:
            bytes_data = f.read()
        st.download_button("Download Excel file", bytes_data, file_name="Automobile_Dashboard_project_Anant_Gupta.xlsx")

    with desc:
        st.write("""
            The Automobile Sales Dashboard provides interactive visual insights into factors influencing automobile purchases.
            - Built entirely in Microsoft Excel using pivot tables, slicers, and graphical visualizations.
            - Includes pie charts, line plots, and bar graphs for dynamic data exploration.
            - Analyzes how age, education, marital status, gender, and region impact purchase behavior.
            - All data cleaning, transformation, and visualization performed within Excel.

            """)
    "---"
