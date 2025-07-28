import streamlit as st
import base64

# ==== Set page config ====
st.set_page_config(page_title="💘 Friendship Predictor 🔮", layout="centered")


# ==== Background Image Function ====
def add_bg(image_file):
    with open(image_file, "rb") as img:
        b64_img = base64.b64encode(img.read()).decode()
        bg_img_style = f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{b64_img}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """
        st.markdown(bg_img_style, unsafe_allow_html=True)

r


# ==== Title ====
st.title("💘 Friendship Predictor 🔮 ")
st.markdown("### 🤖 Batao kya dosti ho payegi ya reh jayegi sirf 'seen' me?")

# ==== Your Info ====
st.header("🧍‍♂️ Tumhari Info")
user = {
    "name": st.text_input("Tumhara Naam"),
    "age": st.slider("Age", 10, 30, 18),
    "city": st.text_input("Sheher"),
    "status": st.selectbox("Status", ["single", "relationship", "confused"]),
    "nature": st.select_slider("Nature", options=["funny", "serious", "rude", "romantic", "caring"]),
    "communication": st.selectbox("Communication Style", ["talkative", "shy", "normal"]),
    "hobbies": st.multiselect("Hobbies", ["gaming", "music", "drawing", "coding", "poetry", "funny videos", "travel"]),
}

# ==== Girl's Info ====
st.header("👧 Larki Ki Info")
girl = {
    "name": st.text_input("Uska Naam"),
    "age": st.slider("Uski Age", 10, 30, 18),
    "city": st.text_input("Uska Sheher"),
    "status": st.selectbox("Uska Status", ["single", "relationship", "complicated"]),
    "nature": st.select_slider("Uska Nature", options=["funny", "serious", "rude", "romantic", "caring"]),
    "response": st.selectbox("Reply Style", ["quick", "late", "seen only"]),
    "looking": st.selectbox("Wo kya dhoond rahi hai?", ["fun", "serious", "study partner", "nothing"]),
    "hobbies": st.multiselect("Uski Hobbies", ["gaming", "music", "drawing", "coding", "poetry", "funny videos", "travel"]),
}


# ==== Prediction Logic ====
def predict_friendship(user, girl):
    score = 0
    reasons = []

    if abs(user["age"] - girl["age"]) <= 2:
        score += 20
        reasons.append("✅ Age ka difference perfect hai!")

    if user["city"].strip().lower() == girl["city"].strip().lower():
        score += 15
        reasons.append("✅ Dono ek sheher se hain!")

    if user["status"] == "single" and girl["status"] == "single":
        score += 20
        reasons.append("✅ Dono hi single hain, free to talk! 😉")

    if user["nature"] == girl["nature"]:
        score += 10
        reasons.append("✅ Same nature — easy bonding!")
    elif (user["nature"], girl["nature"]) in [("funny", "serious"), ("serious", "funny")]:
        score += 7
        reasons.append("✅ Opposite natures — chance for balance!")

    if girl["looking"] == "fun" and user["nature"] == "funny":
        score += 10
        reasons.append("✅ Usay fun chahiye, tum ho full entertainer!")

    if girl["response"] == "quick" and user["communication"] == "talkative":
        score += 10
        reasons.append("✅ Tum bolo ge aur wo sunnay ke liye tayar!")

    common_hobbies = set(user["hobbies"]) & set(girl["hobbies"])
    if common_hobbies:
        score += len(common_hobbies) * 5
        reasons.append(f"✅ Common hobbies: {', '.join(common_hobbies)}")

    return score, reasons


# ==== Predict Button ====
if st.button("💌 Predict Friendship Now!"):
    score, reasons = predict_friendship(user, girl)
    
    st.subheader("📊 Prediction Result")
    st.write(f"**Friendship Score:** {score} / 100")

    if score >= 75:
        st.success("💚 Baat ban sakti hai! Start with meme sharing!")
    elif score >= 50:
        st.warning("💛 Average chance. Try soft baat-cheet first.")
    else:
        st.error("💔 Dosti mushkil lagti hai... but try as a classmate!")

    st.markdown("### 🔍 Reasons:")
    for r in reasons:
        st.write(r)

    st.markdown("### 📈 Friendship Bar")
    st.progress(score if score <= 100 else 100)

    st.markdown("### 🤗 Advice:")
    if score >= 75:
        st.write("Send her a good meme or funny line, friendship ki rocket udaye! 🚀")
    elif score >= 50:
        st.write("Shayad usay tumhara sense of humor pasand aa jaye! 🧠")
    else:
        st.write("Dosti se zyada expectations na rakho bhai 😅")
