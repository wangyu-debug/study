from PIL import Image
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms


#2、为什么需要Tensor数据类型

img_path = "B:\\python_torch\\data\\train\\ants_image\\0013035.jpg"
img = Image.open(img_path)
print(img)  ##<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=768x512 at 0x2395C944188>

writer = SummaryWriter("logs")

##如何使用transforms
tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)
print(tensor_img)
writer.add_image("Tensor_img",tensor_img)

writer.close()
#print(tensor_img) ##tensor([[[ ]]])

