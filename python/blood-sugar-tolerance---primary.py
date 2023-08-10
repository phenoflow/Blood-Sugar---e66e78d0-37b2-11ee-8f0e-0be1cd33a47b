# Tim Doran, Evangelos Kontopantelis, Jose M Valderas, Stephen Campbell, Martin Roland, Chris Salisbury, David Reeves, 2023.

import sys, csv, re

codes = [{"code":"44V..00","system":"readv2"},{"code":"44V..11","system":"readv2"},{"code":"44V..12","system":"readv2"},{"code":"44V6.00","system":"readv2"},{"code":"44VZ.00","system":"readv2"},{"code":"7P17200","system":"readv2"},{"code":"R102.12","system":"readv2"},{"code":"L3300","system":"oxmis"},{"code":"L3300NM","system":"oxmis"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('blood-sugar-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["blood-sugar-tolerance---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["blood-sugar-tolerance---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["blood-sugar-tolerance---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
