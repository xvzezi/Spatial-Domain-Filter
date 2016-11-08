from SpatialDomain.tool import Tool
from PIL import Image

def main():
    # 打开图片
    img = Image.open('filters.png')
    gray = img.convert('L')
    grayBytes = gray.tobytes()

    # make it to 2D-list
    grayList = Tool.bytesToList(grayBytes, gray.width, gray.height)

    # 中位数 5x5
    median = Tool.doMedian(grayList, 5)
    gray.frombytes(bytes(median))
    gray.save('median5.png')

    # 中位数 11x11
    median = Tool.doMedian(grayList, 11)
    gray.frombytes(bytes(median))
    gray.save('median11.png')

    # 均值 5x5
    meanFilter = Tool.genMean(5)
    mean = Tool.dofilter(grayList, meanFilter)
    gray.frombytes(bytes(mean))
    gray.save('mean5.png')

    # 均值 11x11
    meanFilter = Tool.genMean(11)
    mean = Tool.dofilter(grayList, meanFilter)
    gray.frombytes(bytes(mean))
    gray.save('mean11.png')

    # 高斯滤波 5x5 sigma = 0.5
    gaussFilter = Tool.genGauss(sigma=0.5)
    gauss = Tool.dofilter(grayList, gaussFilter)
    gray.frombytes(bytes(gauss))
    gray.save('gauss0.5_5.png')

    # 高斯滤波 5x5 sigma = 3
    gaussFilter = Tool.genGauss(sigma=3)
    gauss = Tool.dofilter(grayList, gaussFilter)
    gray.frombytes(bytes(gauss))
    gray.save('gauss3_5.png')


    # 高斯滤波 11x11 sigma = 3
    gaussFilter = Tool.genGauss(sigma=3, side=11)
    gauss = Tool.dofilter(grayList, gaussFilter)
    gray.frombytes(bytes(gauss))
    gray.save('gauss3_11.png')


main()