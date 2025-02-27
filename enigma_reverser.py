import sys 
import re

assert len(sys.argv) >= 2, "Missing arguments (format: python reverser.py input.enigma output.enigma)"
input_file = sys.argv[1]
output_file = sys.argv[2]
assert output_file != input_file, "output file cannot be the same as input file"

# Dictionary of datatypes. Keys are/will be the name of datatypes before applying the map, Values are/will be the name of the datatypes after applying the map 
class_mapping = {"I": "I", "Z": "Z", "C": "C", "F": "F", "D": "D", "B": "B", "S": "S", "J": "J", "V": "V"}

# Fills the class_mapping
with open(input_file) as input:
    for line in input:
        line_segments = line.strip().split()
        if not line_segments:
            continue

        if line_segments[0].lower() == 'class':
            class_mapping[line_segments[1]] = line_segments[2]


with open(input_file, "r") as input:
    with open(output_file, "w") as output:
        for line in input:
            line_segments = line.split()
            if not line_segments:
                output.write(line)
                continue

            match line_segments[0]:
                case 'CLASS': # Just swap names
                    line_segments[1], line_segments[2] = line_segments[2], line_segments[1]
                    output.write(" ".join(line_segments) + '\n')

                case 'FIELD':
                    line_segments[1], line_segments[2] = line_segments[2], line_segments[1]
                    if line_segments[3][-1] != ';': # return is primitive type, don't change a thing
                        output.write('\t' + " ".join(line_segments) + '\n')                        
                        continue
                    
                    start_of_datatype = line_segments[3].find('L')
                    datatype = line_segments[3][start_of_datatype + 1: -1]

                    if not class_mapping.get(datatype): # non primitive built-in type
                        output.write('\t' + " ".join(line_segments) + '\n')
                        continue

                    line_segments[3] = line_segments[3].replace(datatype, class_mapping[datatype])

                    output.write('\t' + " ".join(line_segments) + '\n')



                case 'METHOD':
                    line_segments[1], line_segments[2] = line_segments[2], line_segments[1]
                    right_parenthesis = line_segments[3].find(')')
                    if right_parenthesis > 1: # function requires arguments
                        # This swaps occurrences in the keys of class_mapping for the values of class_mapping
                        pattern = re.compile('|'.join(map(re.escape, class_mapping.keys())))
                        line_segments[3] = '(' + pattern.sub(lambda match: class_mapping[match.group()], line_segments[3][1:right_parenthesis]) + line_segments[3][right_parenthesis:]


                    right_parenthesis = line_segments[3].find(')')
                    return_type = line_segments[3][right_parenthesis + 1:]

                    if return_type.find(';') == -1 or not class_mapping.get(return_type[1:-1]): #primitive or non primitive built-in type
                        output.write('\t' + " ".join(line_segments) + '\n')
                        continue

                    line_segments[3] = line_segments[3][:right_parenthesis+1] + 'L' + class_mapping.get(return_type[1:-1]) + ';'
                    output.write('\t' + " ".join(line_segments) + '\n')


                case other:
                    output.write(line)