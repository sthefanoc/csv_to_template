from pandas import read_csv
import sys
import os

source_df = read_csv('source.csv', ";")

if len(sys.argv) < 2:
    ref_to_template = source_df.columns[0]
else:
    if sys.argv[1] not in sys.argv:
        raise NameError("Invalid argument. Column doen't exist on .csv file")
    ref_to_template = sys.argv[1]

for i, n in enumerate(sys.argv):
    print(i, n)


def find_all_variables(template):
    variables = []
    while True:
        start = template.find('{')
        end = template.find('}')
        if start == -1 or end == -1:
            break
        variable_name = template[start+1:end]
        variables.append(variable_name)
        template = template[end+1:]

    return variables


template_list = os.listdir(os.path.join(os.getcwd(), 'templates'))

for file in template_list:
    if file[-3:].lower() != 'txt':
        raise NameError(
            "One or more files in the templates folder is not a .txt file.")

if __name__ == '__main__':
    for file in template_list:
        for i in range(len(source_df)):
            with open(os.path.join(os.getcwd(), 'templates', file)) as f:
                template = f.read()

            variables_inside_template = find_all_variables(template)

            for variable in variables_inside_template:
                if variable not in source_df.columns:
                    raise NameError(
                        f'The variable {variable} on the {file} was not found as a reference on the .csv file')
                else:
                    variable_to_be_replaced = '{' + variable + '}'
                    template = template.replace(
                        f'{variable_to_be_replaced}', str(source_df.loc[i, variable]))
            print(template)
            final_name = ''.join(file.split(
                '.')[:-1]) + '_' + source_df.loc[i, ref_to_template] + '.txt'
            with open(os.path.join(os.getcwd(), 'output', final_name), 'w') as final:
                final.write(template)
