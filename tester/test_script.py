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


    print("\n Starting Rate Limit Test (Sending 20 requests fast)...")
    blocked_count = 0
    success_count = 0
    
    for i in range(20):
        try:
            response = requests.get("http://nginx-server:8080")
            if response.status_code == 200:
                success_count += 1
            elif response.status_code == 503:
                blocked_count += 1
                print(f"   Request {i+1}: Blocked! (503 Service Unavailable)")
        except:
            pass

    print(f"Summary: {success_count} succeeded, {blocked_count} blocked.")

    if blocked_count > 0:
        print("Rate Limiting Test Passed: Some requests were blocked.")
    else:
        print("Rate Limiting Test Failed: No requests were blocked (Config issue?)")
        sys.exit(1)

        

if __name__ == "__main__":
    test_servers()
    print("All tests passed successfully.")
    sys.exit(0)