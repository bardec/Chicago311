import csv

with open('all_311_calls.csv', 'rb') as csvfile:
    call_reader = csv.DictReader(csvfile, delimiter=",")
    ssa_coll = dict()
    for row in call_reader:
        ssa = row['SSA']
        request_type = row['Type of Service Request']
        ssa_coll[ssa] = ssa_coll.get(ssa,dict())
        ssa_coll[ssa][request_type] = ssa_coll[ssa].get(request_type,0) + 1

    percentages = dict()
    # SSA, Abandoned Vehicle Complaint, %
    # SSA, Light Out Complaint, %
    for ssa in ssa_coll:
        total_num = sum(ssa_coll[ssa].values())
        percentages[ssa] = dict()
        for request_type in ssa_coll[ssa]:
            percentages[ssa][request_type] = ssa_coll[ssa][request_type]/(total_num*1.0)

    field_names = ['SSA','Type of Service Request','Percentage of Total']
    with open('summarized_311_calls.csv', 'w') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=field_names)
        writer.writeheader()
        for ssa in percentages:
            for request_type in percentages[ssa]:
                writer.writerow({'SSA': ssa, 'Type of Service Request':request_type, 'Percentage of Total': percentages[ssa][request_type]})

