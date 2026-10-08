import pandas as pd, numpy as np
df = pd.read_csv("data/raw/shipments.csv")
perf = pd.read_csv("data/processed/carrier_perf.csv")
worst = perf.sort_values('otif').iloc[0]['carrier']
best = perf.sort_values('otif').iloc[-1]['carrier']
best_avg = perf[perf.carrier==best]['avg_lead'].values[0]
df_sim = df.copy()
df_sim.loc[df_sim.carrier==worst,'actual_lead_days'] = best_avg + np.random.normal(0,0.3,len(df_sim[df_sim.carrier==worst]))
df_sim['on_time_sim'] = df_sim['actual_lead_days']<=5
result = pd.DataFrame([{
  'scenario':f'Switch {worst} -> {best}',
  'otif_before':df['on_time'].mean()*100,
  'otif_after':df_sim['on_time_sim'].mean()*100,
  'cost_before':df['cost'].mean(),
  'cost_after':df['cost'].mean()*1.1
}])
result['otif_gain'] = result['otif_after']-result['otif_before']
result.to_csv("data/processed/what_if.csv", index=False)
print(result)
