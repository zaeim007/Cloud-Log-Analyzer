from collections import Counter
import math


# Security Feature #1
def detect_suspicious_ips(ip_counter):

    if not ip_counter:
        return []

    counts = list(ip_counter.values())

    mean = sum(counts) / len(counts)

    variance = sum(
        (count - mean) ** 2
        for count in counts
    ) / len(counts)

    std_dev = math.sqrt(variance)

    statistical_threshold = mean + (2 * std_dev)

    traffic_threshold = mean * 1.5

    threshold = max(
        statistical_threshold,
        traffic_threshold
    )

    suspicious_ips = []

    for ip, count in ip_counter.items():

        if count > threshold:

            suspicious_ips.append({
                "ip": ip,
                "requests": count
            })

    suspicious_ips.sort(
        key=lambda x: x["requests"],
        reverse=True
    )

    return suspicious_ips


# Security Feature #2
def detect_brute_force(login_failures, threshold=10):

    brute_force_ips = []

    for ip, failures in login_failures.items():

        if failures >= threshold:

            brute_force_ips.append({
                "ip": ip,
                "failed_attempts": failures
            })

    brute_force_ips.sort(
        key=lambda x: x["failed_attempts"],
        reverse=True
    )

    return brute_force_ips


# Security Feature #3
def detect_404_scanners(not_found_counter):

    if not not_found_counter:
        return []

    counts = list(not_found_counter.values())

    mean = sum(counts) / len(counts)

    variance = sum(
        (count - mean) ** 2
        for count in counts
    ) / len(counts)

    std_dev = math.sqrt(variance)

    threshold = mean + (2 * std_dev)

    scanners = []

    for ip, count in not_found_counter.items():

        if count > threshold:

            scanners.append({
                "ip": ip,
                "not_found_requests": count
            })

    scanners.sort(
        key=lambda x: x["not_found_requests"],
        reverse=True
    )

    return scanners


def generate_report(
    ips,
    pages,
    statuses,
    processed_records,
    skipped_records,
    login_failures,
    not_found_counter
):

    total_requests = processed_records

    error_count = sum(
        1 for status in statuses
        if status >= 400
    )

    error_rate = round(
        (error_count / total_requests) * 100,
        2
    ) if total_requests > 0 else 0

    ip_counter = Counter(ips)
    page_counter = Counter(pages)
    status_counter = Counter(statuses)

    most_active_ip = (
        ip_counter.most_common(1)[0][0]
        if ip_counter
        else "N/A"
    )

    most_visited_page = (
        page_counter.most_common(1)[0][0]
        if page_counter
        else "N/A"
    )

    suspicious_ips = detect_suspicious_ips(
        ip_counter
    )

    brute_force_attempts = detect_brute_force(
        login_failures
    )

    excessive_404_ips = detect_404_scanners(
        not_found_counter
    )

    return {
        "total_requests": total_requests,
        "processed_records": processed_records,
        "skipped_records": skipped_records,
        "error_count": error_count,
        "error_rate": error_rate,
        "most_active_ip": most_active_ip,
        "top_ips": ip_counter.most_common(5),
        "most_visited_page": most_visited_page,
        "top_pages": page_counter.most_common(5),
        "status_codes": dict(status_counter),

        # Security Feature #1
        "suspicious_ips": suspicious_ips,

        # Security Feature #2
        "brute_force_attempts": brute_force_attempts,

        # Security Feature #3
        "excessive_404_ips": excessive_404_ips
    }


def analyze_log(file_path):

    print("File path received:", file_path)

    ips = []
    pages = []
    statuses = []

    processed_records = 0
    skipped_records = 0

    login_failures = Counter()
    not_found_counter = Counter()

    with open(file_path, "r") as file:

        for line in file:

            try:

                parts = line.strip().split()

                if len(parts) < 4:
                    skipped_records += 1
                    continue

                ip = parts[0]
                page = parts[2]
                status = int(parts[3])

                ips.append(ip)
                pages.append(page)
                statuses.append(status)

                # Security Feature #2
                if (
                    page in ["/login", "/admin"]
                    and status == 403
                ):
                    login_failures[ip] += 1

                # Security Feature #3
                if status == 404:
                    not_found_counter[ip] += 1

                processed_records += 1

            except Exception:

                skipped_records += 1

    return generate_report(
        ips,
        pages,
        statuses,
        processed_records,
        skipped_records,
        login_failures,
        not_found_counter
    )