import math


def generate_pwm_table(steps):
    pwm_table = []
    for i in range(steps):
        angle = (i / steps) * math.pi
        value = math.sin(angle) * 255
        int_value = round(value)
        pwm_table.append(int_value)
    return pwm_table

def save_header_file(fileName, steps):
    pwm_table = generate_pwm_table(steps)
    guard = f"{fileName.upper()}.H"

    with open(f"{fileName}.h", "wt") as headerFile :
        headerFile.write(f"#ifndef {guard}\n"
                         f"#define {guard}\n")

    
    with open(f"{fileName}.h", "a") as headerFile :

        headerFile.write(f"const char {fileName}_data[{steps}] = [")
        strToWrite = ""
        for i in range(steps) :
            if (i == (steps - 1)) :
                strToWrite = f"{pwm_table[i]}];\n"
            else :
                strToWrite = f"{pwm_table[i]},"
            
            headerFile.write(strToWrite)

        headerFile.write("#endif //PWM_TABLE.H")

if __name__ == "__main__" :
    save_header_file("pwm_table", 256)








