import pandas as pd
import numpy as np

# 1. Generate search performance data
np.random.seed(42)
n_samples = 1000

df = pd.DataFrame({
    'page_id': np.random.randint(100, 500, n_samples),
    'avg_position': np.random.uniform(1.0, 15.0, n_samples),
    'impressions': np.random.randint(500, 50000, n_samples),
})

# 2. Calculate expected vs actual CTR
df['expected_ctr'] = 1 / (df['avg_position'] + 1)
df['actual_ctr'] = df['expected_ctr'] * np.random.uniform(0.6, 1.2, n_samples)
df['actual_clicks'] = (df['actual_ctr'] * df['impressions']).astype(int)

# 3. Calculate CTR performance gap
df['ctr_gap'] = df['expected_ctr'] - df['actual_ctr']

# 4. Assign optimization actions
def assign_action(row):
    if row['avg_position'] <= 5 and row['ctr_gap'] > 0.02:
        return 'Rewrite Meta Title & Description'
    elif row['avg_position'] > 5 and row['ctr_gap'] > 0.02:
        return 'Refresh Content Depth'
    else:
        return 'Protect & Maintain'

df['action_tier'] = df.apply(assign_action, axis=1)

print("Analysis Complete!")
print(df['action_tier'].value_counts())
