def load_config(config_file):
    import json
    with open(config_file, 'r') as file:
        return json.load(file)

def save_config(config_file, config_data):
    import json
    with open(config_file, 'w') as file:
        json.dump(config_data, file, indent=4)

def log_message(message, log_file='project.log'):
    with open(log_file, 'a') as file:
        file.write(f"{message}\n")

def validate_data(data, schema):
    from jsonschema import validate, ValidationError
    try:
        validate(instance=data, schema=schema)
        return True
    except ValidationError as e:
        log_message(f"Validation error: {e.message}")
        return False

def read_csv(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def write_csv(data, file_path):
    import pandas as pd
    data.to_csv(file_path, index=False)