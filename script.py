import json
import os

# Input and output
json_file = "data.json"
html_file = "index.html"

if not os.path.exists(json_file):
    raise FileNotFoundError(f"{json_file} not found")

with open(json_file) as f:
    data = json.load(f)

color = data.get("status", "yellow")
date = data.get("date", "unknown")

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
  </div>
</body>
</html>
"""

with open(html_file, "w") as f:
    f.write(html_content)

print(f"✅ Generated {html_file}")
