import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
df = pd.read_csv("data/raw/shipments.csv")
X = pd.get_dummies(df[['carrier','warehouse','distance_km','is_rainy','is_weekend']], drop_first=True)
y = (~df['on_time']).astype(int)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3, random_state=42)
m = RandomForestClassifier(random_state=42).fit(X_train,y_train)
print(f"Delay prediction accuracy: {m.score(X_test,y_test):.2f}")
imp = pd.DataFrame({'driver':X.columns,'importance':m.feature_importances_}).sort_values('importance', ascending=False)
imp.to_csv("data/processed/delay_drivers.csv", index=False)
print(imp.head(8))
