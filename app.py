import streamlit as st
from dotenv import dotenv_values
from IPython.display import Image
from openai import OpenAI
import requests
import time
from qdrant_client import QdrantClient



st.markdown("""
    <style>
        .centered-title {
            color: white;
            text-align: center;
            font-size: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# Wyświetlamy tytuł z zastosowaniem klasy CSS
st.markdown('<h1 class="centered-title">App\'ka Kolorowanka</h1>', unsafe_allow_html=True)

st.markdown("""
    <style>
        .centered-text {
            text-align: center;
            font-size: 40px;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)
st.markdown('<h4 class="centered-text">Zanim zaczniesz zabawę - przeczytaj o stylach oraz poziomach!</h4>', unsafe_allow_html=True)

env = dotenv_values(".env")







with st.sidebar:
    example_name = st.selectbox(
        "Co chcesz wiedzieć?",
        [
            "Style kolorowanki",
            "Poziom kolorowanki",
        ],
    )


if example_name == "Style kolorowanki":

    tab0, tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Komiksowy (Cartoon)", 
    "Manga/Anime", 
    "Graffiti (Street Art)", 
    "Realistyczny", 
    "Surrealistyczny", 
    "Steampunk",
])
    with tab0:
        with st.expander("Wyświetl opis"):
            st.write(""" Styl rysowania komiksowy charakteryzuje się uproszczonymi kształtami i wyolbrzymionymi proporcjami postaci, często z dużymi oczami czy głowami. Kontury są grube i wyraziste. Mimika twarzy oraz gesty ciała są mocno przesadzone, co podkreśla emocje postaci. Tła są proste, a cieniowanie minimalne. Rysunki mogą zawierać elementy ruchu, jak linie szybkości czy wybuchy. Styl ten często wykorzystuje humor i absurd, nadając całości lekkości i dynamiki. """)
        with st.expander("Wyświetl przykład"):
            st.image("komiksowy_example.png")

    with tab1:
        with st.expander("Wyświetl opis"):
            st.write(""" Styl rysowania Manga/Anime charakteryzuje się szczegółowymi i realistycznymi proporcjami postaci, często z dużymi oczami, cienkimi nosami i delikatnymi ustami. Kontury są cienkie, a cieniowanie zaawansowane, często z użyciem delikatnych gradientów i szrafów. Tła bywają zarówno szczegółowe, jak i minimalistyczne, w zależności od sceny. Ekspresja emocji jest subtelna, ale wyraźna, z naciskiem na mimikę twarzy. Styl ten obejmuje zarówno realistyczne, jak i fantastyczne motywy, z dużą dynamiką w akcjach. Często spotyka się również charakterystyczne elementy jak błyszczące oczy czy stylizowane fryzury. """)
        with st.expander("Wyświetl przykład"):
            st.image("manga_anime_example.png")
    
    with tab2:
        with st.expander("Wyświetl opis"):
            st.write(""" Styl Graffiti (Street Art) charakteryzuje się żywymi, kontrastującymi kolorami oraz dużymi, dynamicznymi literami i obrazami. Często wykorzystuje wyraziste kontury i grube linie, a kompozycje są pełne energii i swobody. Wiele dzieł łączy elementy abstrakcji, realizmu i pop-artu, a postacie oraz symbole mogą być stylizowane lub przekształcone w sposób kreatywny. Tła są zazwyczaj proste, a techniki malowania mogą obejmować aerograf, szablony czy marker. Graffiti często przekazuje silne, społeczne lub polityczne przesłania. W tym stylu dominują często elementy uliczne i kultura młodzieżowa. """)
        with st.expander("Wyświetl przykład"):
            st.image("graffiti_example.png")

    with tab3:
        with st.expander("Wyświetl opis"):
            st.write(""" Styl realistyczny charakteryzuje się wiernym odwzorowaniem rzeczywistości z dużą dbałością o detale i proporcje. Postacie, obiekty i tła są przedstawiane tak, jak wyglądają w rzeczywistości, z naciskiem na naturalne światło, cienie i tekstury. Kolorystyka jest stonowana i zbliżona do prawdziwych odcieni, a cieniowanie jest subtelne, często z zastosowaniem precyzyjnych przejść tonalnych. W realistycznym stylu ważna jest także głębia obrazu i perspektywa, które mają na celu oddanie trójwymiarowości. W tym stylu artyści starają się uchwycić życie w najbardziej wierny sposób, co sprawia, że prace wyglądają niemal jak fotografie. """)
        with st.expander("Wyświetl przykład"):
            st.image("realistyczny_example.png")

    with tab4:
        with st.expander("Wyświetl opis"):
            st.write(""" Styl surrealistyczny charakteryzuje się łączeniem elementów rzeczywistych z wyobrażonymi, tworząc dziwne, nierealne kompozycje. Obrazy często przedstawiają sceny, które łamią zasady logiki, fizyki i proporcji, łącząc przedmioty w sposób, który wywołuje zaskoczenie lub niepokój. Kolorystyka bywa zróżnicowana – od stonowanych po intensywne, nasycone barwy, a cieniowanie może być subtelne lub bardziej wyraziste, zależnie od koncepcji. Często używa się motywów snów, iluzji optycznych, zniekształconych postaci czy fantastycznych krajobrazów, co ma na celu oddanie nieświadomych procesów umysłowych. Styl surrealistyczny wywołuje emocje, skłania do refleksji i zaskakuje swoją nietypową formą. """)
        with st.expander("Wyświetl przykład"):
            st.image("surrealistyczny_example.png")

    with tab5:
        with st.expander("Wyświetl opis"):
            st.write(""" Styl steampunk charakteryzuje się połączeniem elementów epoki wiktoriańskiej z fantastyką naukową i technologią z XIX wieku. Często występują tu zębatki, mechanizmy, parowe maszyny oraz futurystyczne wynalazki, które jednak mają wygląd retro. Postacie w tym stylu noszą odzież inspirowaną wiktoriańską modą, często z dodatkami, takimi jak gogle, zegary, skórzane akcesoria czy metalowe elementy. Kolorystyka obejmuje ciepłe odcienie miedzi, brązów, złota i mosiądzu, a tła często przedstawiają industrialne lub alternatywne światy. Styl ten łączy elementy fantasy, technologii, sztuki użytkowej i retro-futurystycznego designu. Steampunk tworzy unikalną atmosferę, łącząc przeszłość z wyobrażeniami o przyszłości. """)
        with st.expander("Wyświetl przykład"):
            st.image("steampunk_example.png")


