import requests

def check_xss_vulnerability(url):
    payload = '<script>alert("XSS Vulnerability Found");</script>'

    # Mengirim permintaan GET dengan payload XSS
    response = requests.get(url + payload)

    # Memeriksa apakah payload XSS dieksekusi
    if payload in response.text:
        print("XSS Vulnerability Found!")
    else:
        print("No XSS Vulnerability Detected.")

# Meminta input dari pengguna untuk URL web yang akan diperiksa
url = input("Masukkan URL web untuk memeriksa bug XSS: ")
check_xss_vulnerability(url)
