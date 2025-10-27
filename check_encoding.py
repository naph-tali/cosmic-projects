import chardet
import sys

def check_encoding(filename):
    with open(filename, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result

if __name__ == "__main__":
    files_to_check = ['cosmic_evaluator.py', 'src/entropy_tools.py', 'src/resonant_engine.py']
    for file in files_to_check:
        try:
            encoding_info = check_encoding(file)
            print(f"{file}: {encoding_info['encoding']} (confidence: {encoding_info['confidence']:.2f})")
        except Exception as e:
            print(f"{file}: Error - {e}")
