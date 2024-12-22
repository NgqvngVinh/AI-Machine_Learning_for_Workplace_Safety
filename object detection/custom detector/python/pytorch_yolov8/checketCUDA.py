import torch
import torchvision
print(torch.__version__)  # Hiển thị phiên bản PyTorch
print(torch.version.cuda)  # Hiển thị phiên bản CUDA mà PyTorch được xây dựng với
print(torch.backends.cudnn.version())  # Hiển thị phiên bản CuDNN mà PyTorch được xây dựng với
print(torch.cuda.is_available())  # Kiểm tra xem PyTorch có thể sử dụng CUDA không
print(torch.cuda.device_count()) 
print(torch.cuda.get_device_name(0))
print(torchvision.__version__)