
import pandas as pd

def deduplicate_contacts(dataset):
    df = pd.read_csv(dataset)
    df.drop_duplicates(inplace=True)
    df.to_csv(dataset, index=False)
