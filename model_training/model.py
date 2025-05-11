# Importing packages
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Loading data
df = pd.read_csv("data/train.csv")

print(f"The shape of the data is : {df.shape}")
print(f"Here is the list of columns: {df.columns}")

# Get more about the data
df.info()

# Getting possible values of the object variables
categorical_var_list = ["Warehouse_block", "Mode_of_Shipment", "Product_importance", "Gender"]
for i in categorical_var_list:
    print("-"*10)
    print(i)
    print("-"*10)
    print(f"Total unique values: {df[i].nunique()}")
    print(f"Unique values: {df[i].unique()}")

# =====================
# DATA PREPROCESSING
# =====================
# Dropping the ID column
df = df.drop(columns=["ID"])

# Label Encoding
for col in categorical_var_list:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# Define X and y
X = df.drop(columns=["Reached.on.Time_Y.N"])
y = df["Reached.on.Time_Y.N"]

# Splitting data into Train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"The shape of training data is : {X_train.shape}")
print(f"The shape of test data is : {X_test.shape}")

# =====================
# TRAINING MODEL
# =====================
# Model Definition
clf = RandomForestClassifier(n_estimators=500, random_state=42)

# Trainin model
clf.fit(X= X_train, y = y_train)

# Model Evaluation on the test data
score = clf.score(X_test, y_test)
print(f"Model Accuracy: {score: .1f}")

# =====================
# Save the model
# =====================
output_path = "models/model.pkl"
joblib.dump(clf, output_path)
print(f"model saved as {output_path}")