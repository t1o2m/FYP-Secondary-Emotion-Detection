import csv
#annotation categories
annotation_list = ['suffering', 'sadness', 'disappointment',
               'shame', 'neglect', 'sympathy', 'unclassifiable']

print("Input file path...")
input_file = input()

read_data = []
#Reading data from .csv file
with open(input_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for row in csv_reader:
        read_data.append(row)
        line_count+=1
    
    print(f'Processed {line_count} lines.')

# Annotating list of data using user input
for row in read_data:        
    print(row)
    choice = 0

    while 0 >= choice or len(annotation_list) < choice or choice == 9 or choice == 7:
            try:
                choice = int(input('Select annotation 0. Suffering, 1. Sadness,\n 2. Dissapointment, 3. Shame,\n 4. Neglect, 5. Sympathy,\n 6. Unclassifiable, del. Remove data point \n exit to exit \n'))
                if choice == 9:
                    break

                elif choice == 7:
                    read_data.remove(row)
                    break

                elif choice <= 0 or choice >= len(annotation_list):
                    print("Please input a value between 0 and", len(annotation_list))
                
                else:
                    row.append( " " +annotation_list[choice])
            
            except ValueError:
                print("Please enter a value between 0-6")
           
            line_count += 1
    
    if choice == 9:
        break
#writing to annotated data to .csv file

with open("output_data.csv", "w", newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    line_count = 0

    for row in read_data:
        writer.writerow(row)
        line_count += 1

print(line_count)
