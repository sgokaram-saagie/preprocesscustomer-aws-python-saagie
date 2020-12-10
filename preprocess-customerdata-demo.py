import csv,json, sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        inputfile = sys.argv[1]
    else:
        inputfile = "customer.csv"

    if len(sys.argv) > 2:
        outputfile = sys.argv[2]
    else:
        outputfile = "preprocess_customer.csv"

    print("Connecting to source system to fetch customer data")
    print("Found file "+inputfile)
    print("Fetching Data")
    print("Persisting data to Data Lake")
    print("Process complete. Exiting...")
    exit(0)
