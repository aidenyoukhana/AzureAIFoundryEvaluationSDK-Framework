"""
Convert evaluation data to genai-evals GitHub Action format.

The genai-evals action expects a specific format with 'inputs', 'outputs', and 'description' fields.
"""

import json
import sys
from pathlib import Path


def convert_qa_data(line_data):
    """Convert QA data format"""
    return {
        "inputs": {
            "query": line_data.get("question", ""),
            "context": line_data.get("context", "")
        },
        "outputs": {
            "response": line_data.get("answer", "")
        },
        "description": {
            "context": {
                "system-prompt": "Answer questions based on the provided context"
            }
        }
    }


def convert_general_purpose_data(line_data):
    """Convert general purpose (fluency, coherence) data format"""
    return {
        "inputs": {
            "query": line_data.get("query", ""),
        },
        "outputs": {
            "response": line_data.get("response", "")
        },
        "description": {
            "context": {
                "system-prompt": "Provide clear and fluent responses"
            }
        }
    }


def convert_file(input_file, output_file, conversion_func):
    """Convert a JSONL file to the genai-evals format"""
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if line.strip():
                data = json.loads(line)
                converted_data = conversion_func(data)
                outfile.write(json.dumps(converted_data) + '\n')
    print(f"Converted {input_file} -> {output_file}")


def main():
    base_dir = Path(__file__).parent
    data_dir = base_dir / "data"
    
    # Create output directory
    output_dir = data_dir / "genai_evals_format"
    output_dir.mkdir(exist_ok=True)
    
    # Convert general purpose files
    general_purpose_dir = data_dir / "general_purpose"
    for file_name in ["fluency_data.jsonl", "coherence_data.jsonl"]:
        input_file = general_purpose_dir / file_name
        output_file = output_dir / file_name
        if input_file.exists():
            convert_file(input_file, output_file, convert_general_purpose_data)
    
    # Convert QA file
    qa_file = general_purpose_dir / "qa_data.jsonl"
    output_qa = output_dir / "qa_data.jsonl"
    if qa_file.exists():
        convert_file(qa_file, output_qa, convert_qa_data)
    
    print(f"\nAll files converted to {output_dir}")
    print("\nUpdate your workflow file to use these files:")
    print(f"GENAI_EVALS_DATA_PATH: ${{{{ github.workspace }}}}/data/genai_evals_format/${{{{ matrix.evaluator.data }}}}")


if __name__ == "__main__":
    main()
