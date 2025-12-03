import pandas as pd
import numpy as np
import random

def generate_data(num_samples=1000):
    np.random.seed(42)
    random.seed(42)
    
    regions = ['North', 'South', 'East', 'West']
    vehicle_types = ['SUV', 'Sedan', 'Hatchback', 'EV', 'Luxury']
    genders = ['Male', 'Female']
    
    data = {
        'customer_id': range(1, num_samples + 1),
        'age': np.random.randint(18, 70, num_samples),
        'gender': np.random.choice(genders, num_samples),
        'annual_income': np.random.randint(25000, 150000, num_samples),
        'region': np.random.choice(regions, num_samples),
        'dealer_visit_count': np.random.randint(1, 10, num_samples),
        'purchase_probability': np.random.uniform(0.1, 1.0, num_samples).round(2)
    }
    
    df = pd.DataFrame(data)
    
    # Assign vehicle preference based on income and age logic (to make it realistic)
    def assign_vehicle(row):
        if row['annual_income'] > 100000:
            return np.random.choice(['Luxury', 'EV', 'SUV'], p=[0.5, 0.3, 0.2])
        elif row['annual_income'] > 60000:
            return np.random.choice(['SUV', 'Sedan', 'EV'], p=[0.4, 0.4, 0.2])
        else:
            return np.random.choice(['Hatchback', 'Sedan'], p=[0.7, 0.3])
            
    df['vehicle_preference'] = df.apply(assign_vehicle, axis=1)
    
    return df

if __name__ == "__main__":
    df = generate_data()
    df.to_csv('data.csv', index=False)
    print("Generated data.csv with 1000 samples.")
