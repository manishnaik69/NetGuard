import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Feature names
FEATURES = [
    'duration_ms','protocol','src_bytes','dst_bytes','packets',
    'syn','ack','rst','fin','land','wrong_fragment','urgent'
]

# Generate synthetic but realistic flows
def generate_flows(n_samples=1000):
    flows = []
    labels = []
    for _ in range(n_samples):
        # normal flow
        flows.append([
            np.random.randint(100, 1000),  # duration_ms
            0,                             # protocol TCP
            np.random.randint(500, 8000),  # src_bytes
            np.random.randint(500, 5000),  # dst_bytes
            np.random.randint(5, 30),      # packets
            np.random.randint(0, 2),       # syn
            np.random.randint(0, 2),       # ack
            0,                             # rst
            np.random.randint(0, 2),       # fin
            0, 0, 0                        # land, wrong_fragment, urgent
        ])
        labels.append(0)  # normal

        # attack flow
        flows.append([
            np.random.randint(50, 300),    # duration_ms
            np.random.randint(0, 2),       # protocol TCP/UDP
            np.random.randint(10000, 100000),  # src_bytes
            np.random.randint(100, 5000),      # dst_bytes
            np.random.randint(100, 1000),      # packets
            0, 0, 0, 0, 0, 1, 0                # flags, wrong_fragment
        ])
        labels.append(1)  # attack
    return pd.DataFrame(flows, columns=FEATURES), np.array(labels)

# Generate dataset
X, y = generate_flows(1000)
print("Generated realistic dataset:", X.shape, y.shape)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RandomForest
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

print("Training accuracy:", clf.score(X_train, y_train))
print("Testing accuracy:", clf.score(X_test, y_test))

# Save model + feature names
joblib.dump((clf, FEATURES), "models/netguard_model.pkl")
print("✅ Model saved at models/netguard_model.pkl")
