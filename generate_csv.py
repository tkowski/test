import csv

def generate_empty_csv(output_path):
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        # Nie dodajemy żadnych danych, pozostawiamy pusty plik
        pass
