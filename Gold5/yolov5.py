import torch

if torch.cuda.is_available():    
    device = torch.device("cuda")
    print('There are %d GPU(s) available.' % torch.cuda.device_count())
    print('We will use the GPU:', torch.cuda.get_device_name(0))

else:
    print('No GPU available, using the CPU instead.')
    device = torch.device("cpu")

# 구글 드라이브에서 데이터 가져오기
from google.colab import drive
drive.mount('/content/drive')

from glob import glob

# train, test 이미지 경로 지정
train_img_list = glob('/content/drive/MyDrive/Colab Notebooks/Yolo/yolov5/hardhat/train/images/*.jpg')
test_img_list = glob('/content/drive/MyDrive/Colab Notebooks/Yolo/yolov5/hardhat/test/images/*.jpg')
print(len(train_img_list), len(test_img_list))

from sklearn.model_selection import train_test_split
import yaml

test_img_list, val_img_list = train_test_split(test_img_list, test_size=0.5, random_state=777) # test 셋 분리
print(len(train_img_list), len(test_img_list))

import yaml

# 각각 이미지 리스트 텍스트 파일에 넣어주기
with open('train.txt', 'w') as f:
    f.write('\n'.join(train_img_list) + '\n')

with open('test.txt', 'w') as f:
    f.write('\n'.join(test_img_list) + '\n')

with open('val.txt', 'w') as f:
    f.write('\n'.join(val_img_list) + '\n')

#customize iPython writefile so we can write variables
from IPython.core.magic import register_line_cell_magic

#yaml 수정 함수
@register_line_cell_magic
def writetemplate(line, cell):
    with open(line, 'w') as f:
        f.write(cell.format(**globals()))

import torch
from IPython.display import Image, clear_output

# num_classes에 class 개수 넣어주기
with open('data.yaml', 'r') as stream:
    num_classes = str(yaml.safe_load(stream)['nc'])

from keras.preprocessing import image
import matplotlib.pyplot as plt
from IPython.display import Image, display

# 결과 확인
Image(filename='runs/train/hardhat_results/results.png', width=1000)
Image(filename='runs/train/hardhat_results/train_batch0.jpg', width=1000)



