import subprocess
import importlib


def install_module(module_name):
    """Install the module"""
    try:
        importlib.import_module(module_name)
    except ImportError:
        subprocess.check_call(["pip", "install", module_name])


def install_missing_modules(missing_modules):
    """Install missing modules"""
    for module_name in missing_modules:
        print(f"Installing module '{module_name}'...")
        install_module(module_name)


def get_missing_modules(output):
    """Parse the output to find missing modules"""
    missing_modules = []
    for line in output.splitlines():
        if "ModuleNotFoundError" in line:
            module_name = line.split("'")[1]
            missing_modules.append(module_name)
    return missing_modules


def main():
    """Check for required modules and install if necessary"""
    file_to_test = input("Enter the file to test: ")
    try:
        subprocess.check_output(["python3", file_to_test])
    except subprocess.CalledProcessError:
        try:
            output = subprocess.check_output(["python3", file_to_test],
                                             stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            assert False, f"An error occurred while running the file: {str(e)}"
        
        missing_modules = get_missing_modules(output)

        if missing_modules:
            print("Missing modules detected:", ", ".join(missing_modules))
            install_missing_modules(missing_modules)
            print("Modules installed successfully.")
        else:
            print("An error occurred while running the file.")
    except Exception as e:
        print("An error occurred while running the file:", str(e))
    return 0


if __name__ == "__main__":
    main()
