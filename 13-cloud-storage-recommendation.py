import time

def recommend_storage(availability, storage_type, latency):
    if availability == "high":
        if storage_type == "file":
            if latency == "low":
                return "File Storage (e.g., AWS EFS, Azure Files, Google Filestore)"
            return "Distributed File Storage for High Latency Environments"
        if storage_type == "object":
            return "Object Storage (e.g., AWS S3, Azure Blob, Google Cloud Storage)"
        if storage_type == "block":
            if latency == "low":
                return "Block Storage (e.g., AWS EBS, Azure Managed Disks, Google Persistent Disks)"
            return "High-Availability Block Storage for High Latency Workloads"
    else:
        if storage_type == "file":
            if latency == "low":
                return "Standard File Storage (e.g., NAS, SMB-based storage)"
            return "Basic File Storage with Replication"
        if storage_type == "object":
            return "Standard Object Storage (e.g., AWS S3 Standard, Google Cloud Storage Standard)"
        if storage_type == "block":
            if latency == "low":
                return "Basic Block Storage (e.g., Local SSDs, On-Prem Block Storage)"
            return "Standard Block Storage with Higher Latency Tolerance"
    return "Custom Hybrid Storage Solution"

def get_input(prompt, options):
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print("Invalid choice. Try again.")

def main():
    print("Cloud Storage Recommendation System\n")
    availability = get_input("High availability required? (yes/no): ", ["yes", "no"])
    storage_type = get_input("Storage type (file/object/block): ", ["file", "object", "block"])
    latency = get_input("Latency sensitivity (low/high): ", ["low", "high"])
    
    availability = "high" if availability == "yes" else "normal"
    recommendation = recommend_storage(availability, storage_type, latency)

    print("\nProcessing...\n")
    time.sleep(2)
    print(f"Recommended Storage Type: {recommendation}")

if __name__ == "__main__":
    main()
