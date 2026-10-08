import pandas as pd, os
os.makedirs("data/processed", exist_ok=True)
df = pd.read_csv("data/raw/shipments.csv")
print(f"OTIF {df['on_time'].mean()*100:.1f}% | Avg Lead {df['actual_lead_days'].mean():.2f}d")
carrier_perf = df.groupby('carrier').agg(otif=('on_time','mean'), avg_lead=('actual_lead_days','mean'), avg_cost=('cost','mean'), orders=('order_id','count')).reset_index()
carrier_perf['otif']*=100
carrier_perf.to_csv("data/processed/carrier_perf.csv", index=False)
print(carrier_perf.sort_values('otif', ascending=False))
