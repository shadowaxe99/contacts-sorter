import pandas as pd
from utils.unification import unify_contacts

def main():
    # Read the contacts data from CSV file
    contacts = pd.read_csv('contacts.csv')

    # Perform contact unification
    unified_contacts = unify_contacts(contacts)

    # Save the unified contacts to a new CSV file
    unified_contacts.to_csv('unified_contacts.csv', index=False)

if __name__ == "__main__":
    main()