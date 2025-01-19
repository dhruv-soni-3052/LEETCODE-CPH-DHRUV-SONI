import re
import importlib.util
import ast
import sys

def import_user_function(file_path, function_name):
    spec = importlib.util.spec_from_file_location(function_name, file_path)
    user_module = importlib.util.module_from_spec(spec)
    sys.modules[function_name] = user_module
    spec.loader.exec_module(user_module)
    return getattr(user_module, function_name)

def convert_value(value, data_type):
    try:
        value = value.strip()

        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return value.strip('"').strip("'")
        elif data_type == "bool":
            return value.lower() in ['true', '1', 't', 'y', 'yes']
        elif data_type in ["list", "tuple", "dict"]:
            return ast.literal_eval(value)
        else:
            return value
    except Exception as e:
        print(f"Error converting value: {value} to type: {data_type}. Exception: {e}")
        return None

def split_outside_brackets(line):
    return re.split(r',\s*(?![^\[]*\])', line)

def format_list_for_output(lst):
    if isinstance(lst, list):
        if len(lst) == 0:
            return "[]"
        return f'[{",".join(map(str, lst))}]'
    return str(lst)

def run_tests(input_file, output_file, my_output_file, function_name, data_types):
    solve_function = import_user_function('solution.py', function_name)

    with open(input_file, 'r') as f:
        inputs = f.readlines()

    with open(my_output_file, 'w') as f:
        for line in inputs:
            parts = split_outside_brackets(line)
            values = []
            for i, part in enumerate(parts):
                if "=" in part:
                    value = part.split("=")[1].strip() 
                    data_type = data_types[i] 
                    converted_value = convert_value(value, data_type) 
                    values.append(converted_value)
                else:
                    print(f"Malformed input line: {line}")
                    return

            result = solve_function(*values) 
            f.write(format_list_for_output(result) + '\n')

    with open(output_file, 'r') as f:
        expected_outputs = f.readlines()

    with open(my_output_file, 'r') as f:
        generated_outputs = f.readlines()

    all_passed = True
    for i, (expected, generated) in enumerate(zip(expected_outputs, generated_outputs), start=1):
        expected = expected.strip().strip('"').strip("'")
        generated = generated.strip().strip('"').strip("'")

        if expected != generated:
            print(f"Test case failed on line {i}: expected '{expected}' but found '{generated}'")
            all_passed = False

    if all_passed:
        print("All test cases passed!")

def main():
    function_name = "Solve"
    
    num_variables = int(input("Enter the number of input variables: "))
    data_types = []
    
    for i in range(num_variables):
        data_type = input(f"Enter the data type for variable {chr(120 + i)} (x, y, z, ...): ").strip()
        data_types.append(data_type)
    
    input_file = "input.txt"
    output_file = "output.txt"
    my_output_file = "myoutput.txt"
    
    run_tests(input_file, output_file, my_output_file, function_name, data_types)

if __name__ == "__main__":
    main()
