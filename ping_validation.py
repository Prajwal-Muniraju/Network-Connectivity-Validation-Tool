import subprocess

devices = [
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.3",
    "192.168.2.1",
    "192.168.2.2",
    "192.168.2.3"
]

report = []

print("=== Network Connectivity Validation Report ===\n")

for ip in devices:

    print(f"Checking connectivity to {ip}...")

    response = subprocess.run(
        ["ping", "-n", "1", ip],
        capture_output=True,
        text=True
    )

    if "TTL=" in response.stdout:
        result = f"{ip} --> Reachable"
    else:
        result = f"{ip} --> Unreachable"

    print(result)
    report.append(result)

with open("validation_report.txt", "w") as file:
    for line in report:
        file.write(line + "\n")

print("\nValidation report generated successfully.")