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
    toxic_keywords = ["idiot", "hate", "stupid", "kill", "ugly", "loser", "dumb", "fool", "moron",
"trash", "worthless", "pathetic", "jerk", "creep", "bastard", "scum",
"shut up", "die", "annoying", "disgusting", "nonsense", "garbage",
"retard", "psycho", "mad", "crazy", "evil", "brainless", "failure",
"lame", "weak", "useless", "coward", "pervert", "toxic", "dirty",
"stink", "sick", "hate you", "go die", "kill yourself", "nobody likes you"]
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
