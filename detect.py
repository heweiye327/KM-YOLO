from ultralytics import YOLO

# Load the trained KM-YOLO model
model = YOLO('weights/best.pt')

# Sample image for inference
source = 'demo/sample.jpg'

# Run inference
model.predict(
    source=source,
    imgsz=640,
    conf=0.25,
    save=True
)
