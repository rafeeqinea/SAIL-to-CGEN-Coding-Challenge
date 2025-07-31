#importing necessary libraries
import yaml
import json

input_file = 'data.yaml'  # or 'data.json'

#detecting the file type and loading data
if input_file.endswith(".json"):
    file_type = "json"
    with open(input_file, 'r') as file:
        data = json.load(file)
elif input_file.endswith(".yaml") or input_file.endswith(".yml"):
    file_type = "yaml"
    with open(input_file, 'r') as file:
        data = yaml.safe_load(file)
else:
    raise ValueError("Unsupported file format. Please provide a .json or .yaml file.")

#converting the data to S-expression format
def to_s_expression(data, prefix):
    if isinstance(data, dict):  # key-value object
        result = []
        for key, value in data.items():
            child = to_s_expression(value, prefix=f"{prefix}:{key}")
            if isinstance(value, (dict, list)):
                result.append(f"({prefix}:{key} {child})")
            else:
                result.append(child)
        return ' '.join(result)

    elif isinstance(data, list):  # list of values
        result = []
        for item in data:
            expr = to_s_expression(item, prefix=f"{prefix}:item")
            result.append(expr)
        return ' '.join(result)

    elif isinstance(data, str):
        if prefix.endswith(":date") and "-" in data:
            parts = data.split("-")
            if len(parts) == 3 and all(p.isdigit() for p in parts):
                return f"({prefix} (make-date {int(parts[0])} {int(parts[1])} {int(parts[2])}))"
        escaped = data.replace('"', '\\"')
        return f'({prefix} "{escaped}")'

    elif isinstance(data, (int, float)):
        return f"({prefix} {data})"

    else:
        return f'({prefix} "{str(data)}")'

s_expr = f"({to_s_expression(data, prefix=file_type)})"

# Print result
print(s_expr)

# Save to file
with open("output.lisp", "w") as f:
    f.write(s_expr)
