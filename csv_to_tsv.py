import csv

def convert_train(csv_file,tsv_file):
  f = open(csv_file, 'r')
  out_csv = open(tsv_file, 'w+')
  in_reader= csv.reader(f, delimiter = ',')
  with open(tsv_file, 'w') as out_tsv:
    out_writer = csv.writer(out_tsv,delimiter = '\t',lineterminator='\n')
    for row in in_reader:
      out_writer.writerow([row[0],row[1],row[2]])

convert_train('test.csv','test.tsv')
