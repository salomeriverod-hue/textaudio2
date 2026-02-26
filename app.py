import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image
import base64

st.title("Fábulas infantiles")
image = Image.open('ricitos de oro.jpg')
st.image(image, width=1000)
with st.sidebar:
    st.subheader("Esrcibe y/o selecciona texto para ser escuchado.")


try:
    os.mkdir("temp")
except:
    pass

st.subheader("Ricitos de oro")
st.write('Érase una vez una familia de osos que vivían en una linda casita en el bosque. Papá Oso era muy grande, Mamá Osa era de tamaño mediano y Osito era pequeño.

Una mañana, Mamá Osa sirvió la más deliciosa avena para el desayuno, pero como estaba demasiado caliente para comer, los tres osos decidieron ir de paseo por el bosque mientras se enfriaba. Al cabo de unos minutos, una niña llamada Ricitos de Oro llegó a la casa de los osos y tocó la puerta. Al no encontrar respuesta, abrió la puerta y entró en la casa sin permiso.

En la cocina había una mesa con tres tazas de avena: una grande, una mediana y una pequeña. Ricitos de Oro tenía un gran apetito y la avena se veía deliciosa. Primero, probó la avena de la taza grande, pero la avena estaba muy fría y no le gustó. Luego, probó la avena de la taza mediana, pero la avena estaba muy caliente y tampoco le gustó. Por último, probó la avena de la taza pequeña y esta vez la avena no estaba ni fría ni caliente, ¡estaba perfecta! La avena estaba tan deliciosa que se la comió toda sin dejar ni un poquito.

Después de comer el desayuno de los osos, Ricitos de Oro fue a la sala. En la sala había tres sillas: una grande, una mediana y una pequeña. Primero, se sentó en la silla grande, pero la silla era muy alta y no le gustó. Luego, se sentó en la silla mediana, pero la silla era muy ancha y tampoco le gustó. Fue entonces que encontró la silla pequeña y se sentó en ella, pero la silla era frágil y se rompió bajo su peso.

Buscando un lugar para descansar, Ricitos de Oro subió las escaleras, al final del pasillo había un cuarto con tres camas: una grande, una mediana y una pequeña. Primero, se subió a la cama grande, pero estaba demasiado dura y no le gustó. Después, se subió a la cama mediana, pero estaba demasiado blanda y tampoco le gustó. Entonces, se acostó en la cama pequeña, la cama no estaba ni demasiado dura ni demasiado blanda. De hecho, ¡se sentía perfecta! Ricitos de Oro se quedó profundamente dormida.

Al poco tiempo, los tres osos regresaron del paseo por el bosque. Papá Oso notó inmediatamente que la puerta se encontraba abierta:

—Alguien ha entrado a nuestra casa sin permiso, se sentó en mi silla y probó mi avena —dijo Papá Oso con una gran voz de enfado.

—Alguien se ha sentado en mi silla y probó mi avena —dijo Mamá Osa con una voz medio enojada.

Entonces, dijo Osito con su pequeña voz:

—Alguien se comió toda mi avena y rompió mi silla.

Los tres osos subieron la escalera. Al entrar en la habitación, Papá Oso dijo:

—¡Alguien se ha acostado en mi cama!

Y Mamá Osa exclamó:

—¡Alguien se ha acostado en mi cama también!

Y Osito dijo:

—¡Alguien está durmiendo en mi cama! —y se puso a llorar desconsoladamente.

El llanto de Osito despertó a Ricitos de Oro, que muy asustada saltó de la cama y corrió escaleras abajo hasta llegar al bosque para jamás regresar a la casa de los osos.')
           
st.markdown(f"Quieres escucharlo?, copia el texto")
text = st.text_area("Ingrese El texto a escuchar.")

tld='com'
option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English"))
if option_lang=="Español" :
    lg='es'
if option_lang=="English" :
    lg='en'

def text_to_speech(text, tld,lg):
    
    tts = gTTS(text,lang=lg) # tts = gTTS(text,'en', tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

if st.button("convertir a Audio"):
     result, output_text = text_to_speech(text, 'com',lg)#'tld
     audio_file = open(f"temp/{result}.mp3", "rb")
     audio_bytes = audio_file.read()
     st.markdown(f"## Tú audio:")
     st.audio(audio_bytes, format="audio/mp3", start_time=0)

     #if display_output_text:
     
     #st.write(f" {output_text}")
    
#if st.button("ElevenLAabs",key=2):
#     from elevenlabs import play
#     from elevenlabs.client import ElevenLabs
#     client = ElevenLabs(api_key="a71bb432d643bbf80986c0cf0970d91a", # Defaults to ELEVEN_API_KEY)
#     audio = client.generate(text=f" {output_text}",voice="Rachel",model="eleven_multilingual_v1")
#     audio_file = open(f"temp/{audio}.mp3", "rb")

     with open(f"temp/{result}.mp3", "rb") as f:
         data = f.read()

     def get_binary_file_downloader_html(bin_file, file_label='File'):
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href
     st.markdown(get_binary_file_downloader_html("audio.mp3", file_label="Audio File"), unsafe_allow_html=True)

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
