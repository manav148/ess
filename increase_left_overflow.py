#!/usr/bin/env python3
import re

with open('/Users/manav/Downloads/ess/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the current positioning
pattern = r'<img src="small-storage-items\.webp" alt="Storage items in boxes" style="position:absolute;bottom:-50px;left:-30px;width:40%;height:auto;border-radius:8px;box-shadow:0 4px 6px rgba\(0,0,0,0\.1\)">'

# Increase left overflow significantly - about half the image should be outside
# Using -100px to get approximately half the image overflowing on the left
replacement = r'<img src="small-storage-items.webp" alt="Storage items in boxes" style="position:absolute;bottom:-50px;left:-100px;width:40%;height:auto;border-radius:8px;box-shadow:0 4px 6px rgba(0,0,0,0.1)">'

html = re.sub(pattern, replacement, html)

with open('/Users/manav/Downloads/ess/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Increased left overflow to -100px - about half the image extends beyond left edge!")
