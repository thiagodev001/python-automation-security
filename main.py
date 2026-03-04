from zipfile import ZipFile

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password.encode("utf-8"))
        return True
    except:
        return False

def main():
    print("[+] Beginning bruteforce ")
    with ZipFile('enc.zip') as zf:
        with open('rockyou.txt', 'r', encoding="utf-8", errors="ignore") as f:
            for line in f:
                pwd = line.strip()  # senha como string
                if attempt_extract(zf, pwd):
                    print(f"[+] Password found: {pwd}")
                    return
    print("[+] Password not found in list")

if __name__ == "__main__":
    main()
