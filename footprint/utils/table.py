
def buildTable(tabularData):
    types = []
    for _ in tabularData:
        types.append(_[0])
    type = (len(max(types, key=len))+2)*"-"
    values = []
    for _ in tabularData:
        values.append(_[1])
    value = (len(max(values, key=len))+2)*"-"
    print(f"+{type}+{value}+")
    for _ in tabularData:
        spacing = (len(type)-len(_[0])-2)*" "
        trailingSpace = (len(value)-len(_[1])-2)*" "
        print(f"| {_[0]}{spacing} | {_[1]}{trailingSpace} |")
    print(f"+{type}+{value}+")

if __name__ == "__main__":
    tabularData = [
        ["Type", "Value"],
        ["SomeTypeName", "SomeValueData"],
        ["SomeTypeNameData", "SomeValueData"],
        ["SomeLongTypeNameData", "SomeValueData"],
        ["ShortName", "SomeLongValueData"],
    ]
    buildTable(tabularData)