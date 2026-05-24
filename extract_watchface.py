from PIL import Image
import os
import math

# Load the original image
img = Image.open('PHOTO-2026-05-24-20-02-58.jpg')

# From previous analysis:
# Dial bounds: (237, 196, 727, 686) - this is 490x490
dial_bounds = (237, 196, 727, 686)
dial_crop = img.crop(dial_bounds)
dial_w, dial_h = dial_crop.size
dial_center = (dial_w // 2, dial_h // 2)

print(f"Dial size: {dial_w}x{dial_h}, center: {dial_center}")

# Save the full dial as reference
dial_crop.save('watchface_assets/full_dial_reference.png')
print("Saved full_dial_reference.png")

# Create a clean background by sampling from edges
def create_clean_bg(dial_img, center):
    bg = dial_img.copy()
    cx, cy = center
    w, h = dial_img.size
    hand_radius = int(min(w, h) * 0.25)
    
    for y in range(max(0, cy - hand_radius), min(h, cy + hand_radius)):
        for x in range(max(0, cx - hand_radius), min(w, cx + hand_radius)):
            dist_sq = (x - cx)*(x - cx) + (y - cy)*(y - cy)
            if dist_sq < hand_radius*hand_radius:
                sample_angle = math.atan2(y - cy, x - cx)
                sample_r = hand_radius + 15
                sx = int(cx + sample_r * math.cos(sample_angle))
                sy = int(cy + sample_r * math.sin(sample_angle))
                if 0 <= sx < w and 0 <= sy < h:
                    bg.putpixel((x, y), dial_img.getpixel((sx, sy)))
    return bg

bg_clean = create_clean_bg(dial_crop, dial_center)
bg_clean.save('watchface_assets/background_clean_490x490.png')
print("Created background_clean_490x490.png")

# Scale to 480x480 for Active Max
bg_480 = bg_clean.resize((480, 480), Image.Resampling.LANCZOS)
bg_480.save('watchface_assets/background_480x480.png')
print("Saved background_480x480.png")

# Now extract hands by analyzing the difference between original and clean background
diff = Image.new('RGBA', dial_crop.size, (0, 0, 0, 0))
for y in range(dial_h):
    for x in range(dial_w):
        orig_pixel = dial_crop.getpixel((x, y))
        clean_pixel = bg_clean.getpixel((x, y))
        # Calculate difference
        diff_val = sum(abs(orig_pixel[i] - clean_pixel[i]) for i in range(3))
        if diff_val > 50:  # Significant difference = likely a hand
            diff.putpixel((x, y), (*orig_pixel, 255))
        else:
            diff.putpixel((x, y), (0, 0, 0, 0))

diff.save('watchface_assets/hands_diff_mask.png')
print("Created hands_diff_mask.png showing all hands")

# Extract individual hand regions based on distance from center
def extract_hand_by_distance(dial_img, bg_img, center, min_dist, max_dist, width_factor=0.1):
    w, h = dial_img.size
    cx, cy = center
    hand_w = int(min(w, h) * width_factor)
    hand_h = max_dist - min_dist
    
    # Create vertical hand image
    hand_img = Image.new('RGBA', (hand_w, hand_h), (0, 0, 0, 0))
    
    for dy in range(min_dist, max_dist):
        for dx in range(-hand_w//2, hand_w//2):
            x = cx + dx
            y = cy - dy  # Going upward from center
            
            if 0 <= x < w and 0 <= y < h:
                orig = dial_img.getpixel((x, y))
                clean = bg_img.getpixel((x, y))
                diff_val = sum(abs(orig[i] - clean[i]) for i in range(3))
                
                if diff_val > 40:
                    hand_x = dx + hand_w//2
                    hand_y = dy - min_dist
                    if 0 <= hand_x < hand_w and 0 <= hand_y < hand_h:
                        hand_img.putpixel((hand_x, hand_y), (*orig, 255))
    
    return hand_img

# Hour hand: closest to center (shortest)
hour_hand = extract_hand_by_distance(dial_crop, bg_clean, dial_center, 10, 100, 0.15)
hour_hand.save('watchface_assets/hour_hand_490.png')
print(f"Created hour_hand_490.png: {hour_hand.size}")

# Minute hand: medium distance
minute_hand = extract_hand_by_distance(dial_crop, bg_clean, dial_center, 50, 180, 0.12)
minute_hand.save('watchface_assets/minute_hand_490.png')
print(f"Created minute_hand_490.png: {minute_hand.size}")

# Second hand: longest, thinnest
second_hand = extract_hand_by_distance(dial_crop, bg_clean, dial_center, 30, 200, 0.06)
second_hand.save('watchface_assets/second_hand_490.png')
print(f"Created second_hand_490.png: {second_hand.size}")

# Scale hands to 480
scale = 480 / 490
for name in ['hour_hand', 'minute_hand', 'second_hand']:
    hand = Image.open(f'watchface_assets/{name}_490.png')
    new_size = (int(hand.width * scale), int(hand.height * scale))
    hand_scaled = hand.resize(new_size, Image.Resampling.LANCZOS)
    hand_scaled.save(f'watchface_assets/{name}_480.png')
    print(f"Scaled {name} to {new_size}")

print("\n=== ASSETS CREATED ===")
print("All assets saved to watchface_assets/")
