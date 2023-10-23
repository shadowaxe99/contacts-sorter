import pandas as pd

def unify_contacts(contacts):
    # Remove duplicate contacts
    contacts = contacts.drop_duplicates()

    # Merge contacts with the same name
    merged_contacts = contacts.groupby('Name').agg({
        'Phone': 'first',
        'Email': 'first',
        'Address': 'first'
    }).reset_index()

    return merged_contacts