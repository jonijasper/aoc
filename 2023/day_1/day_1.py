
def recover_calibration_value_part1(document_filepath):
    with open(document_filepath,'r') as f:
        calibration_document = f.read().split()
    
    # print(calibration_document)
    total_sum = 0
    for line in calibration_document:
        # find first digit
        for char in line:
            if char.isnumeric():
                calibration_value = char
                break
        
        # find last digit
        for char in line[::-1]:
            if char.isnumeric():
                calibration_value += char
                break

        total_sum += int(calibration_value)

    print(total_sum)


def recover_calibration_value_part2(document_filepath):
    with open(document_filepath,'r') as f:
        calibration_document = f.read().split()
    
    # print(calibration_document)

    total_sum = 0
    for line in calibration_document:
        # find first digit
        for i,char in enumerate(line):
            if char.isnumeric():
                calibration_value = char
                break

            elif line[i:i+3] == "one":
                calibration_value = "1"
                break
            
            elif line[i:i+3] == "two":
                calibration_value = "2"
                break

            elif line[i:i+5] == "three":
                calibration_value = "3"
                break

            elif line[i:i+4] == "four":
                calibration_value = "4"
                break

            elif line[i:i+4] == "five":
                calibration_value = "5"
                break

            elif line[i:i+3] == "six":
                calibration_value = "6"
                break

            elif line[i:i+5] == "seven":
                calibration_value = "7"
                break

            elif line[i:i+5] == "eight":
                calibration_value = "8"
                break

            elif line[i:i+4] == "nine":
                calibration_value = "9"
                break
        
        # find last digit
        for i,char in enumerate(line[::-1]):
            if char.isnumeric():
                calibration_value += char
                break

            elif line[::-1][i:i+3] == "eno":
                calibration_value += "1"
                break
            
            elif line[::-1][i:i+3] == "owt":
                calibration_value += "2"
                break

            elif line[::-1][i:i+5] == "eerht":
                calibration_value += "3"
                break

            elif line[::-1][i:i+4] == "ruof":
                calibration_value += "4"
                break

            elif line[::-1][i:i+4] == "evif":
                calibration_value += "5"
                break

            elif line[::-1][i:i+3] == "xis":
                calibration_value += "6"
                break

            elif line[::-1][i:i+5] == "neves":
                calibration_value += "7"
                break

            elif line[::-1][i:i+5] == "thgie":
                calibration_value += "8"
                break

            elif line[::-1][i:i+4] == "enin":
                calibration_value += "9"
                break

        total_sum += int(calibration_value)

    print(total_sum)

if __name__=="__main__":
    recover_calibration_value_part2("day_1/day_1_input.dat")