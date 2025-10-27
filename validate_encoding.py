#!/usr/bin/env python3
"""
 PERMANENT ENCODING VALIDATION SYSTEM
Validates ALL Python files for syntax and encoding issues
"""

import ast
import sys
import os
import glob

def validate_file(filepath):
    """Validate a single Python file for syntax and encoding"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            source_code = f.read()
        
        # Try to parse the AST
        ast.parse(source_code, filename=filepath)
        return True, "PASS"
        
    except SyntaxError as e:
        return False, f"Syntax error: {e.msg} ({e.filename}, line {e.lineno})"
    except UnicodeDecodeError as e:
        return False, f"Encoding error: {e}"
    except Exception as e:
        return False, f"Unexpected error: {e}"

def validate_all_files():
    """Validate all Python files in the project"""
    print("  VALIDATING ALL PYTHON FILES...")
    print("=" * 60)
    
    python_files = glob.glob('**/*.py', recursive=True)
    total_files = len(python_files)
    passed_files = 0
    failed_files = []
    
    for filepath in python_files:
        is_valid, message = validate_file(filepath)
        status = "PASS" if is_valid else "FAIL"
        print(f"{status}: {filepath}")
        
        if is_valid:
            passed_files += 1
        else:
            failed_files.append((filepath, message))
            print(f"      {message}")
    
    print("=" * 60)
    print(f" RESULTS: {passed_files}/{total_files} files passed")
    
    if failed_files:
        print("❌ FAILED FILES:")
        for filepath, message in failed_files:
            print(f"   {filepath}: {message}")
        return False
    else:
        print("✅ ALL FILES VALIDATED SUCCESSFULLY!")
        return True

if __name__ == "__main__":
    success = validate_all_files()
    sys.exit(0 if success else 1)
