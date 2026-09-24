import json
import os

# Input and output
json_file = "data.json"
html_file = "index.html"
annual_sums_file = "annual_sums.json"
history_file = "sum_history.json"

if not os.path.exists(json_file):
    raise FileNotFoundError(f"{json_file} not found")

with open(json_file) as f:
    data = json.load(f)

color = data.get("status", "yellow")
date = data.get("date", "unknown")
sum_value = data.get("sum", 0)
index_value = data.get("index", 1)  # Avoid division by zero

year = str(date)[:4]

if not year.isdigit() or len(year) != 4:
    raise ValueError(f"Could not determine a year from date: {date}")

annual_sums = {}

if os.path.exists(annual_sums_file):
    with open(annual_sums_file, "r", encoding="utf-8") as f:
        annual_sums = json.load(f)

annual_sums[year] = annual_sums.get(year, 0) + float(sum_value)

with open(annual_sums_file, "w", encoding="utf-8") as f:
    json.dump(annual_sums, f, indent=2)
    f.write("\n")

ytd_value = annual_sums[year]
ytd_text = f"{ytd_value:,.2f}"

if os.path.exists(history_file):
    with open(history_file, "r", encoding="utf-8") as f:
        history = json.load(f)
else:
    history = []

record = {
    "date": str(date),
    "sum": float(sum_value)
}

# Avoid adding the same date repeatedly if the script is run again.
history = [item for item in history if item.get("date") != record["date"]]
history.append(record)

# Optional: keep records ordered by date
history.sort(key=lambda item: item["date"])

with open(history_file, "w", encoding="utf-8") as f:
    json.dump(history, f, indent=2)
    f.write("\n")

# Compute difference and percentage
diff = sum_value - index_value
percent = (diff / index_value) * 100

# Format nicely
diff_text = f"{diff:+,.2f}"  # + shows sign
percent_text = f"{percent:+.2f}%"

# Decide text color based on background
text_color = "white" if "dark" in color or color in ["red", "green"] else "black"

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Status {date}</title>
  <style>
    body {{
      margin: 0;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      background-color: {color};
      color: {text_color};
      text-align: center;
    }}
    h1 {{
      font-size: 12vw; /* scales with screen width */
      margin: 0;
    }}
    p {{
      font-size: 6vw; /* smaller but still responsive */
      margin: 0;
    }}
  </style>
</head>
<body>
  <div>
    <h1>{color.upper()}</h1>
    <p>{date}</p>
    <p>{percent_text} ({diff_text})</p>
  </div>
</body>
</html>
"""

with open(html_file, "w") as f:
    f.write(html_content)

print(f"✅ Generated {html_file}")
