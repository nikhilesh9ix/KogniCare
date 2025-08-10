# 🎥 Video Integration Setup Guide

## Quick Setup Steps

### 1. Add Your Video File

Copy your video file to the static folder:
```
Kognicare/
├── static/
│   └── Hospital_Patient_Monitoring_Video_Generation.mp4  ← Put your video here
├── templates/
├── app.py
└── ...
```

### 2. File Location
Your video should be placed at:
```
c:\Files\Files\BTech College\Projects\Kognicare\static\Hospital_Patient_Monitoring_Video_Generation.mp4
```

### 3. How It Works

- **Default State**: Shows a placeholder with "Click to start monitoring"
- **Active State**: Plays your video on continuous loop
- **Toggle Function**: Click to start/stop the video feed
- **Auto-loop**: Video will automatically restart when it ends

### 4. Video Specifications

**Recommended Settings:**
- **Format**: MP4 (H.264 codec)
- **Resolution**: 720p (1280x720) or 1080p (1920x1080)
- **Frame Rate**: 24-30 fps
- **Duration**: Any length (will loop)
- **Audio**: Not required (video is muted for medical environment)

**File Size Considerations:**
- Keep under 50MB for smooth loading
- Higher quality videos may load slower

### 5. Features

✅ **Automatic Loop**: Video plays continuously once started
✅ **Click to Toggle**: Easy start/stop functionality  
✅ **Professional UI**: Integrated seamlessly with medical dashboard
✅ **Status Indicator**: Shows "Ready" or "Live" status
✅ **Responsive Design**: Works on all screen sizes

### 6. Testing Your Video

1. **Place the video file** in the static folder
2. **Start the application** with `.\start.bat`
3. **Open the dashboard** at `http://localhost:5000`
4. **Look for the camera feed** in the right panel
5. **Click "Click to start monitoring"** to begin video playback

### 7. AI Integration

When video is active, the AI analysis panel will show:
- **Current Status**: "Monitoring patient via video feed"
- **Activity Level**: "Video analysis active"

This simulates real-time AI video analysis that would be possible with computer vision integration.

### 8. Troubleshooting

**Video not loading?**
- Check file path: `/static/Hospital_Patient_Monitoring_Video_Generation.mp4`
- Verify file format is MP4
- Check file size (keep under 100MB)
- Ensure Flask server is running

**Video not playing?**
- Try a different browser (Chrome, Firefox, Edge)
- Check browser's autoplay settings
- Verify video codec compatibility

**File not found error?**
- Make sure the video file is exactly named: `Hospital_Patient_Monitoring_Video_Generation.mp4`
- Check that it's in the `static` folder
- Restart the Flask application

### 9. Alternative Video Names

If you want to use a different filename, update this line in `templates/index.html`:
```html
<source src="/static/YOUR_VIDEO_NAME.mp4" type="video/mp4">
```

### 10. Future Enhancements

The video integration is designed to be easily extended for:
- **Multiple camera feeds**
- **Real-time streaming integration**
- **Computer vision AI analysis**
- **Recording capabilities**
- **Privacy controls**

---

**🎬 Your patient monitoring video is ready to integrate!**

Once you copy the video file to the static folder, the camera feed will show professional hospital monitoring footage that loops continuously, enhancing the realism of your AI patient monitoring system demonstration.
