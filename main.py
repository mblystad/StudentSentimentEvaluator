# Importerer nødvendige biblioteker
import pandas as pd  # For databehandling av Excel-ark
import nltk  # Natural Language Toolkit – brukes for språkverktøy (f.eks. sentimentanalyse)
import matplotlib.pyplot as plt  # For grafer og figurer
import seaborn as sns  # For forbedrede matplotlib-plott
from wordcloud import WordCloud  # For å generere ordskyer
from nltk.sentiment import SentimentIntensityAnalyzer  # VADER sentimentanalyse
from deep_translator import GoogleTranslator  # Automatisk oversettelse fra norsk til engelsk

# Laster ned nødvendige ressurser fra NLTK
nltk.download('punkt')  # Ord- og setningsdeling
nltk.download('vader_lexicon')  # Ordlista som brukes av VADER for å analysere tonefall

# Leser inn Excel-filen som inneholder studentenes evalueringsutsagn
df = pd.read_excel("dummy_student_evaluations.xlsx")  # Sørg for at filnavnet stemmer
df.columns = ["original_text"]  # Standardiserer kolonnenavn til "original_text"

# Oversetter hver norsk tekstlinje til engelsk for at sentimentanalyse skal fungere (VADER fungerer best på engelsk)
df["english_text"] = df["original_text"].astype(str).apply(
    lambda x: GoogleTranslator(source='auto', target='en').translate(x)
)

# Initialiserer VADER sentimentanalysatoren
sia = SentimentIntensityAnalyzer()

# Funksjon som klassifiserer tekst som positiv, negativ eller nøytral basert på VADER-score
def get_sentiment(text):
    score = sia.polarity_scores(text)
    if score['compound'] >= 0.05 and score['pos'] > score['neg']:
        return "Positive"
    elif score['compound'] <= -0.05 and score['neg'] > score['pos']:
        return "Negative"
    else:
        return "Neutral"

# Bruker funksjonen til å kategorisere hver oversatt tekst
df["sentiment"] = df["english_text"].apply(get_sentiment)

# 📊 Plotter fordeling av sentimentkategorier
plt.figure(figsize=(6, 4))
sns.countplot(x="sentiment", data=df, palette="coolwarm")
plt.title("Sentimentfordeling i studentuttalelser")
plt.xlabel("Kategori")
plt.ylabel("Antall utsagn")
plt.tight_layout()
plt.show()

# 🛑 Liste over vanlige norske stoppord (blir fjernet fra ordskyer for bedre innsikt)
norske_stoppord = {
    "og", "i", "jeg", "det", "at", "en", "et", "den", "til", "er", "som", "på",
    "de", "med", "han", "av", "ikke", "ikkje", "så", "men", "vi", "om", "da",
    "du", "seg", "har", "kan", "blir", "for", "å", "var", "meg", "deg", "oss",
    "hva", "hvem", "hvor", "når", "hvordan", "hvorfor", "alle", "noe", "noen",
    "dette", "disse", "man", "min", "ditt", "sin", "sitt", "vår", "deres",
    "hans", "hennes", "være", "hadde", "skulle", "kunne", "ville", "måtte",
    "gjøre", "si"
}

# ☁️ Genererer og viser ordskyer for hvert sentiment (basert på *norske* tekster)
for sentiment, color in zip(["Positive", "Neutral", "Negative"], ["white", "lightgrey", "black"]):
    # Samler alle tekstene innenfor én kategori
    text = " ".join(df[df["sentiment"] == sentiment]["original_text"].astype(str))
    if text.strip():  # Hopper over tomme strenger
        # Lager ordsky, fjerner stoppord og justerer farger
        wordcloud = WordCloud(
            width=800,
            height=400,
            background_color=color,
            colormap="viridis",
            stopwords=norske_stoppord
        ).generate(text)

        # Viser ordskyen
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.title(f"Ordsky for {sentiment.lower()} utsagn")
        plt.savefig(f"{sentiment.lower()} .png", bbox_inches="tight", dpi=300)  # Valgfri: lagrer som PNG
        plt.tight_layout()
        plt.show()

# 📏 Undersøker lengden (antall ord) på hvert utsagn og sammenligner mellom sentimentgrupper
df["text_length"] = df["original_text"].apply(lambda x: len(str(x).split()))
plt.figure(figsize=(6, 4))
sns.boxplot(x="sentiment", y="text_length", data=df, palette="pastel")
plt.title("Lengde på utsagn etter sentiment")
plt.xlabel("Sentimentkategori")
plt.ylabel("Antall ord")
plt.tight_layout()
plt.show()

# 💾 Eksporterer data med originaltekst, oversettelse og sentiment til ny Excel-fil
df[["original_text", "english_text", "sentiment"]].to_excel("NO/EN Evalueringer.xlsx", index=False)
print("Saved to: evaluations_with_sentiment.xlsx")
