from PIL import Image
import os

# Load the reference image
img = Image.open('/workspace/PHOTO-2026-05-24-20-02-58.jpg')
print(f"Original image size: {img.size}")

# Amazfit Active Max resolution is 480x480
# The reference image is 916x1184, we need to extract and resize appropriately

# Create output directory
os.makedirs('/workspace/watchface_assets', exist_ok=True)

# Based on typical watchface layouts, let's extract the main components
# We'll create a script that extracts key regions - you may need to adjust coordinates

# For now, let's create the background resized to 480x480
background = img.resize((480, 480), Image.Resampling.LANCZOS)
background.save('/workspace/watchface_assets/background.png', 'PNG')
print("Created background.png (480x480)")

# Let's also save the original image info for manual extraction guidance
info_text = """
Amazfit Active Max Watchface Asset Extraction Guide
====================================================

Original Image: 916x1184 pixels
Target Resolution: 480x480 pixels

For Sasha's Watchface Maker v17.1, you'll need to extract these assets:

1. BACKGROUND (480x480):
   - Save as: background.png
   - This should include the brand logo and any static elements

2. HOUR HAND:
   - Extract the hour hand from the reference
   - Save as: hour_hand.png
   - Pivot point should be at the center of rotation
   - Recommended size: ~100x150 pixels

3. MINUTE HAND:
   - Extract the minute hand from the reference
   - Save as: minute_hand.png
   - Pivot point should be at the center of rotation
   - Recommended size: ~120x180 pixels

4. SECOND HAND:
   - Extract the second hand from the reference
   - Save as: second_hand.png
   - Pivot point should be at the center of rotation
   - Recommended size: ~130x200 pixels

5. SUBDIALS (if present):
   - Extract each subdial separately
   - Save as: subdial_1.png, subdial_2.png, etc.
   - Size: typically 100x100 or 120x120 pixels

6. DATE/DAY INDICATORS (if present):
   - Extract date window or day indicators
   - Save as: date_frame.png, day_frame.png

MANUAL EXTRACTION STEPS:
========================
Since automatic extraction requires knowing exact coordinates, please:

1. Open PHOTO-2026-05-24-20-02-58.jpg in an image editor (Photoshop, GIMP, etc.)
2. Note the coordinates of each element (hour hand, minute hand, second hand, subdials)
3. Extract each element as a separate PNG with transparent background
4. Ensure hands have their pivot point centered horizontally
5. Save all assets to /workspace/watchface_assets/ folder

Common coordinate ranges to check in the 916x1184 image:
- Center point is approximately at (458, 592)
- Hour hand: typically shorter, thicker
- Minute hand: longer, thinner
- Second hand: thinnest, often red or contrasting color
- Subdials: usually at 3, 6, or 9 o'clock positions

After extracting assets manually, use the guide below for Sasha's tool.
"""

with open('/workspace/watchface_assets/EXTRACTION_GUIDE.txt', 'w') as f:
    f.write(info_text)

print("\nCreated EXTRACTION_GUIDE.txt with detailed instructions")
print("\nAssets folder created at: /workspace/watchface_assets/")
