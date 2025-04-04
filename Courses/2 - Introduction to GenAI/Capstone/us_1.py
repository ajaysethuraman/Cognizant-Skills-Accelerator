# -*- coding: utf-8 -*-
"""US_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yPCo1I31772gkiKnVbhyeIpa9pZuTkPW
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import fetch_openml

# Load dataset (using a publicly available dataset from OpenML)
data = fetch_openml(name="UCI-student-performance-mat", version=1, as_frame=True)
df = data.frame

# Selecting relevant features (study time, past scores, absences)
features = ['studytime', 'failures', 'absences', 'G1', 'G2']
target = 'G3'  # Final exam grade

print(df.columns)

df['pass'] = df['G3'] >= 10  # Creating a binary classification label
X = df[features]
y = df['pass'].astype(int)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print(report)

# Feature importance visualization
plt.figure(figsize=(8, 5))
sns.barplot(x=model.feature_importances_, y=features)
plt.title('Feature Importance')
plt.show()

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import fetch_openml

# Load dataset (using a publicly available dataset from OpenML)
data = fetch_openml(name="UCI-student-performance-mat", version=1, as_frame=True)
df = data.frame

# Selecting relevant features (study time, past scores, absences)
features = ['studytime', 'failures', 'absences', 'G1', 'G2']
target = 'G3'  # Final exam grade

df['pass'] = df['G3'] >= 10  # Creating a binary classification label
X = df[features]
y = df['pass'].astype(int)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy:.2f}')
print(report)

# Feature importance visualization
plt.figure(figsize=(8, 5))
sns.barplot(x=model.feature_importances_, y=features)
plt.title('Feature Importance')
plt.show()