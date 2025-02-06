# Token Detection Model

This repository provides a framework to train a custom object detection model for recognizing various Solana tokens using Apple's CreateML.

## Repository Structure

- **Annotations/**: Contains annotation files exported from RectLabel.
- **Generated/**: Output directory for the exported CreateML JSON file and trained CoreML model.
- **Tokens/**: Contains the download script and subdirectories for each token with their respective images.
- **TokenDetector.mlproj**: CreateML project file for training the object detection model.

## Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **icrawler**: Install using `pip install icrawler`.
- **RectLabel Pro**: Available on the Mac App Store for image annotation.
- **CreateML**: Comes with Xcode - ensure you have the latest version installed.

## Instructions

### Step 1: Download Token Images

Run the `download.py` script inside the Tokens directory to fetch token images:

```
./download.py "solana token" "SOL" --max_num 100
```

- **Search Query**: Search query for the token (e.g., "Solana token")
- **Folder Name**: Folder name for images (e.g., "SOL")

### Step 2: Annotate Images with RectLabel Pro

1. Open RectLabel Pro
2. Open images folder and annotations folder
    - Set images folder to `Tokens` directory
    - Set annotations folder to `Annotations` directory
3. Draw bounding boxes around tokens and label them
4. Export CreateML JSON file to `Generated` directory
    - Make sure `Split to train/val/text folders` is checked

### Step 3: Train the Model with CreateML

1. Open `TokenDetector.mlproj`
2. Create a new Model Source and version it accordingly (e.g v1, v2, v3, etc.)
3. Select `train` for the training data
4. Press `Train` to start training the model

### Step 4: Save the Trained Model

1. Go to `Output` tab after training completes
2. Click `Get` to save the `.mlmodel` file to the `Generated` directory
