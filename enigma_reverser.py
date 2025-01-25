import sys 

assert len(sys.argv) >= 2, "Missing arguments (format: python reverser.py input.enigma output.enigma)"
input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, "r") as input:
    with open(output_file, "w") as output:
        for line in input:
            if len(line) < 2 or not line.lstrip():
                output.write(line)
                continue 
            
            if line.lstrip()[0] == '#': # Comment character in enigma
                output.write(line)
                continue

            output_line = line.rstrip().split(' ')
            output_line[1], output_line[2] = output_line[2], output_line[1] 
            output.write(" ".join(output_line)+'\n')