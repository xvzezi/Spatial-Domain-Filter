# Spatial Domain Filter
author : 许泽资 5140379068

## Instruction
 - 本例采用典型的滤镜框的实现处理方式。实现了包括中值、均值、高斯等在内的空间域滤波。
 - 本例支持生成均值滤波矩阵；支持自定义的高斯滤波矩阵
 - 高斯滤波矩阵的计算，采用计算一半，利用对称性填充一半的方式提升效率

## Result Analysis
 - 中值滤波。分别采用5x5，11x11的矩阵求中值，可以发现，最后的效果像是“团墨”的感觉，且矩阵越大，成团效应越明显，  
   矩阵取大时，模糊的感觉逐渐消失，最后应当会成为颜色块组成的图像。
 - 均值滤波。分别采用5x5，11x11的矩阵求均值，可以发现，模糊很明显，相比其他两种方式，均值的方式模糊度更高，  
   大矩阵就越来越模糊。
 - 高斯滤波。sigma = 0.5时，模糊效果几乎没有，但可以去除噪声，矩阵大小大于5时效果几乎无变化，这是由于sigma较小  
   ，峰顶较陡，所以扩大矩阵无益；sigma = 3时，有一定模糊效果。发现，高斯滤波要用于模糊的话，sigma取值要更大，  
   但这是会逼近均值滤波，不若直接采用均值滤波，无益。所以高斯滤波去除噪声是最好的选择。

## File Announcement
 - tool.py 所有的实现工具
 - spatial_domain.py 所有的实现代码
 - median5.png 中值5x5
 - median11.png 中值11x11
 - mean5.png 均值5x5
 - mean11.png 均值11x11
 - gauss0.5_5.png 高斯5x5 sigma=0.5
 - gauss3_5.png 高斯5x5 sigma=3
 - gauss3_11.png 高斯11x11 sigma=3
 - filters.png 原图

## Python Environment
```Python
python3.5
pip install Pillow
```

## Code Description
 - tool.py 
```python
class Tool:

    @classmethod
    def bytesToList(cls, b_list, width, height):
    '''
    将bytes转化为2D list
    '''

    @classmethod
    def doMedian(cls, source, side):
    '''
    对source(2D list) 做中值滤波，side指定矩阵大小
    '''

    @classmethod
    def dofilter(cls, source, filter):
    '''
    对source(2D list) 做filter(2D list)的滤波，filter的长宽应为奇数
    '''

    @classmethod
    def genMean(cls, side = 5):
    '''
    获取指定side的均值方矩阵(2D list)
    '''

    @classmethod
    def genGauss(cls, side = 5, sigma = 1):
    '''
    获取指定side，指定sigma的高斯方矩阵(2D list)
    '''

```
 - spatial_domain.py 
```python
 # 生成一系列想要的图片，见文件
```
