import importlib.util

def import_variable(file_path, variable_name):
    spec = importlib.util.spec_from_file_location("module_name", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, variable_name)

if __name__ == "__main__":
    file_path = "variable_load_2.py"
    variable_name = "a"
    a_value = import_variable(file_path, variable_name)
    print(a_value)

