# helper.py

def validate_non_empty(input_str, field_name):
    """
    Validate that input_str is not empty or just whitespace.
    Prints an error message if invalid.
    """
    if not input_str.strip():
        print(f"\033[31m{field_name} cannot be empty.\033[0m")
        return False
    return True


def confirm_action(prompt="Are you sure? (y/n): "):
    """
    Prompt the user for a yes/no confirmation.
    Returns True if user confirms with 'y' or 'Y'.
    """
    answer = input(prompt).strip().lower()
    return answer == 'y'


def print_list(items, header="Items"):
    """
    Nicely print a numbered list of items.
    """
    if not items:
        print(f"\033[31mNo {header.lower()} found.\033[0m")
        return
    print(f"\033[32m{header}:\033[0m")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")


def format_float(value, decimals=2):
    """
    Format a float to a string with given decimal places.
    """
    try:
        return f"{float(value):.{decimals}f}"
    except (ValueError, TypeError):
        return "N/A"
