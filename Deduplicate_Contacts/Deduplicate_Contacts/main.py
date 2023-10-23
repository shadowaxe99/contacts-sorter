
import pandas as pd
from utils.deduplicate import remove_duplicates

def main():
    # Read the dataset
    df = pd.read_csv("contacts.csv")

    # Remove duplicate rows
    deduplicated_df = remove_duplicates(df)

    # Save the deduplicated dataset
    deduplicated_df.to_csv("deduplicated_contacts.csv", index=False)

if __name__ == "__main__":
    main()
