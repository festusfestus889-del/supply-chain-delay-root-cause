import pandas as pd, numpy as np, os, random
os.makedirs("data/raw", exist_ok=True)
np.random.seed(42)
carriers = ["DHL","GIG Logistics","UPS","KOS","ABC Cargo"]
warehouses = ["PH","Lagos","Abuja"]
rows=[]
for i in range(5000):
  carrier = np.random.choice(carriers, p=[0.3,0.25,0.2,0.15,0.1])
  wh = random.choice(warehouses)
  base = {"DHL":3,"GIG Logistics":4,"UPS":3.5,"KOS":6,"ABC Cargo":5}[carrier] + (1 if wh=="PH" else 0)
  delay = 0
  is_rainy = random.random()<0.2
  is_weekend = random.random()<0.3
  dist = np.random.normal(400,100)
  if carrier in ["KOS","ABC Cargo"]: delay+=np.random.exponential(1.5)
  if is_rainy: delay+=np.random.exponential(1)
  if is_weekend: delay+=0.8
  actual = base + delay + np.random.normal(0,0.5)
  rows.append({
    "order_id": f"ORD_{i}","carrier":carrier,"warehouse":wh,
    "distance_km":int(dist),"is_rainy":is_rainy,"is_weekend":is_weekend,
    "actual_lead_days":round(actual,2),"on_time":actual<=5,"cost":int(dist*0.8 + (100 if carrier=="DHL" else 0))
  })
pd.DataFrame(rows).to_csv("data/raw/shipments.csv", index=False)
print(f"Done. OTIF {pd.DataFrame(rows)['on_time'].mean()*100:.1f}%")
