"""
Test script for F5 DevOps Assignment.
Tests: HTTP 200 on port 8080, HTTP 500 on port 8081, and rate limiting.
Exit codes: 0 = all tests passed, 1 = test failed (used by CI)
"""
import requests
import sys


def test_servers():
    # Test 1: Port 8080 should return 200 (healthy server)
    # Assumption: nginx-server DNS name is resolved via Docker network
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

    # Test 2: Port 8081 should return 500 (simulated error)
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

    # Test 3: Rate limiting - send 20 rapid requests, some should be blocked (503)
    # Trade-off: 20 requests is arbitrary, enough to trigger limit without being excessive
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
            pass  # Network errors ignored - focus on rate limit behavior

    print(f"Summary: {success_count} succeeded, {blocked_count} blocked.")

    # Assumption: at least 1 blocked request means rate limiting works
    if blocked_count > 0:
        print("Rate Limiting Test Passed: Some requests were blocked.")
    else:
        print("Rate Limiting Test Failed: No requests were blocked (Config issue?)")
        sys.exit(1)


if __name__ == "__main__":
    test_servers()
    print("All tests passed successfully.")
    sys.exit(0)  # Exit 0 = success, tells CI pipeline tests passed
