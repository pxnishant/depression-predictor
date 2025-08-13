# Depression Predictor

We use a **Logistic Regression** model to predict whether a **college student** is likely to be experiencing depression, based on age, location, lifestyle, academic, and work-related factors.
The model uses a **Streamlit** web app where a user can enter information and get predictions.

[Link](https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset) to the dataset used for training.

## Factors Considered

  * Gender
  * Age
  * City
  * Academic Pressure (0–5)
  * Work Pressure (0–5)
  * CGPA (0-10)
  * Study Satisfaction (0–5)
  * Job Satisfaction (0–5)
  * Sleep Duration
  * Dietary Habits
  * Degree
  * Suicidal Thoughts (Yes/No)
  * Study Hours per Day (0–24)
  * Financial Stress (0–5)
  * Family History of Mental Illness (Yes/No)

## Details

* **Algorithm:** Logistic Regression
* **Preprocessing:**

  * **Categorical**: One-Hot Encoding (nominal) and Ordinal Encoding (ordered categories)
  * **Numeric**: Standard Scaling
* **Target Variable:** `depression` (0 or 1)

The model was trained on a dataset containing data for college students, focusing on lifestyle, academic, and work-related mental health indicators.
