# A Comprehensive Framework for Evaluating Deepfake Generators: Dataset, Metrics Performance, and Comparative Analysis
![My Photo](https://github.com/ICCVsupplementary/ICCV_2023/blob/main/protocol_final.png)

## Requirements
Before using the code and resources provided in this repository, ensure you have the following dependencies installed:
* Python (>= 3.6)
* OpenCV (cv2)
* NumPy (numpy)
* Pillow (PIL)
* trimesh
* pyrender

## Real Head dataset
Our dataset structure follows the format of the original FaceScape [1] dataset, ensuring compatibility with FaceScape's data organization, file naming conventions, and directory structure for consistency and ease of use. For more detailed information on the dataset attributes and their meanings, please refer to the FaceScape documentation.

## Synthesized Dataset of MetaHumans
In addition to the Real Head dataset, we offer an example of a synthesized dataset of MetaHumans. This dataset comprises six different characters sharing the same head pose and expression. You can access the dataset through the following link: 

https://synthesizedmetahuman.eurecom.fr/


[1] https://github.com/zhuhao-nju/facescape
