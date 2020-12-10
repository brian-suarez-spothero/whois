from ipwhois import IPWhois
import csv


#   Creates a Host class
class Host:
    def __init__(self,
                 asn_description):
        self.host_description = asn_description

    def __str__(self):
        return f"{self.host_description}"


#   Open a csv file
with open('/Users/Brian.Suarez/Downloads/gmail.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        obj = IPWhois(row[0])

        #   Perform an RDAP lookup of the IP address in the csv file
        results = obj.lookup_rdap(depth=1)
        some_Host = Host(results['asn_description'])

        #   Prints each IP in a row, with the ASN description next to it
        print(f"{row[0]} - {some_Host}")
