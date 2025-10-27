#  ENCODING PROTECTION SYSTEM
# Prevent UTF-8 BOM issues in future file operations

import os
import sys

class EncodingGuard:
    """Protect against BOM and encoding issues"""
    
    def __init__(self):
        self.safe_encoding = 'utf-8'
    
    def safe_write_file(self, file_path, content):
        """Safely write file without BOM"""
        try:
            with open(file_path, 'w', encoding=self.safe_encoding, newline='') as f:
                f.write(content)
            print(f"  Safely wrote: {file_path}")
            return True
        except Exception as e:
            print(f" Error writing {file_path}: {e}")
            return False
    
    def safe_read_file(self, file_path):
        """Safely read file, handling BOM if present"""
        try:
            with open(file_path, 'rb') as f:
                content_bytes = f.read()
            
            # Remove BOM if present
            if content_bytes.startswith(b'\xef\xbb\xbf'):
                content_bytes = content_bytes[3:]
            
            return content_bytes.decode(self.safe_encoding)
        except Exception as e:
            print(f" Error reading {file_path}: {e}")
            return None
    
    def check_file_encoding(self, file_path):
        """Check if file has BOM or encoding issues"""
        try:
            with open(file_path, 'rb') as f:
                first_bytes = f.read(3)
            
            has_bom = first_bytes.startswith(b'\xef\xbb\xbf')
            
            # Try to decode as UTF-8
            with open(file_path, 'r', encoding='utf-8') as f:
                f.read()
            can_decode = True
            
            return {
                'has_bom': has_bom,
                'can_decode': can_decode,
                'status': 'CLEAN' if not has_bom and can_decode else 'ISSUES'
            }
        except Exception as e:
            return {
                'has_bom': False,
                'can_decode': False,
                'status': 'ERROR',
                'error': str(e)
            }
    
    def scan_project_encoding(self):
        """Scan entire project for encoding issues"""
        python_files = []
        
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith('.py'):
                    full_path = os.path.join(root, file)
                    python_files.append(full_path)
        
        print("  SCANNING PROJECT ENCODING...")
        print("=" * 50)
        
        issues_found = 0
        for file_path in python_files:
            result = self.check_file_encoding(file_path)
            if result['status'] != 'CLEAN':
                print(f"  {file_path}: {result['status']}")
                if result.get('error'):
                    print(f"     Error: {result['error']}")
                issues_found += 1
        
        if issues_found == 0:
            print(" ALL FILES HAVE CLEAN ENCODING!")
        else:
            print(f"  Found {issues_found} files with encoding issues")
        
        return issues_found

# Create global encoding guard instance
encoding_guard = EncodingGuard()

print("  Encoding Protection System activated!")
