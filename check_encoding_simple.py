import sys

def check_file_encoding(filename):
    """Check if a file has BOM using pure Python"""
    try:
        with open(filename, 'rb') as f:
            raw = f.read(4)  # Read first 4 bytes to check for BOM
            
        # Common BOM signatures
        bom_signatures = {
            b'\xff\xfe': 'UTF-16 LE',
            b'\xfe\xff': 'UTF-16 BE', 
            b'\xef\xbb\xbf': 'UTF-8 BOM',
            b'\xff\xfe\x00\x00': 'UTF-32 LE',
            b'\x00\x00\xfe\xff': 'UTF-32 BE'
        }
        
        for bom, encoding in bom_signatures.items():
            if raw.startswith(bom):
                return encoding
                
        # No BOM detected, assume UTF-8 or other
        return 'No BOM detected (likely UTF-8 without BOM)'
        
    except Exception as e:
        return f'Error: {e}'

# Check our files
files_to_check = ['cosmic_evaluator.py', 'src/entropy_tools.py', 'src/resonant_engine.py', 'enhanced_cosmic.py']

print("🔍 CHECKING FILE ENCODINGS:")
print("=" * 40)
for file in files_to_check:
    try:
        encoding = check_file_encoding(file)
        print(f"{file}: {encoding}")
    except Exception as e:
        print(f"{file}: Cannot check - {e}")
