def filter_logs_by_topic(logs: list, target_topic: str) -> list:
    filtered = []
    for log in logs:
        topics = log.get("topics", [])
        if target_topic.lower() in [t.lower() for t in topics]:
            filtered.append(log)
    return filtered

if __name__ == "__main__":
    sample_logs = [{"topics": ["0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"]}]
    match = filter_logs_by_topic(sample_logs, "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef")
    print(f"Matched logs count: {len(match)}")
  
