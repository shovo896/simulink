
---

## 2️⃣ `scripts/generate_readme.py`

```python
import os
from datetime import datetime

# Path to Simulink models
MODEL_DIR = "./"
ASSET_DIR = "./assets/"

# List of Simulink models and preview images
models = []
for file in os.listdir(MODEL_DIR):
    if file.endswith(".slx"):
        image_file = os.path.join(ASSET_DIR, file.replace(".slx", ".png"))
        if not os.path.exists(image_file):
            image_file = ""  # No preview
        models.append({"file": file, "image": image_file})

# Generate the Markdown table
model_table = "| Model | Preview |\n|-------|--------|\n"
for model in models:
    name = model["file"].replace(".slx", "").replace("_", " ").title()
    if model["image"]:
        model_table += f"| {name} | ![{name}]({model['image']}) |\n"
    else:
        model_table += f"| {name} | Preview not available |\n"

# Read template README
with open("README_TEMPLATE.md", "r") as f:
    template = f.read()

# Replace placeholders
readme_content = template.replace("{{MODEL_TABLE}}", model_table)
readme_content = readme_content.replace("{{LAST_UPDATED}}", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Write README.md
with open("README.md", "w") as f:
    f.write(readme_content)

print("README.md updated successfully!")
