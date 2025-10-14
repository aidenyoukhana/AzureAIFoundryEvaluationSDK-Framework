import json
import sys

def format_jsonl_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    formatted_lines = []
    for line in lines:
        line = line.strip()
        if line:
            try:
                obj = json.loads(line)
                formatted = json.dumps(obj, indent=2)
                formatted_lines.append(formatted)
            except json.JSONDecodeError as e:
                print(f"Error parsing line: {line} - {e}")
                formatted_lines.append(line)  # Keep original if error
        else:
            formatted_lines.append('')

    with open(file_path, 'w') as f:
        for line in formatted_lines:
            f.write(line + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python format_jsonl.py <file_path>")
        sys.exit(1)
    format_jsonl_file(sys.argv[1])