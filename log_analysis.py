# -*- coding: utf-8 -*-
"""Log-Analysis.py.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GpivlsaL9wQsIADn79PKUL4Ase9T7Fgd
"""

import csv
from collections import defaultdict

# Configuration
FAILED_LOGIN_THRESHOLD = 10

def parse_log(file_path):
    """Parse the log file and return structured data."""
    requests_by_ip = defaultdict(int)
    endpoints = defaultdict(int)
    failed_logins = defaultdict(int)

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) < 9:
                continue

            # Extract IP Address
            ip = parts[0]
            requests_by_ip[ip] += 1

            # Extract Endpoint
            endpoint = parts[6]
            endpoints[endpoint] += 1

            # Check for failed login attempts
            status_code = parts[8]
            if status_code == "401" or "Invalid credentials" in line:
                failed_logins[ip] += 1

    return requests_by_ip, endpoints, failed_logins

def save_to_csv(data, headers, filename):
    """Save data to a CSV file."""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data)

def analyze_log(file_path):
    """Analyze the log file and output results."""
    # Parse log file
    requests_by_ip, endpoints, failed_logins = parse_log(file_path)

    # Count requests per IP
    ip_request_data = sorted(requests_by_ip.items(), key=lambda x: x[1], reverse=True)

    print("IP Address           Request Count")
    for ip, count in ip_request_data:
        print(f"{ip:<20} {count}")

    # Identify the most frequently accessed endpoint
    most_accessed_endpoint = max(endpoints.items(), key=lambda x: x[1])
    print("\nMost Frequently Accessed Endpoint:")
    print(f"{most_accessed_endpoint[0]} (Accessed {most_accessed_endpoint[1]} times)")

    # Detect suspicious activity
    suspicious_ips = [(ip, count) for ip, count in failed_logins.items() if count > FAILED_LOGIN_THRESHOLD]

    print("\nSuspicious Activity Detected:")
    if suspicious_ips:
        print("IP Address           Failed Login Attempts")
        for ip, count in suspicious_ips:
            print(f"{ip:<20} {count}")
    else:
        print("No suspicious activity detected.")

    # Save results to CSV
    save_to_csv(ip_request_data, ["IP Address", "Request Count"], "requests_per_ip.csv")
    save_to_csv([most_accessed_endpoint], ["Endpoint", "Access Count"], "most_accessed_endpoint.csv")
    save_to_csv(suspicious_ips, ["IP Address", "Failed Login Count"], "suspicious_activity.csv")

    print("\nResults saved to CSV files.")

# File path to the log file
log_file_path = "/content/sample.log"

# Analyze the log
analyze_log(log_file_path)