records = []
record = {}
record["name"] = "Rusakov"
record["age"] = 37
record["lecture"] = "Python Way"
records.append(record)
record = {}
record["name"] = "Gorin"
record["age"] = 37
record["lecture"] = "C++ Way"
records.append(record)
print(records)
for record in records:
    for key, value in record.items():
        if key == "Gorin":
            record["lecture"] = "Love assembler"
        print(f"{key} - {value} \t")
    print("\n")
