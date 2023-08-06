# Learning LogScale

---

### Key Definitions:

- **Primary Key (PK):** A unique identifier for a record in a table. No two records can have the same primary key value.
- **Foreign Key (FK):** A field (or collection of fields) in one table that refers to the primary key in another table. It establishes a relationship between the two tables.

---

This table provides a clear overview of the primary and foreign keys in the data model, along with their descriptions and relationships.


### Keys in the Data Model:

| Table Name             | Key Type | Field Name       | Description                                           | Refers To (If FK)          |
|------------------------|----------|------------------|-------------------------------------------------------|----------------------------|
| MV-Collisions - Crash  | PK       | `collision_id`   | Unique record code generated by the system.           | N/A                        |
| MV-Collisions - Vehicle| PK       | `veh_unique_id`  | Unique record code generated by the system for each vehicle. | N/A                    |
| MV-Collisions - Vehicle| FK       | `veh_collision_id`| Unique crash identification code.                     | `collision_id` in Crash    |
| MV-Collisions - Person | PK       | `vic_unique_id`  | Unique record code generated by the system for each person/victim. | N/A          |
| MV-Collisions - Person | FK       | `vic_collision_id`| Unique crash identification code.                     | `collision_id` in Crash    |
| MV-Collisions - Person | FK       | `vic_vehicle_id` | Unique vehicle record associated with the victim.     | `veh_unique_id` in Vehicle |

---

These code blocks provide the naming convention used to rename and link the features in the tables together.
```python
### Rename Keys from the Original Data

# Import necessary libraries
import pandas as pd
import numpy as np

# Load the data
persons_url = "URL_TO_PERSONS_DATA"
vehicles_url = "URL_TO_VEHICLES_DATA"

persons_df = pd.read_csv(persons_url)
vehicles_df = pd.read_csv(vehicles_url)

# Data exploration
print("Persons Data Overview:")
print(persons_df.head())
print(persons_df.info())

print("\nVehicles Data Overview:")
print(vehicles_df.head())
print(vehicles_df.info())

# Rename columns based on the naming convention
persons_df.rename(columns={
    'UNIQUE_ID': 'vic_id',
    'COLLISION_ID': 'collision_id',
    'CRASH_DATE': 'acc_date',
    'CRASH_TIME': 'acc_time',
    'VICTIM_ID': 'vic_victim_id',
    'VICTIM_TYPE': 'vic_type',
    'VICTIM_INJURY': 'vic_injury',
    'VEHICLE_ID': 'veh_id',
    'VICTIM_AGE': 'vic_age',
    'EJECTION': 'vic_ejection',
    'EMOTIONAL_STATUS': 'vic_emotional_status',
    'BODILY_INJURY': 'vic_bodily_injury',
    'POSITION_IN_VEHICLE': 'vic_position',
    'SAFETY_EQUIPMENT': 'vic_safety_equipment',
    'PED_LOCATION': 'ped_location',
    'PED_ACTION': 'ped_action',
    'COMPLAINT': 'vic_complaint',
    'VICTIM_ROLE': 'vic_role',
    'CONTRIBUTING _FACTOR_1': 'vic_contrib_factor_1',
    'CONTRIBUTING_FACTOR_2': 'vic_contrib_factor_2',
    'VICTIM_SEX': 'vic_sex'
}, inplace=True)

vehicles_df.rename(columns={
    'UNIQUE_ID': 'veh_unique_id',
    'COLLISION_ID': 'collision_id',
    'CRASH_DATE': 'acc_date',
    'CRASH_TIME': 'acc_time',
    'VEHICLE_ID': 'veh_id',
    'STATE_REGISTRATION': 'veh_state_reg',
    'VEHICLE_TYPE': 'veh_type',
    'VEHICLE_MAKE': 'veh_make',
    'VEHICLE_MODEL': 'veh_model',
    'VEHICLE_YEAR': 'veh_year',
    'TRAVEL_DIRECTION': 'veh_travel_dir',
    'VEHICLE_OCCUPANTS': 'veh_occupants',
    'DRIVER_SEX': 'driver_sex',
    'DRIVER_LICENSE_STATUS': 'driver_license_status',
    'DRIVER_LICENSE_JURISDICTION': 'driver_license_jurisdiction',
    'PRE_ACDNT_ACTION': 'pre_acc_action',
    'POINT_OF_IMPACT': 'point_of_impact',
    'VEHICLE_DAMAGE': 'veh_damage',
    'VEHICLE_DAMAGE_1': 'veh_damage_1',
    'VEHICLE_DAMAGE_2': 'veh_damage_2',
    'VEHICLE_DAMAGE_3': 'veh_damage_3',
    'PUBLIC_PROPERTY_DAMAGE': 'public_prop_damage',
    'PUBLIC_PROPERTY_DAMAGE_TYPE': 'public_prop_damage_type',
    'CONTRIBUTING_FACTOR_1': 'veh_contrib_factor_1',
    'CONTRIBUTING_FACTOR_2': 'veh_contrib_factor_2'
}, inplace=True)

# Combine date and time columns and parse into datetime
persons_df['datetime'] = pd.to_datetime(persons_df['acc_date'] + ' ' + persons_df['acc_time'])
vehicles_df['datetime'] = pd.to_datetime(vehicles_df['acc_date'] + ' ' + vehicles_df['acc_time'])

# Drop the original date and time columns
persons_df.drop(['acc_date', 'acc_time'], axis=1, inplace=True)
vehicles_df.drop(['acc_date', 'acc_time'], axis=1, inplace=True)

# Data Cleaning
# Handle missing values
persons_df.fillna("Unknown", inplace=True)
vehicles_df.fillna("Unknown", inplace=True)

# Data Enrichment
# Extracting the day of the week from the datetime column
persons_df['day_of_week'] = persons_df['datetime'].dt.day_name()
vehicles_df['day_of_week'] = vehicles_df['datetime'].dt.day_name()

# Save processed data
persons_df.to_csv("processed_persons.csv", index=False)
vehicles_df.to_csv("processed_vehicles.csv", index=False)

print("Data processing completed and saved to processed CSV files.")
```

## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## Disclaimer

Please note that these notes and files are for educational purposes only. Make sure to comply with all data privacy regulations and policies when using real data.
