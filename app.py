import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Cyberbullying Detection System",
    page_icon="🛡️",
    layout="centered"
)

# Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff; /* Original Dark Blue */
        color: white;
        border: none;
        transition: background-color 0.3s ease, color 0.3s ease; 
    }

    .stButton>button:hover {
        background-color: #93c5fd !important; /* Light Blue on hover */
        color: #1e3a8a !important;            /* Dark Blue text for contrast */
        border: 1px solid #60a5fa;
    }
    footer {
        visibility: hidden;
    }
    .footer-text {
        text-align: center;
        color: #6c757d;
        margin-top: 50px;
        font-size: 0.9em;
    }
    </style>
    """, unsafe_allow_html=True)

# Header Section
st.title("🛡️ Cyberbullying Detection ")
st.write("This system uses natural language processing patterns to check whether a message is safe or contains provoking content. Help keep the digital space respectful.")

st.divider()

# Input Section
user_input = st.text_area("Enter the message you want to analyze:", placeholder="Type your message here...", height=150)

# Prediction Logic
def analyze_text(text):
    toxic_keywords = ["idiot","hate","stupid","kill","ugly","loser","dumb","fool","moron","trash",
"worthless","pathetic","jerk","creep","bastard","scum","shut up","die","annoying",
"disgusting","nonsense","garbage","psycho","mad","crazy","evil","brainless",
"failure","lame","weak","useless","coward","pervert","toxic","dirty","stink",
"sick","hate you","go die","kill yourself","nobody likes you","nobody cares",
"you are nothing","piece of trash","human garbage","waste of space","shame on you",
"embarrassing","you disgust me","get lost","get out","go away","drop dead",
"you are useless","you are stupid","you are dumb","you are ugly","you are a joke",
"you make me sick","you deserve pain","you should die","you are pathetic",
"you are worthless","crybaby","attention seeker","drama queen",
"fake","liar","cheater","backstabber","snake","two faced","manipulative",
"selfish","heartless","cold","cruel","mean","nasty","vile","filthy","rotten",
"spoiled","broken","damaged","hopeless","helpless","good for nothing",
"born loser","total failure","complete idiot","absolute fool","big mistake",
"burden","curse","problem","liability","disappointment","family shame",
"society shame","waste of life","waste of oxygen","brain dead","no brain",
"empty head","low IQ","mentally weak","mentally sick","unstable","freak",
"weirdo","oddball","outcast","reject","nobody","nobody wants you","alone forever",
"die alone","stay lonely","unwanted","unlovable","ugliest","dirtiest",
"disgrace","dishonor","clown","joker","laughing stock","mockery",
"not normal","abnormal","trash human","subhuman","inferior","worthless piece",
"cheap","low class","bad","bad person","bad human","bad behavior","bad attitude",
"bad character","bad mentality","bad thinking","bad influence","bad vibes",
"bad presence","bad intentions","bad mindset","bad nature","bad conduct",
"bad reputation","bad example","bad role model","bad citizen","bad friend",
"bad soul","bad heart","bad blood","bad energy","bad personality","bad habits",
"toxic person","poison","disease","virus","infection","plague","cancer",
"parasite","leech","drain","energy vampire","evil person","evil mind","dark soul",
"dead inside","heart of stone","stone heart","cold blooded","no feelings",
"emotionless","monster","beast","animal","pig","dog","rat","worm","insect",
"cockroach","garbage person","failure in life","ruined life","wasted life",
"no future","futureless","hopeless case","lost cause","beyond help",
"beyond saving","irredeemable","idiotic","moronic","foolish","mindless",
"clueless","ignorant","lazy","slacker","freeloader","menace","dangerous",
"violent","aggressive","abusive","bully","harasser","threatening","intimidating",
"creepy","perverted","dirty mind","sick mentality","twisted mind","corrupt brain",
"black heart","soulless","inhuman","merciless","ruthless","sadistic",
"shameless","no dignity","cheap mentality","vulgar","obnoxious","irritating",
"unbearable","go away forever","never come back","disappear","you don't matter",
"you mean nothing","irrelevant","insignificant","narrow minded","close minded",
"backward","trash mindset","garbage mindset","negative mindset","evil mindset"
]
    text_lower = text.lower()
    
    # Check if any keyword exists in the input
    if any(word in text_lower for word in toxic_keywords):
        return "PROVOKING"
    return "SAFE"

# Action Button
if st.button("Analyze Message"):
    if not user_input.strip():
        st.info("ℹ️ Please enter some text first to perform the analysis.")
    else:
        result = analyze_text(user_input)
        
        st.subheader("Analysis Result:")
        
        if result == "SAFE":
            st.success("✅ This message is safe. Thank you for maintaining respectful communication.")
            st.balloons()
        else:
            st.error("⚠️ You are violating ethical standards by using abusive or provoking language. Please avoid such words.")
            st.warning("Detection Note: Our system identified keywords associated with cyberbullying or harassment.")

# Footer
st.markdown("---")
st.markdown('<p class="footer-text">Cyberbullying Detection System – Minor Project</p>', unsafe_allow_html=True)
