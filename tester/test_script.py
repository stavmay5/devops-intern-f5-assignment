import requests
import sys


def test_servers():
    try:
        response8080 = requests.get("http://nginx-server:8080")

        if response8080.status_code == 200:
            print("Server 8080 is running, status code 200 OK")
        else:
            print("Server 8080 isn't running, returned status code:", response8080.status_code)
            sys.exit(1)

    except Exception as e:
        print("Error connecting to server 8080:", e)
        sys.exit(1)


    try:
        response8081 = requests.get("http://nginx-server:8081")

        if response8081.status_code == 500:
            print("Server returned 500 as expected on port 8081")
        else:
            print("Server 8081 returned unexpected status code:", response8081.status_code)
            sys.exit(1)

    except Exception as e:
        print("Error connecting to server 8081:", e)
        sys.exit(1)

if __name__ == "__main__":
    test_servers()
    print("All tests passed successfully.")
    sys.exit(0)