elif example_name == "Poziom kolorowanki":

    tab0, tab1, tab2, tab3 = st.tabs([
    "Bardzo Proste", 
    "Proste (mało skomplikowane)", 
    "Średniozaawansowane", 
    "Zaawansowane (expert)", 
])
    with tab0:
        with st.expander("Wyświetl opis"):
            st.write(""" Rysunki o prostych kształtach i minimalnych detalach. Skupiają się na podstawowych formach, takich jak okręgi, kwadraty i linie. Często są to postacie lub obiekty w stylu kreskówkowym lub symbolicznym, idealne dla początkujących. """)
        with st.expander("Wyświetl przykład"):
            st.image("bardzo_proste_example.png")

    with tab1:
        with st.expander("Wyświetl opis"):
            st.write(""" Obrazy z niewielką liczbą szczegółów, ale z bardziej wyrazistą strukturą. Postacie mają podstawowe proporcje, z naciskiem na formy i kolory, z minimalnym cieniowaniem. To poziom, który wymaga pewnej biegłości w rysowaniu, ale nie jest jeszcze trudny. """)
        with st.expander("Wyświetl przykład"):
            st.image("proste_example.png")

    with tab2:
        with st.expander("Wyświetl opis"):
            st.write(""" Rysunki zawierają bardziej złożone detale, precyzyjniejsze proporcje i wyraźne cieniowanie. Postacie oraz tła są bardziej szczegółowe, a kompozycje wymagają lepszej kontroli nad światłem i cieniami. To etap, w którym zaczyna się pracować nad realistycznymi efektami. """)
        with st.expander("Wyświetl przykład"):
            st.image("srednio_example.png")

    with tab3:
        with st.expander("Wyświetl opis"):
            st.write(""" Wysokiej jakości rysunki z dużą ilością detali i zaawansowanym cieniowaniem. Proporcje postaci są perfekcyjnie dopracowane, a techniki rysunkowe (np. światło, tekstura, perspektywa) są na najwyższym poziomie. Artyści na tym poziomie tworzą prace realistyczne lub artystyczne, pełne subtelności i finezji. """)
        with st.expander("Wyświetl przykład"):
            st.image("expert_example.png")



