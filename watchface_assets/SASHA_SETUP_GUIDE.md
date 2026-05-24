# Sasha's Watchface Maker v17.1 - Analog Pro Watchface Guide
## For Amazfit Active Max (480x480)

This guide will help you create an analog watchface with ticking seconds hand like an automatic watch.

---

## PREREQUISITES

### Assets Needed (in /workspace/watchface_assets/):
1. **background.png** (480x480) - ✅ Already created
2. **hour_hand.png** - Extract manually (see EXTRACTION_GUIDE.txt)
3. **minute_hand.png** - Extract manually
4. **second_hand.png** - Extract manually
5. **Optional**: subdial images, date frames, etc.

---

## STEP-BY-STEP INSTRUCTIONS FOR SASHA'S TOOL

### Step 1: Open Sasha's Watchface Maker v17.1
1. Launch the application on your PC
2. Click **"New Project"**
3. Select device: **Amazfit Active Max** (or custom 480x480)
4. Choose template: **Analog** or **Blank**

### Step 2: Add Background
1. Go to **"Background"** tab
2. Click **"Add Image"**
3. Select `background.png` from your assets folder
4. Position: X=0, Y=0
5. Ensure it fills the entire 480x480 canvas

### Step 3: Add Hour Hand
1. Go to **"Hands"** or **"Pointers"** tab
2. Click **"Add Hand"** → Select **"Hour Hand"**
3. Click on the hand layer → **"Change Image"**
4. Select `hour_hand.png`
5. **Set Pivot Point** (CRITICAL):
   - The pivot should be at the center of rotation
   - Typically: X = half of hand width, Y = near the bottom of the hand
   - Example: If hand is 40x120, pivot might be X=20, Y=100
6. **Position on Watch**:
   - Center X: 240 (half of 480)
   - Center Y: 240 (half of 480)
7. **Rotation Settings**:
   - Start angle: 0° (or adjust if hand points wrong direction)
   - End angle: 360°
   - Time range: 12 hours (for 12-hour format) or 24 hours

### Step 4: Add Minute Hand
1. In **"Hands"** tab, click **"Add Hand"** → Select **"Minute Hand"**
2. Change image to `minute_hand.png`
3. **Set Pivot Point**:
   - Similar to hour hand but adjusted for minute hand length
   - Example: If hand is 30x150, pivot might be X=15, Y=120
4. **Position on Watch**:
   - Center X: 240
   - Center Y: 240
5. **Rotation Settings**:
   - Time range: 60 minutes
   - Ensure smooth movement

### Step 5: Add Second Hand (Ticking Like Automatic Watch)
1. In **"Hands"** tab, click **"Add Hand"** → Select **"Second Hand"**
2. Change image to `second_hand.png`
3. **Set Pivot Point**:
   - Usually closer to the end for balance
   - Example: If hand is 20x180, pivot might be X=10, Y=150
4. **Position on Watch**:
   - Center X: 240
   - Center Y: 240
5. **Rotation Settings**:
   - Time range: 60 seconds
   - **For TICKING motion** (like automatic watch):
     - Look for **"Movement Type"** or **"Motion"** setting
     - Select **"Tick"** or **"Step"** instead of **"Smooth"**
     - Some versions have a checkbox: ☑️ **"Tick movement"**
     - Or set: **"Steps per cycle" = 60** (one tick per second)

### Step 6: Add Subdials (If Your Design Has Them)
1. Go to **"Images"** or **"Layers"** tab
2. Click **"Add Image"**
3. Select your subdial image (e.g., `subdial_1.png`)
4. Position according to your design:
   - 3 o'clock: X≈360, Y≈240
   - 6 o'clock: X≈240, Y≈360
   - 9 o'clock: X≈120, Y≈240
5. Add rotating hands for subdials if needed (follow Steps 3-5)

### Step 7: Add Date/Day Indicators (Optional)
1. Go to **"Text"** or **"Date"** tab
2. Click **"Add Date"**
3. Choose format: Day, Date, Month, etc.
4. Position on the watchface
5. Customize font, size, and color

### Step 8: Preview and Test
1. Click **"Preview"** button
2. Use the time slider to see hands move
3. Verify second hand ticks (not smooth sweep)
4. Check all elements are properly aligned

### Step 9: Export Watchface
1. Click **"Export"** or **"Build"**
2. Choose output format: **.bin** or **.wfz** (depending on your device)
3. Save to your computer
4. Transfer to your Amazfit Active Max using:
   - Amazfit app
   - Notify for Amazfit app
   - Direct file transfer

---

## TROUBLESHOOTING

### Second Hand Not Ticking?
- Check if "Smooth movement" is disabled
- Look for "Tick mode" or "Step mode" option
- Set steps to 60 for one tick per second
- Some versions require setting "Animation type" to "Quartz"

### Hands Not Aligned at 12:00?
- Adjust the **rotation offset** for each hand
- Hour hand at 12:00 should point straight up (0° or 90° depending on image)
- You may need to rotate the source image itself

### Pivot Point Wrong?
- The hand rotates around its pivot point
- If it orbits instead of rotating, move pivot to base of hand
- Test in preview mode and adjust until rotation looks natural

### Hands Behind Background?
- Check **layer order** in the layers panel
- Background should be at bottom (layer 0)
- Hands should be above background
- Drag layers to reorder if needed

---

## FILE STRUCTURE SUMMARY

```
/workspace/watchface_assets/
├── background.png          # 480x480 - Base layer
├── hour_hand.png           # ~100x150 - Extract manually
├── minute_hand.png         # ~120x180 - Extract manually  
├── second_hand.png         # ~130x200 - Extract manually
├── EXTRACTION_GUIDE.txt    # Manual extraction instructions
└── SASHA_SETUP_GUIDE.md    # This file
```

---

## PRO TIPS

1. **PNG with Transparency**: All hand images should have transparent backgrounds
2. **Pivot Point Testing**: Draw a small dot at the pivot point in your image editor to visualize rotation
3. **Hand Layering**: Order should be: Background → Hour → Minute → Second (top)
4. **Automatic Watch Feel**: The ticking second hand gives that classic mechanical watch feel
5. **Battery Optimization**: Tick movement uses less battery than smooth sweep

---

## NEXT STEPS

1. Manually extract the hand images from your reference photo
2. Save them as PNGs with transparent backgrounds
3. Follow this guide in Sasha's Watchface Maker
4. Test and refine until perfect!

Good luck with your watchface creation! 🕐⌚
