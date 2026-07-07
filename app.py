import streamlit as st
import streamlit.components.v1 as components
import time
import numpy as np

#To use local images in HTML
import base64

st.title("Happy Anniversary Maa and Baba")


#main image
st.image("images/main.jpeg")

st.subheader("1. Calculate match percentage")
# Center using columns
col1, col2, col3 = st.columns([1.8, 2, 1])

with col2:
    st.markdown("""
        <style>
        div.stButton > button {
            background-color: red;
            color: white;
            height: 100px;
            width: 100%;
            font-size: 30px;
            border-radius: 15px;
            border: none;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    div[data-testid="stProgress"] > div > div > div {
        height: 30px;          /* thickness */
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)
    button = st.button("CLICK HERE")


col1, col2, col3 = st.columns([1, 5, 1])

with col2 :
    if button :

        with st.spinner("evaluating compatibility...") :

            progress = st.progress(0)
            text = st.empty()
            end = 0

            for i in range(91):
                time.sleep(0.03)
                progress.progress(i)
                text.write(f"{i}%")

            time.sleep(2.2)

            for i in range(10) :
                time.sleep(0.001)
                progress.progress(91+i)
                text.write(f"{i+91}%")

                if i+ 91 == 100 :
                    end = 1
            
            time.sleep(1)
            
            r = np.random.rand()
            if r > 0.15 :
                st.image("images/match.jpeg")
                st.markdown("***Congratulation your compatibility is 100%***")
            else :
                st.image("images/me.png")
                st.markdown("***Enjoy this amazing photo of your son***")
            if end == 1 :
                st.info("Press button again to re-evaluate")

st.markdown("<div style='height:400px;'></div>", unsafe_allow_html=True)

pressed = st.button("Press here to go down memory lane :)")

with open("images/img1.jpeg", "rb") as f:
    encoded1 = base64.b64encode(f.read()).decode()

with open("images/img2.jpeg", "rb") as f:
    encoded2 = base64.b64encode(f.read()).decode()

with open("images/img3.jpeg", "rb") as f:
    encoded3 = base64.b64encode(f.read()).decode()

with open("images/img4.jpeg", "rb") as f:
    encoded4 = base64.b64encode(f.read()).decode()

with open("images/img5.jpeg", "rb") as f:
    encoded5 = base64.b64encode(f.read()).decode()

img_list = [encoded1, encoded2, encoded3, encoded4, encoded5]



def slide_show() :
    fade = f"""
    <img id="slider" src="data:image/jpeg;base64,{img_list[0]}" 
    style="width:100%; max-width:500px; height:auto; opacity:0; display:block; margin:auto;">

    <style>
    #slider {{
        transition: opacity 1.5s ease-in-out;
        border-radius: 10px;
    }}
    </style>

    <script>
    const images = [
        "data:image/jpeg;base64,{img_list[1]}",
        "data:image/jpeg;base64,{img_list[2]}",
        "data:image/jpeg;base64,{img_list[3]}",
        "data:image/jpeg;base64,{img_list[4]}"
    ];

    let index = 0;
    const img = document.getElementById("slider");

    function showNextImage() {{
        img.style.opacity = 0;

        setTimeout(() => {{
            index = (index + 1) % images.length;
            img.src = images[index];
            img.style.opacity = 1;
        }}, 1500);
    }}

    setTimeout(() => {{
        img.style.opacity = 1;
    }}, 200);

    setInterval(showNextImage, 4000);
    </script>
    """

    components.html(fade, height=500)

if pressed :
    slide_show()
    time.sleep(6)
    st.markdown("## Stay Happy, Love You")

    time.sleep(4)
    st.warning("Note: Keep re-evaluating compatibility for a secret")