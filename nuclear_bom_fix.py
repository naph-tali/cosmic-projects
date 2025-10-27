#  NUCLEAR BOM REMOVAL - ABSOLUTE FIX
import os
import glob

def nuclear_bom_removal():
    print(" DEPLOYING NUCLEAR BOM REMOVAL...")
    
    # Get ALL Python files recursively
    python_files = glob.glob('**/*.py', recursive=True)
    
    fixed_count = 0
    for file_path in python_files:
        try:
            # Read file in binary mode
            with open(file_path, 'rb') as f:
                content = f.read()
            
            # Check for BOM and remove it
            if content.startswith(b'\xef\xbb\xbf'):
                print(f" Removing BOM from: {file_path}")
                with open(file_path, 'wb') as f:
                    f.write(content[3:])
                fixed_count += 1
            else:
                # Also fix any file that might have encoding issues
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        test_content = f.read()
                    # If we get here, file is readable, rewrite it cleanly
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(test_content)
                except:
                    # File has other encoding issues, try to recover
                    print(f"  Encoding issues in: {file_path}")
                    
        except Exception as e:
            print(f" Error processing {file_path}: {e}")
    
    print(f" NUCLEAR FIX COMPLETE: Fixed {fixed_count} files")
    return fixed_count

if __name__ == "__main__":
    nuclear_bom_removal()
