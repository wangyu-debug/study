from PIL import Image
from torch.utils.tensorboard import SummaryWriter

from torchvision import transforms

img_path = "B:\\python_torch\\data\\train\\ants_image\\0013035.jpg"
img = Image.open(img_path)
print(img)  ##<PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=768x512 at 0x2395C944188>

writer = SummaryWriter("logs")

##如何使用transforms
tensor_trans = transforms.ToTensor()
tensor_img = tensor_trans(img)
writer.add_image("tensor_img",tensor_img)
writer.close()
#print(tensor_img) ##tensor([[[ ]]])

