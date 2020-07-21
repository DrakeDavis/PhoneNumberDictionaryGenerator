AreaCodeList = []
AllNumbersInAreaCode = []

# Read in list of US Area Codes
with open('./AreaCodes.txt') as areCodeFile:
    for line in areCodeFile:
        if not line.startswith('#') and not len(line.rstrip()) == 0:
            AreaCodeList.append(line.rstrip())

# US phone number format: (NXX) NXX-XXXX, where N is 2–9 and X is 0–9
# We define 'leadingDigit' to be between 2-9 as explained above
for areaCode in AreaCodeList:
    # Gotta clear this list for each area code, using one huge list leads to OutOfMemory exceptions (even with x64)
    AllNumbersInAreaCode.clear()
    for leadingDigit in range(2, 9):
        count = 0
        while count < 999999:
            AllNumbersInAreaCode.append(areaCode + str(leadingDigit) + str(count).zfill(6))
            count = count + 1
    # Using "a" to append each area code to the output file
    with open("ListOfUnitedStatesPhoneNumbers.txt", "a") as outfile:
        outfile.write("\n".join(AllNumbersInAreaCode))
        # If it's not the last area code, add a newline
        if not areaCode == AreaCodeList[-1]:
            outfile.write("\n")

