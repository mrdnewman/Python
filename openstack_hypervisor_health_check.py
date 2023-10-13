from openstack import connection

# OpenStack Credentials
auth_url = "https://your-openstack-auth-url"
project_name = "your-project"
username = "your-username"
password = "your-password"

# Initialize the OpenStack connection
conn = connection.Connection(
    auth_url=auth_url,
    project_name=project_name,
    username=username,
    password=password,
)

# Get a list of availability zones
azs = conn.compute.availability_zones()

failed_hypervisors = {}

# Iterate through availability zones
for az in azs:
    az_name = az.zoneName
    print(f"Checking Availability Zone: {az_name}")

    # List hypervisors in the availability zone
    hypervisors = conn.compute.hypervisors(availability_zone=az_name)

    # Iterate through hypervisors in the availability zone
    for hypervisor in hypervisors:
        if hypervisor.state == "up" and hypervisor.status == "enabled":
            # Hypervisor is active, continue
            continue

        # Hypervisor is not active or not enabled, add it to the failed list
        failed_hypervisors[hypervisor.hypervisor_hostname] = {
            "Availability Zone": az_name,
            "State": hypervisor.state,
            "Status": hypervisor.status,
        }

# Generate a report of failed hypervisors
print("\nFailed Hypervisors Report:")
for hostname, details in failed_hypervisors.items():
    print(f"Hypervisor: {hostname}")
    print(f"Availability Zone: {details['Availability Zone']}")
    print(f"State: {details['State']}")
    print(f"Status: {details['Status']}")
    print("---------------")

# Output the report to a file
with open("failed_hypervisors_report.txt", "w") as report_file:
    for hostname, details in failed_hypervisors.items():
        report_file.write(f"Hypervisor: {hostname}\n")
        report_file.write(f"Availability Zone: {details['Availability Zone']}\n")
        report_file.write(f"State: {details['State']}\n")
        report_file.write(f"Status: {details['Status']}\n")
        report_file.write("---------------\n")

print("Report saved to 'failed_hypervisors_report.txt'")
