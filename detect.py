from ultralytics import YOLO
# 加载训练好的模型，改为自己的路径
model = YOLO('/root/autodl-tmp/ultralytics-yolo11and12/ultralytics-yolo11-main/runs/train/原版/weights/last.pt')  #修改为训练好的路径
source = '/root/001885_png.rf.775da828b2d2bf7fe3ba6b9b6bcac3ca.jpg' #修改为自己的图片路径及文件名
# 运行推理，并附加参数
model.predict(source, save=True)