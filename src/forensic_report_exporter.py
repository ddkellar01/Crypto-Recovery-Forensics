import json

def export_forensic_report(data_dict: dict, filename: str = "forensic_report.json"):
    with open(filename, "w") as f:
        json.dump(data_dict, f, indent=4)
    print(f"Report successfully exported to {filename}")

if __name__ == "__main__":
    export_forensic_report({"target": "0x3535...", "status": "analyzed"})
  
