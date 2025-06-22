# 📊 Student Sentiment Analysis (Norwegian to English)

This project analyzes free-text student evaluations written in Norwegian. It translates the statements to English, performs sentiment analysis using VADER, and generates visual insights like sentiment distribution, word clouds, and statement length comparisons.

---

## 🚀 Features

- 🔁 **Automatic Translation** (Norwegian → English)
- 🧠 **Sentiment Analysis** using NLTK VADER
- ☁️ **Word Clouds** for each sentiment category
- 📈 **Visualization** of sentiment distribution and text lengths
- 📦 **Excel Export** with translated text and sentiment labels

---

## 📂 Input

Place an Excel file in the project root named:

```
dummy_student_evaluations.xlsx
```

With **one column** of free-text student feedback, like:

| original_text                         |
|--------------------------------------|
| Jeg synes forelesningene går for fort |
| Filmen var vanskelig å forstå         |
| Læreren var engasjert og tydelig      |

---

## 📊 Output

The script will produce:

- PNG word cloud images: `positive.png`, `neutral.png`, `negative.png`
- Sentiment distribution bar plot
- Boxplot of text lengths by sentiment
- Excel file: `NO/EN Evalueringer.xlsx` with translations and sentiment labels

---

## 🧰 Requirements

Install dependencies via:

```bash
pip install pandas matplotlib seaborn nltk wordcloud deep-translator openpyxl
```

Also, NLTK resources are downloaded automatically:

```python
nltk.download('punkt')
nltk.download('vader_lexicon')
```

---

## 🧠 Methodology

1. **Translate** Norwegian statements using `deep-translator` (Google Translate).
2. **Analyze sentiment** using `SentimentIntensityAnalyzer` from `nltk`.
3. **Categorize** each entry as `Positive`, `Neutral`, or `Negative`.
4. **Visualize** insights with `seaborn` and `matplotlib`.
5. **Generate word clouds** while filtering out common Norwegian stopwords.

---

## 📤 Output Preview

<img src="positive .png" width="400"/>  
<img src="negative .png" width="400"/>  
<sub>Example: Word clouds from translated statements</sub>

---

## 📝 License

MIT License — free to use, adapt, and share!

---

## 👨‍🏫 Created by

Magnus H. Blystad — Associate Professor in Psychology  
Special interest in NLP, sentiment analysis, and educational tech.
