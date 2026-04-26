# KM-YOLO: A Novel Pedestrian Detection Model for Low-light Scenes

This repository provides the source code of KM-YOLO, an improved YOLO-based pedestrian detection model for low-light traffic scenes.

Low-light pedestrian detection is challenging because pedestrians often suffer from low contrast, weak texture information, blurred edges, partial occlusion, and complex background interference. To address these problems, KM-YOLO introduces the PKI module and the MAN module into the YOLO framework to enhance local texture extraction, multi-scale feature representation, and cross-layer feature aggregation.

The proposed model is evaluated on the low-light-enhanced KITTI dataset.

## Main Contributions

- The PKI module is introduced to enhance local texture extraction and multi-scale contextual feature representation under low-light conditions.
- The MAN module is used to strengthen multi-scale feature aggregation and key-region response.
- The proposed KM-YOLO model improves pedestrian detection performance for weak-texture, small-scale, and partially occluded targets in low-light traffic scenes.

## Project Structure

```text
KM-YOLO/
├── train.py                              # Training script
├── test.py                               # Validation and metric extraction script
├── detect.py                             # Inference script
├── data/
│   └── data.yaml                         # Dataset configuration file
├── ultralytics/
│   ├── cfg/
│   │   └── models/
│   │       └── 11/
│   │           └── C3K2-PKI+MAN.yaml     # Model configuration file
│   └── nn/
│       ├── tasks.py                      # Model parser and module registration
│       └── extra_modules/
│           └── block.py                  # PKI and MAN module implementation
└── README.md
```

## Dataset

The experiments are conducted on the low-light-enhanced KITTI dataset. The dataset contains typical traffic targets under low-light conditions, including cars, pedestrians, cyclists, trucks, vans, and other traffic-related categories.

The dataset configuration file is located at:

```text
data/data.yaml
```

The class names are defined as follows:

```yaml
names:
  0: Car
  1: Cyclist
  2: DontCare
  3: Misc
  4: Pedestrian
  5: Person_sitting
  6: Tram
  7: Truck
  8: Van
```

Please organize the dataset according to the following structure:

```text
data/
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/
```

Before training, please check whether the paths in `data/data.yaml` are consistent with your local dataset path.

## Installation

Clone this repository:

```bash
git clone https://github.com/heweiye327/KM-YOLO.git
cd KM-YOLO
```

Create a Python environment:

```bash
conda create -n kmyolo python=3.10 -y
conda activate kmyolo
```

Install the required packages:

```bash
pip install torch torchvision torchaudio
pip install opencv-python numpy pandas matplotlib scipy tqdm pyyaml prettytable
```

## Training

To train the proposed KM-YOLO model, run:

```bash
python train.py
```

The main training configuration is shown below:

```python
from ultralytics import YOLO

model = YOLO('ultralytics/cfg/models/11/C3K2-PKI+MAN.yaml')

model.train(
    data='data/data.yaml',
    imgsz=640,
    epochs=300,
    batch=32,
    optimizer='SGD',
    workers=4,
    project='runs/train',
    name='KM-YOLO'
)
```

The trained weights will be saved in:

```text
runs/train/KM-YOLO/weights/
```

## Validation

After training, modify the weight path in `test.py`:

```python
model_path = 'runs/train/KM-YOLO/weights/best.pt'
```

Then run:

```bash
python test.py
```

The validation script reports the following metrics:

- Precision
- Recall
- F1-score
- mAP@0.5
- mAP@0.75
- mAP@0.5:0.95
- Parameters
- GFLOPs
- FPS
- Model file size

## Inference

To perform inference on a single image, modify the model path and image path in `detect.py`:

```python
from ultralytics import YOLO

model = YOLO('runs/train/KM-YOLO/weights/best.pt')
source = 'path/to/test/image.jpg'

model.predict(source, save=True)
```

Then run:

```bash
python detect.py
```

The detection results will be saved in:

```text
runs/detect/predict/
```

## Experimental Results

The comparison results on the low-light-enhanced KITTI dataset are shown below.

| Method | Precision (%) | Recall (%) | mAP@0.5 (%) | mAP@0.5:0.95 (%) |
|---|---:|---:|---:|---:|
| YOLOv12 | 80.26 | 73.94 | 79.72 | 57.79 |
| YOLOv8 | 79.22 | 74.15 | 78.65 | 55.76 |
| YOLOv11 | 83.09 | 74.01 | 80.70 | 58.62 |
| YOLOv13 | 83.22 | 74.83 | 81.17 | 59.45 |
| KM-YOLO | 86.99 | 78.04 | 84.10 | 62.06 |

## Ablation Study

| Method | Precision (%) | Recall (%) | mAP@0.5 (%) | mAP@0.5:0.95 (%) |
|---|---:|---:|---:|---:|
| YOLOv12 | 80.18 | 73.98 | 79.71 | 57.81 |
| YOLOv12 + PKI | 83.95 | 76.79 | 81.92 | 59.57 |
| YOLOv12 + MAN | 86.03 | 78.55 | 83.94 | 61.58 |
| YOLOv12 + PKI + MAN | 86.99 | 78.04 | 84.10 | 62.06 |

## Visualization Results

Several representative low-light traffic images are selected for visual comparison. The red dashed ellipses indicate regions where the proposed method achieves more complete or more stable detection results.

```text
results/fig5_visualization.png
```

## Notes

The complete dataset and trained weight files are not included in this repository because of file size limitations. Please prepare the dataset locally and modify `data/data.yaml` according to your own path.

If trained weights are provided later, they can be placed in:

```text
runs/train/KM-YOLO/weights/
```

or released through GitHub Releases, Google Drive, Baidu Netdisk, or Hugging Face.

## Citation

If this project is helpful for your research, please cite or star this repository.
