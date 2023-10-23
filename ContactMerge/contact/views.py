
from django.shortcuts import render
from django.http import HttpResponse
import csv

def merge_contacts(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        reader = csv.reader(csv_file)
        contacts = []
        for row in reader:
            contacts.append(row)
        
        # Logic to merge duplicate contacts
        
        merged_contacts = merge_duplicates(contacts)
        
        # Save merged contacts to a new CSV file
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="merged_contacts.csv"'
        
        writer = csv.writer(response)
        for contact in merged_contacts:
            writer.writerow(contact)
        
        return response
    
    return render(request, 'contact/merge.html')

