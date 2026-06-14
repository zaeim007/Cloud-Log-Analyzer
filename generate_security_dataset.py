import random

OUTPUT_FILE = "logs/security_million.log"

NORMAL_IPS = [
    f"192.168.1.{i}"
    for i in range(1, 101)
]

PAGES = [
    "/home",
    "/products",
    "/cart",
    "/profile",
    "/contact"
]

STATUS_CODES = [
    200,
    200,
    200,
    200,
    404,
    403,
    500
]

TOTAL_LOGS = 1_000_000

# Attack IPs
SUSPICIOUS_IP = "10.0.0.1"
BRUTE_FORCE_IP = "10.0.0.2"
SCANNER_IP = "10.0.0.3"

# Attack volumes
SUSPICIOUS_TRAFFIC = 100_000
BRUTE_FORCE_ATTEMPTS = 10_000
SCANNER_ATTEMPTS = 10_000

MALFORMED_ROWS = 50_000


with open(OUTPUT_FILE, "w") as file:

    print("Generating normal traffic...")

    normal_logs = (
        TOTAL_LOGS
        - SUSPICIOUS_TRAFFIC
        - BRUTE_FORCE_ATTEMPTS
        - SCANNER_ATTEMPTS
        - MALFORMED_ROWS
    )

    for _ in range(normal_logs):

        ip = random.choice(NORMAL_IPS)

        page = random.choice(PAGES)

        status = random.choice(STATUS_CODES)

        file.write(
            f"{ip} GET {page} {status}\n"
        )

    print("Generating suspicious IP traffic...")

    for _ in range(SUSPICIOUS_TRAFFIC):

        page = random.choice(PAGES)

        file.write(
            f"{SUSPICIOUS_IP} GET {page} 200\n"
        )

    print("Generating brute force attack...")

    for _ in range(BRUTE_FORCE_ATTEMPTS):

        file.write(
            f"{BRUTE_FORCE_IP} GET /login 403\n"
        )

    print("Generating 404 scanner attack...")

    scan_pages = [
        "/wp-admin",
        "/phpmyadmin",
        "/config.php",
        "/backup.zip",
        "/admin.php",
        "/database.sql",
        "/secret",
        "/old-backup.zip"
    ]

    for _ in range(SCANNER_ATTEMPTS):

        page = random.choice(scan_pages)

        file.write(
            f"{SCANNER_IP} GET {page} 404\n"
        )

    print("Generating malformed rows...")

    bad_rows = [
        "hello world",
        "abc xyz",
        "random text",
        "invalid log",
        "broken record"
    ]

    for _ in range(MALFORMED_ROWS):

        file.write(
            random.choice(bad_rows) + "\n"
        )

print("Done.")
print(f"Created: {OUTPUT_FILE}")