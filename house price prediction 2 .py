import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# 1. Create a synthetic dataset (Simulating real-estate records)
np.random.seed(42)
n_samples = 1000

data = {
    'Size_sqft': np.random.randint(800, 5000, n_samples),
    'Bedrooms': np.random.randint(1, 6, n_samples),
    'Age_years': np.random.randint(0, 50, n_samples),
    'Location': np.random.choice(['Urban', 'Suburban', 'Rural'], n_samples),
    # Price is generated using a formula + random noise
    'Price_USD': None 
}

df = pd.DataFrame(data)
df['Price_USD'] = (
    df['Size_sqft'] * 150 + 
    df['Bedrooms'] * 25000 - 
    df['Age_years'] * 1200 + 
    np.where(df['Location'] == 'Urban', 50000, np.where(df['Location'] == 'Suburban', 20000, 0)) +
    np.random.normal(0, 15000, n_samples)
)

# 2. Split features (X) and target variable (y)
X = df.drop(columns=['Price_USD'])
y = df['Price_USD']

# 3. Separate numerical and categorical features
numeric_features = ['Size_sqft', 'Bedrooms', 'Age_years']
categorical_features = ['Location']

# 4. Create preprocessing pipelines
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# 5. Bundle preprocessing and the model into a final pipeline
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

# 6. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 7. Train the model
model_pipeline.fit(X_train, y_train)

# 8. Evaluate model performance
y_pred = model_pipeline.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error (MAE): ${mae:,.2f}")
print(f"R² Score (Accuracy Metric): {r2:.4f}")

# 9. Predict price for a brand-new house listing
new_house = pd.DataFrame({
    'Size_sqft': [2500],
    'Bedrooms': [3],
    'Age_years': [5],
    'Location': ['Suburban']
})

predicted_price = model_pipeline.predict(new_house)
print(f"\nPredicted Price for the new house: ${predicted_price[0]:,.2f}")
