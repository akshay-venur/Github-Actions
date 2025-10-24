import argparse
from datetime import datetime, timedelta
import os

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Generate dates for a given range")
parser.add_argument("--start", required=True, help="Start date in YYYY-MM-DD format")
parser.add_argument("--end", required=True, help="End date in YYYY-MM-DD format")
args = parser.parse_args()

start_date = datetime.strptime(args.start, "%Y-%m-%d")
end_date = datetime.strptime(args.end, "%Y-%m-%d")

# Create output folder if it doesn’t exist
os.makedirs("output", exist_ok=True)

# Prepare output file path
output_file = os.path.join("output", "dates.txt")

# Generate all dates between start and end
current_date = start_date
dates = []
while current_date <= end_date:
    dates.append(current_date.strftime("%Y-%m-%d"))
    current_date += timedelta(days=1)

# --- Get current timestamp ---
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Write to file
with open(output_file, "w") as f:
    for d in dates:
        f.write(d + "\n")
    f.write("\nGenerated on: " + timestamp + "\n")

# Print info
print(f"Generated {len(dates)} dates from {args.start} to {args.end}")
print(f"Saved to: {output_file}")
