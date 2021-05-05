import csv
 
results = []
with open('C:\\scripts\\python\\executables.csv') as File:
    reader = csv.DictReader(File)
    for row in reader:
        results.append(row)
    myData = [{k:v for k,v in d.items() if k in ['File name', 'Folder','Owner']} for d in results ]
    

with open('C:\\scripts\\python\\executables_output.csv', 'w', newline='') as csvfile:
    fieldnames = ['File name', 'Folder', 'Owner']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    writer.writerows(myData)
    
 
print("Writing complete")