@st.cache_resource
def get_openai_client():
    return OpenAI(api_key=st.session_state["openai_api_key"])

# Funkcja generująca tekst
def generate_text(prompt):
    openai_client = get_openai_client()
    res = openai_client.chat.completions.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": """
                Jesteś pomocnikiem, który pomaga wybrać elementy do kolorowanki dla dzieci.
                Bądź bardzo kreatywny i konkretny. Niech to będzie zabawne. Ogranicz się do przedstawienia elementów, nie używaj żadnych kolorów. Drobne detale. 
                Pamiętaj, że jest to kolorowanka dla dzieci do 18 roku życia, więc nie może być przemocy i innych niestosownych rzeczy. 
                Ogranicz się do 300 znaków. Zawsze daj gotowy jeden pomysł. 
                """
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
    )
    return res.choices[0].message.content

def generate_new_text(prompt):
    # Generowanie nowej odpowiedzi
    new_response = generate_text(prompt)
    st.session_state["response"] = new_response  # Przypisujemy nową odpowiedź do session_state
    # Resetujemy inne zmienne, aby aplikacja ponownie się załadowała
    st.session_state["style_selected"] = False
    st.session_state["ready_to_generate"] = False

    # Wymuszenie odświeżenia aplikacji
    st.rerun()  # Używamy rerun, aby aplikacja zaktualizowała stan i widok

def generate_image(
    text,
    output_path,
    style,
    level
):
    try:
        if style == "Komiksowy (Cartoon)":
            prompt = f"{text} Rysuj obrazek w stylu komiksowym, z grubymi, wyraźnymi konturami, uproszczonymi kształtami, dużymi oczami. Dodaj odrobinę humoru i absurdu."
        elif style == "Manga/Anime":
            prompt = f"{text} Rysuj obrazek w stylu manga/anime, z dużymi oczami postaci, szczegółowymi fryzurami, ekspresyjnymi pozami i wyrazistymi konturami. Tło powinno być dynamiczne, ale nie zbyt skomplikowane."
        elif style == "Graffiti (Street Art)":
            prompt = f"{text} Rysuj obrazek w stylu graffiti, z odważnymi konturami, dużymi kształtami i elementami abstrakcyjnymi. Dodaj graffiti-style litery i mocny uliczny młodzieżowy klimat."
        elif style == "Realistyczny":
            prompt = f"{text} Rysuj obrazek w stylu realistycznym, z dokładnymi detalami, realistycznymi proporcjami postaci i obiektów. Użyj subtelnych konturów, aby zachować realizm."
        elif style == "Surrealistyczny":
            prompt = f"{text} Rysuj obrazek w stylu surrealistycznym, z dziwacznymi, nierealnymi elementami, które łamią zasady logiki. Wykorzystaj nieoczekiwane połączenia, zniekształcone kształty i abstrakcyjne formy."
        elif style == "Steampunk":
            prompt = f"{text} Rysuj obrazek w stylu steampunk, z elementami wiktoriańskimi, maszynami parowymi, zębatkami i retro-futurystycznymi wynalazkami. Dodaj szczegóły metaliczne i mechaniczne, zachowując wyraźne kontury."



        if level == "Bardzo Proste (Dla najmłodszych artystów)":
            prompt += f"{text} Rysuj obrazek z grubymi konturami, dużymi, prostymi kształtami, bez szczegółów, dużo przestrzeni do wypełnienia."
        elif level == "Proste (Mało skomplikowane)":
            prompt += f"{text} Rysuj obrazek z wyraźnymi konturami, z kilkoma detalami na postaciach i prostym tłem, dużo przestrzeni do wypełnienia."
        elif level == "Średniozaawansowane (Dla średnio zaawansowanych artystów)":
            prompt += f"{text} Rysuj obrazek z wyraźnymi konturami, dużo szczegółów, tło z kilkoma elementami krajobrazu, dużo przestrzeni do wypełnienia"
        elif level == "Zaawansowane (Poziom expert z dużą ilością szczegółów)":
            prompt += f"{text} Rysuj obrazek z wyraźnymi konturami, bardzo dużo szczegółów, złożone tło, detale w postaciach, dużo przestrzeni do wypełnienia"

        openai_client = get_openai_client()
        response = openai_client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        with open(output_path, "wb") as f:
            f.write(requests.get(response.data[0].url).content)

        return Image(output_path)
    except Exception as e:
        # Obsługa błędu: wyświetlenie komunikatu o błędzie
        st.error("Nie udało się wygenerować obrazu. Spróbuj ponownie później.")
        print(f"Error during image generation: {e}")
        return None

@st.cache_resource
def get_qdrant_client():
    return QdrantClient(
    url=env["QDRANT_URL"], 
    api_key=env["QDRANT_API_KEY"],
)

style_kolorowanki = [
    "Komiksowy (Cartoon)", 
    "Manga/Anime", 
    "Graffiti (Street Art)", 
    "Realistyczny", 
    "Surrealistyczny", 
    "Steampunk",
]
level_kolorowanki = [
    "Bardzo Proste (Dla najmłodszych artystów)", 
    "Proste (Mało skomplikowane)", 
    "Średniozaawansowane (Dla średnio zaawansowanych artystów)", 
    "Zaawansowane (Poziom expert z dużą ilością szczegółów)",
]

# OpenAI API key protection
if not st.session_state.get("openai_api_key"):
    if "OPENAI_API_KEY" in env:
        st.session_state["openai_api_key"] = env["OPENAI_API_KEY"]

    else:
        st.info("Dodaj swój klucz API OpenAI aby móc korzystać z tej aplikacji")
        st.session_state["openai_api_key"] = st.text_input("Klucz API", type="password")
        if st.session_state["openai_api_key"]:
            st.rerun()

if not st.session_state.get("openai_api_key"):
    st.stop()



# Inicjalizowanie zmiennych w session_state, jeśli jeszcze nie istnieją
if 'prompt' not in st.session_state:
    st.session_state["prompt"] = ""
if 'response' not in st.session_state:
    st.session_state["response"] = ""    
if 'style_selected' not in st.session_state:
    st.session_state["style_selected"] = False
if 'level_selected' not in st.session_state:
    st.session_state["level_selected"] = False
if 'ready_to_generate' not in st.session_state:
    st.session_state["ready_to_generate"] = False
if 'selected_style' not in st.session_state:
    st.session_state["selected_style"] = None  
if 'selected_level' not in st.session_state:
    st.session_state["selected_level"] = None  
if 'new_file_ready' not in st.session_state:
    st.session_state["new_file_ready"] = None
if 'image_path' not in st.session_state:
    st.session_state["image_path"] = None
if 'image_generated' not in st.session_state:
    st.session_state["image_generated"] = False

    

prompt = st.text_input("Podaj temat kolorowanki", value=st.session_state.get("prompt", ""))

if prompt != st.session_state.get("prompt", ""):
    progress_text = "Trwa generowanie propozycji"
    progress_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1, text=progress_text)
            
    
    st.session_state["response"] = generate_text(prompt)  # Generowanie nowego tekstu
    st.session_state["prompt"] = prompt
    time.sleep(0.5)
    progress_bar.empty()



# Jeżeli mamy odpowiedź, wyświetlamy propozycję kolorowanki
if st.session_state.get("response"):
    st.markdown(f"### Propozycja kolorowanki:\n{st.session_state['response']}")

    

 

    col1, col2 = st.columns([15, 5])
    with col1:
        prepare_image = st.button("Podoba mi się!")
        if prepare_image:
            
            with st.status("Obieram ziemniaki...", expanded=True) as status:
                time.sleep(1)
                st.write("Kroję cebulę...")
                time.sleep(1)
                st.write("Może Ci to zaimponuję...")
                time.sleep(1)
                status.update(label="Możemy przystąpić do generowania obrazu!", state="complete", expanded=False)
            st.session_state["style_selected"] = True

            

    with col2:
        change_prompt = st.button("Nie podoba mi się") # Reset propozycji 
        if change_prompt:
            st.session_state["new_file_ready"] = False
            st.session_state["response"] = ""  # Resetowanie odpowiedzi
            st.session_state["style_selected"] = False  # Resetowanie wyboru stylu
            st.session_state["selected_style"] = None  # Resetowanie wybranego stylu
            st.session_state["selected_level"] = None  # Resetowanie wybranego poziomu
            st.session_state["level_selected"] = False  # Resetowanie poziomu
            st.session_state["ready_to_generate"] = False  # Resetowanie gotowości do generowania
            st.session_state["image_path"] = None
            st.session_state["image_generated"] = False
            
            progress_text = "Trwa generowanie nowej propozycji"
            progress_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.01)
                progress_bar.progress(percent_complete + 1, text=progress_text)
            generate_new_text(prompt)
            time.sleep(0.5)
            progress_bar.empty()
            
            
    # Po kliknięciu "Podoba mi się" wyświetlamy wybór stylu
    if st.session_state["style_selected"]:
        st.session_state["selected_style"] = st.selectbox(
            "Wybierz styl kolorowanki:", 
            style_kolorowanki
        )
        st.session_state["level_selected"] = False  # Pokaż wybór poziomu po wybraniu stylu

    # Po wybraniu stylu, wyświetlamy wybór poziomu
    if st.session_state["selected_style"]:
        st.session_state["selected_level"] = st.selectbox(
            "Wybierz poziom kolorowanki:",
            level_kolorowanki
        )
        st.session_state["ready_to_generate"] = False
    
    if st.session_state["selected_level"]:
        st.session_state["ready_to_generate"] = True

    # Generowanie obrazka
    if st.session_state["ready_to_generate"]:
        ready_to_generate = st.button("Wygeneruj kolorowankę")
        if ready_to_generate:
            output_path = "kolorowanka.png" # ścieżka zapisu
            progress_text = "RYSUJĘ KRESKI... GWOŹDZIE... PINEZKI... LATAJĄ OŁÓWKI - MOŻE ZJESZ SOBIE TRZY KRÓWKI?"
            progress_bar = st.progress(0, text=progress_text)
            for percent_complete in range(100):
                time.sleep(0.02)
                progress_bar.progress(percent_complete + 1, text=progress_text)
            generate_image(
                text=f"Biała kartka, czarne kontury, tylko białe i czarne elementy, żadnych innych kolorów. "
                    f"styl ({st.session_state['selected_style']}), "
                    f"poziom obrazka ({st.session_state['selected_level']}), "
                    f"temat to ({st.session_state['response']})",
                output_path=output_path,
                level=st.session_state['selected_level'],
                style=st.session_state['selected_style']
            )
            
            time.sleep(0.1)
            progress_bar.empty()
            st.success("Już wszystko gotowe, możesz pobrać swoje arcydzieło!")

            st.session_state["image_path"] = output_path
            st.session_state["image_generated"] = True
        

            # Wyświetlanie obrazka natychmiast po wygenerowaniu
    if st.session_state["image_path"]:
        st.image(st.session_state["image_path"], caption="Wygenerowana kolorowanka", use_container_width=True)

    

        # Przycisk do pobierania kolorowanki
        with open(st.session_state["image_path"], "rb") as file:
            st.download_button(
                label="Pobierz kolorowankę",
                data=file,
                file_name="kolorowanka.png",
                mime="image/png"
            )

            
            

else:
    st.write("Czekam na Twoją propozycję!")


# Nowy projekt
if st.session_state.get("image_generated"):
    new_file = st.button("Nowy projekt")
    if new_file:
        # Reset wszystkiego
        st.warning("Wszystkie wybory zostały zresetowane. Rozpoczynasz nowy projekt.")
        st.session_state["prompt"] = ""
        st.session_state["response"] = ""
        st.session_state["ready_to_generate"] = False
        st.session_state["style_selected"] = False
        st.session_state["selected_style"] = None
        st.session_state["selected_level"] = None
        st.session_state["new_file_ready"] = False
        st.session_state["image_path"] = None  
        st.session_state["image_generated"] = False
        st.rerun()



