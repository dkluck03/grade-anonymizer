NUID_dict = dict()
csvfile = open('NUID.csv', 'r')
for row in csvfile:
    items = row.split(',')
    NUID_dict[items[0]] = items[1].strip()
csvfile.close()

try:
    grade_file = open('gradefile.txt', 'r')
    anonymized_file = open('anonymized_grades.csv', 'w')
    is_first = True
    output = list()
    for row in grade_file:
        items = row.split('\t')
        string_line = ''
        if is_first:
            is_first = False
            string_line += f'NUID,'
            for checkpoint in items[1:]:
                string_line += f'{checkpoint.strip()},'
        else:
            string_line += f'{NUID_dict[items[0]]},'
            for grade in items[1:]:
                if grade.strip() == 'TRUE':
                    string_line += 'Y,'
                else:
                    string_line += 'N,'
        string_line += '\n'
        output.append(string_line)
    
    output[1:].sort()
    for line in output:
        anonymized_file.write(line)
    print('Success')
except KeyError as e:
    print(f'Key Error: {e}')
finally:           
    grade_file.close()
    anonymized_file.close()

    
    
