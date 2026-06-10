# 🍷 Wine Quality Prediction App

A machine learning web application that predicts whether a red wine is **Good Quality** or **Not Good Quality** based on its chemical properties — built with Python, Scikit-learn, and Streamlit.

---

## 📌 Project Overview

| Property | Detail |
|---|---|
| **Model** | Random Forest Classifier |
| **Dataset** | UCI Red Wine Quality (1,599 samples) |
| **Task** | Binary Classification |
| **Accuracy** | 93.12% |
| **Deployment** | Streamlit |

> **Label Logic:** Wine with quality score **≥ 7 → Good (1)**, else **Not Good (0)**

---

## 🚀 Live Demo

👉 [Click here to try the app](https://your-streamlit-app-link.streamlit.app)

---

## 📂 Project Structure

```
wine_quality_app/
│
├── app.py               # Streamlit web application
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Tech Stack

- **Python 3.x**
- **Scikit-learn** — Random Forest Classifier
- **Pandas & NumPy** — Data processing
- **Streamlit** — Web app deployment

---

## 🧪 Input Features

| Feature | Description |
|---|---|
| Fixed Acidity | Most acids in wine (tartaric, malic, citric) |
| Volatile Acidity | Amount of acetic acid (vinegar taste) |
| Citric Acid | Adds freshness and flavor |
| Residual Sugar | Sugar remaining after fermentation |
| Chlorides | Amount of salt in wine |
| Free Sulfur Dioxide | Prevents microbial growth & oxidation |
| Total Sulfur Dioxide | Free + bound forms of SO₂ |
| Density | Density of wine (water = 1) |
| pH | Acidity level (0–14 scale) |
| Sulphates | Wine additive contributing to SO₂ |
| Alcohol | Percentage of alcohol content |

---

## ✅ Good Quality Test Values

Use these values in the app to get a 🟢 **Good Quality** prediction:

```
Fixed Acidity      : 12.8
Volatile Acidity   : 0.30
Citric Acid        : 0.74
Residual Sugar     : 2.6
Chlorides          : 0.095
Free SO₂           : 9.0
Total SO₂          : 28.0
Density            : 0.9994
pH                 : 3.20
Sulphates          : 0.77
Alcohol            : 10.8
→ Result: 🟢 Good Quality Wine | Confidence: 93%
```

---

## 🛠️ Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/your-username/wine-quality-prediction.git
cd wine-quality-prediction
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

**4. Open in browser**
```
http://localhost:8501
```

---

## ☁️ Deploy on Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click **New App** → Connect your GitHub repo
4. Set **Main file:** `app.py`
5. Click **Deploy** 🚀

---

## 📊 Model Performance

```
Dataset Split  : 80% Train / 20% Test
Train Samples  : 1,279
Test Samples   :   320
Accuracy       : 93.12%
```

**Key Insight:** Alcohol % has the strongest **positive correlation** with wine quality.
Volatile acidity has the strongest **negative correlation**.

---

## 📸 Screenshots

> * <img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/668c459c-45fc-4c29-b5f7-6360247d6738" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/1cdd9f7f-69a6-43a7-9368-a00c11f3b524" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/c9161a6d-836e-40ac-a22b-5ed541efb769" />




---

## 🙋‍♂️ Author

**Your Name**
- LinkedIn: [linkedin.com/in/your-profile](https://linkedin.com/in/your-profile)
- GitHub: [github.com/your-username](https://github.com/your-username)

---

## 📃 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ **If you found this helpful, please star the repo!**
