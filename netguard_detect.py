import joblib
import pandas as pd

# Load model + features
clf, FEATURES = joblib.load("models/netguard_model.pkl")

# Example network flows (12 features each)
flows = [
    [850, 0, 7200, 3500, 20, 1, 1, 0, 1, 0, 0, 0],   # normal-like
    [120, 1, 85000, 500, 600, 0, 0, 0, 0, 0, 1, 0], # attack-like
    [400, 0, 1500, 2000, 15, 1, 0, 0, 0, 0, 0, 0]   # normal-like
]

df = pd.DataFrame(flows, columns=FEATURES)
preds = clf.predict(df)

for i, p in enumerate(preds):
    label = "normal" if p == 0 else "attack"
    print(f"Flow {i+1} → {label}")
