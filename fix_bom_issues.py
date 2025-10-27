#  UTF-8 BOM REMOVAL SCRIPT
# Remove Byte Order Mark from all Python files

import os
import sys

def remove_bom_from_file(file_path):
    """Remove UTF-8 BOM from a file"""
    try:
        # Read file with binary mode to detect BOM
        with open(file_path, 'rb') as f:
            content_bytes = f.read()
        
        # Check for UTF-8 BOM (EF BB BF)
        if content_bytes.startswith(b'\xef\xbb\xbf'):
            print(f" Removing BOM from: {file_path}")
            # Rewrite file without BOM
            with open(file_path, 'wb') as f:
                f.write(content_bytes[3:])  # Skip first 3 bytes (BOM)
            return True
        else:
            return False
            
    except Exception as e:
        print(f" Error processing {file_path}: {e}")
        return False

def fix_all_bom_issues():
    """Fix BOM issues in all Python files"""
    python_files = []
    
    # Find all Python files
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py'):
                full_path = os.path.join(root, file)
                python_files.append(full_path)
    
    print(" SCANNING FOR UTF-8 BOM ISSUES...")
    print("=" * 60)
    
    fixed_count = 0
    total_count = len(python_files)
    
    for file_path in python_files:
        if remove_bom_from_file(file_path):
            fixed_count += 1
    
    print("\\n" + "=" * 60)
    print(f"📊 FIXED {fixed_count} OUT OF {total_count} FILES")
    
    if fixed_count > 0:
        print("✅ BOM ISSUES RESOLVED!")
        print("�� Running syntax validation again...")
        
        # Re-run syntax validation
        import validate_syntax
        validate_syntax.validate_all_files()
    else:
        print("✅ NO BOM ISSUES FOUND")
    
    return fixed_count

if __name__ == "__main__":
    fixed = fix_all_bom_issues()
    sys.exit(0 if fixed == 0 else 1)
