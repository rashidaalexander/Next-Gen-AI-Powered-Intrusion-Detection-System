import scapy.all as scapy
import numpy as np
import joblib
from sklearn.ensemble import IsolationForest

# Load or train the anomaly detection model
def train_model():
    # Placeholder for training data (replace with real network traffic features)
    X_train = np.random.rand(100, 5)
    model = IsolationForest(contamination=0.05)
    model.fit(X_train)
    joblib.dump(model, "model.pkl")
    return model

try:
    model = joblib.load("model.pkl")
except:
    model = train_model()

def detect_intrusion(packet):
    # Extract features (for simplicity, using dummy data)
    features = np.random.rand(1, 5)
    prediction = model.predict(features)
    if prediction[0] == -1:
        print("[ALERT] Intrusion detected!")

print("[+] AI Intrusion Detection System Running...")
scapy.sniff(prn=detect_intrusion, store=False)
