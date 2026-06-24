# ==========================================
# DEVELOPER: Keshav Kumar Jha
# DATE: June 2026
# PROJECT: Custom Security Input Validation Gate
# ==========================================
import re

def analyze_password(password):
    print(f"\n[KESHAV-SEC-AUDIT] Scanning password payload: '{password}'")
    
    if len(password) < 8:
        print("[-] Security Alert: Input length falls below the 8-character threshold.")
        return False
        
    if not re.search("[a-z]", password) or not re.search("[A-Z]", password):
        print("[-] Security Alert: Missing critical mixed-case complexity.")
        return False
    if not re.search("[0-9]", password):
        print("[-] Security Alert: Missing numerical identifier.")
        return False
    if not re.search("[_@$!%*#?&]", password):
        print("[-] Security Alert: Missing special cryptographic character.")
        return False
        
    print("[+] Status: Authentication parameter verification successful!")
    return True

# Running custom test asset
test_input = "Keshav@IITK2026"
analyze_password(test_input)
