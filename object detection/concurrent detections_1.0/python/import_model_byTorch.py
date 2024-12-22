import torch

# Đường dẫn đến file trọng số của mô hình
path_to_weights = r'C:\Program Files (x86)\ZED SDK\samples\object detection\custom detector\python\pytorch_yolov8\yolov8s_custom.pt'

# Tải mô hình từ kho lưu trữ
model = torch.hub.load('ultralytics/yolov8', 'custom', path=path_to_weights, source='local')


# Đường dẫn đến hình ảnh cần dự đoán
img = "D:\TPM\ML_Yolov_eight\Yolo_env2.0\code"

# Thực hiện dự đoán
results = model(img)

# Hiển thị kết quả dự đoán
results.show()

# In ra các bounding box và nhãn
print(results.pandas().xyxy[0])  # Bounding boxes, scores, and labels

