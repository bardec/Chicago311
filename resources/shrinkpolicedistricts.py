import csv
from datetime import date
import string

with open('all_311_calls.csv', 'rb') as csvfile:
    call_reader = csv.DictReader(csvfile, delimiter=",")
    date_coll = dict()
    count = 0
    for row in call_reader:
        if row['Creation Date'] != "":
            start_date = row['Creation Date']
            start_year = start_date[0:4]
            start_month = start_date[5:7]
            if start_month[0] == "0":
                #   print start_month
                start_month = start_month[1]
            #print start_month
            start_day = start_date[8:10]
            end_date = row['Completion Date']
            end_year = end_date[6:10]
            end_month = end_date[0:2]
            if row['Status'] != 'Open' and row['Status'] != 'Open - Dup':
            #print row["Status"]
                if end_month[0] == "0":
                    end_month = end_month[1]
                end_day = end_date[3:5]
                average_response = (date(int(end_year), int(end_month), int(end_day)) - date(int(start_year), int(start_month), int(start_day))).days * 1.0
                police_district = row['Police District']
                if police_district in date_coll:
                    date_coll[police_district].append(average_response)
                else:
                    date_coll[police_district] = [average_response]
#count = count + 1
            
    
    average_response_times = dict()
    for police_district in date_coll:
        #print sum(date_coll[neighborhood].values())
        #print len(date_coll[neighborhood])
        #print len(date_coll[neighborhood].values())
        average = sum(date_coll[police_district])/len(date_coll[police_district])
        average_response_times[police_district] = average
    
    field_names = ['Police District', 'Average Response Time']
    with open('summarized_police_district.csv', 'w') as outfile:
        writer = csv.DictWriter(outfile, fieldnames = field_names)
        writer.writeheader()
        for police_district in average_response_times:
            writer.writerow({'Police District': police_district, 'Average Response Time': average_response_times[police_district]})
                            

