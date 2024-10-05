from openai import OpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def generate_image(prompt, usuario):
  response = client.images.generate(
    model="dall-e-3",
    prompt=f"Prompt engineer: {prompt} n\
      Entrada do projeta: {usuario}",
    size="1024x1024",
    quality="standard",
    n=1,
  )
  return response.data[0].url

st.title("Play Profético")
st.write("Peça ao espirito santo uma palavra profética e fale o que ele te mostrar")

user_input = st.text_input("o que o espirito santo te mostrou?")

if user_input:
  prompt_engineer = "A partir de agora você é artista de artes proféticas, irá receber \
  algumas palavras proféticas e deverá desenhar de acordo com o usuario dizer"
  image_url = generate_image(prompt_engineer, user_input)
  st.write("Aqui está a imagem que o espirito santo te mostrou, se não gostar, recarregua a pagina e tente novamente")
  st.image(image_url, width=700)