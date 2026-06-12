# Auto-Liker-Facebook

A small Python automation script that automatically "likes" posts on a given Facebook
profile. It works purely through GUI automation: it opens the profile in your browser,
visually locates the Like button on screen using template image matching, clicks it,
scrolls down, and repeats until a set number of posts have been liked.

Because it relies on screen recognition (not the Facebook API or page scraping), no login
tokens or credentials are handled by the script — it simply drives the mouse and keyboard
the way a person would.

## How It Works

1. Opens the target profile URL in your default web browser.
2. Repeatedly searches the screen for the Like button using `pyautogui.locateOnScreen`
   with the reference image `likebtn.png` (OpenCV is used for confidence-based matching).
3. When a match is found, it moves to the button's center and clicks it.
4. Scrolls the page down and keeps going until `no_of_posts` likes have been performed.

## Features

- Image-recognition based clicking (matches the `likebtn.png` template against the screen)
- Configurable target profile URL
- Configurable number of posts to like (`no_of_posts`)
- Automatic scrolling between likes

## Tech Stack

- **Language:** Python 3
- **Dependencies:**
  - [`pyautogui`](https://pypi.org/project/PyAutoGUI/) – mouse/keyboard control and on-screen image location
  - [`opencv-python`](https://pypi.org/project/opencv-python/) – enables the `confidence` parameter for image matching

## Project Structure

```
.
├── autoLike.py     # Main script
├── likebtn.png     # Reference image of the Facebook Like button (used for matching)
└── Assets/
    └── demo.mp4    # Demo video of the script in action
```

## Setup

Install the required packages:

```bash
pip install pyautogui
pip install opencv-python
```

## Usage

1. Open `autoLike.py` and set the target profile on the `webbrowser.open(...)` line
   (line 5) to the profile whose posts you want to like.
2. Optionally change `no_of_posts` to control how many posts get liked.
3. Run the script:

   ```bash
   python autoLike.py
   ```

The script will open the profile in your browser and begin liking posts. Keep the browser
window in the foreground so the Like button stays visible on screen for image matching.

### Notes & Tips

- The included `likebtn.png` is matched against your screen. If your screen resolution,
  zoom level, or Facebook's theme differs, you may need to recapture `likebtn.png` to match
  how the Like button looks on your display.
- `confidence=.5` in the script controls how strict the image match is and requires
  `opencv-python` to be installed.

## Disclaimer

This project was made for fun/learning as a desktop-automation experiment. Automating
interactions on Facebook may violate its Terms of Service. Use responsibly and at your own
risk.
