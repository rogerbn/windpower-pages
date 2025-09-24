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
<html>
<head>
    <meta charset="utf-8">
    <title>Status {date}</title>
</head>
<body style="background-color:{color}; height:100vh; margin:0;
             display:flex; align-items:center; justify-content:center;
             font-family:sans-serif;">
    <div style="text-align:center;">
        <h1 style="font-size:3em; color:{text_color}; margin:0;">
            {color.upper()}
        </h1>
        <p style="font-size:1.5em; color:{text_color}; margin:0;">
            {date}
        </p>
    </div>
</body>
</html>
"""

with open(html_file, "w") as f:
    f.write(html_content)

print(f"✅ Generated {html_file}")
