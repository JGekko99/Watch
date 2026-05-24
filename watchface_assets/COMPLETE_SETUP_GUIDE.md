# Sasha's Watchface Maker v17.1 - Complete Setup Guide for Amazfit Active Max

## Extracted Assets Summary

All assets have been extracted from your reference image and are ready in the `watchface_assets/` folder:

### Core Assets (Required):
1. **background_480x480.png** (480x480) - Main dial background with hour markers, brand logo, and subdials
2. **hour_hand_480.png** (71x88) - Hour hand with transparent background
3. **minute_hand_480.png** (56x127) - Minute hand with transparent background  
4. **second_hand_480.png** (28x166) - Second hand with transparent background

### Reference Assets (For Manual Refinement):
- **full_dial_reference.png** - Original extracted dial for reference
- **hands_diff_mask.png** - Shows where all hands were located
- **subdial_3_oclock.png**, **subdial_6_oclock.png**, **subdial_9_oclock.png** - Subdial extracts

---

## Step-by-Step Sasha Tool Setup

### Step 1: Open Sasha's Watchface Maker v17.1
1. Launch the application
2. Click "Create New Watchface"
3. Select device: **Amazfit Active Max** (480x480 resolution)

### Step 2: Set the Background
1. Go to the "Background" tab
2. Click "Add Image" or drag & drop
3. Select: **background_480x480.png**
4. Position: X=0, Y=0 (should fill entire screen)
5. This includes: dial face, hour markers, brand logo, and subdial backgrounds

### Step 3: Add the Hour Hand
1. Go to "Pointers" or "Hands" tab
2. Click "Add Pointer" → Select "Hour Hand"
3. Import image: **hour_hand_480.png**
4. **Critical Settings:**
   - Pivot Point X: 35 (center of hand width)
   - Pivot Point Y: 80 (near bottom of hand image)
   - Position X: 240 (screen center)
   - Position Y: 240 (screen center)
   - Angle offset: Adjust so hand points to 12 at midnight
   - Time range: 0-12 hours

### Step 4: Add the Minute Hand
1. Click "Add Pointer" → Select "Minute Hand"
2. Import image: **minute_hand_480.png**
3. **Critical Settings:**
   - Pivot Point X: 28 (center of hand width)
   - Pivot Point Y: 115 (near bottom of hand image)
   - Position X: 240 (screen center)
   - Position Y: 240 (screen center)
   - Angle offset: Adjust to align with hour markers
   - Time range: 0-60 minutes

### Step 5: Add the Second Hand (with TICKING motion)
1. Click "Add Pointer" → Select "Second Hand"
2. Import image: **second_hand_480.png**
3. **Critical Settings for Automatic Watch Ticking:**
   - Pivot Point X: 14 (center of thin hand)
   - Pivot Point Y: 150 (near bottom of hand image)
   - Position X: 240 (screen center)
   - Position Y: 240 (screen center)
   - Angle offset: Adjust to point at 12
   - Time range: 0-60 seconds
   
4. **ENABLE TICKING MOTION:**
   - Look for "Movement Type" or "Motion Mode" dropdown
   - Select: **"Tick"** or **"Step"** or **"Discrete"** (NOT "Smooth" or "Continuous")
   - Some versions call this: "Quartz mode" or "Step movement"
   - This makes the second hand jump once per second like a real automatic watch

### Step 6: Fine-Tune Hand Alignment
1. Preview the watchface
2. Check that all hands point correctly at 12:00:00
3. If needed, adjust the "Angle Offset" for each hand:
   - Positive values rotate clockwise
   - Negative values rotate counter-clockwise
4. Ensure hands are layered correctly (second hand on top)

### Step 7: Add Subdials (Optional - if they show data)
If your subdials display complications (steps, heart rate, etc.):

1. Go to "Complications" or "Data Display" tab
2. For each subdial position:
   - **3 o'clock subdial**: Add complication, position ~X=360, Y=240
   - **6 o'clock subdial**: Add complication, position ~X=240, Y=360
   - **9 o'clock subdial**: Add complication, position ~X=120, Y=240
3. Choose data type: Steps, Heart Rate, Battery, Date, etc.

### Step 8: Save and Export
1. Click "Save Project" to keep editable file
2. Click "Export" or "Build Watchface"
3. Select format: **.bin** for Amazfit devices
4. The tool will generate a .bin file ready for installation

---

## Installing on Amazfit Active Max

### Method 1: Via Amazfit App
1. Transfer the .bin file to your phone
2. Open Amazfit app
3. Go to Profile → Your Device → Watch Faces
4. Look for "Import" or "+" button
5. Select the .bin file

### Method 2: Direct Transfer
1. Connect watch to computer via USB (if supported)
2. Copy .bin file to watch's watchface folder
3. Disconnect and select new face from watch settings

---

## Troubleshooting

### Hands Not Visible?
- Check that PNG files have transparency (alpha channel)
- Verify pivot points are set correctly
- Ensure hand images are not positioned off-screen

### Second Hand Not Ticking?
- In Sasha tool, look for these setting names:
  - "Movement: Tick/Step" 
  - "Animation: Discrete"
  - "Mode: Quartz" (not "Automatic" or "Smooth")
- Some versions have a checkbox: "Enable step movement"

### Hands Misaligned?
- Adjust "Angle Offset" in small increments (1-5 degrees)
- Test at different times (3:00, 6:00, 9:00) to verify alignment

### Colors Look Wrong?
- Ensure images are in sRGB color space
- Check that PNG compression didn't alter colors
- Try saving as PNG-24 (not PNG-8)

---

## Asset Notes

The automatically extracted hands may need manual refinement in an image editor:
- Open the hand PNGs in Photoshop/GIMP
- Clean up any artifacts around the edges
- Ensure the hand extends to the edge of the canvas where it should pivot
- Save with transparency preserved

For best results, you can trace over the extracted hands to create cleaner versions.

---

## File Locations

```
/workspace/watchface_assets/
├── background_480x480.png      ← Use this for background
├── hour_hand_480.png           ← Use this for hour hand
├── minute_hand_480.png         ← Use this for minute hand
├── second_hand_480.png         ← Use this for second hand
├── full_dial_reference.png     ← Reference only
├── hands_diff_mask.png         ← Reference only
└── subdial_*.png               ← Optional for complications
```

Good luck with your watchface creation!
