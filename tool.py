import math

class Tool:

    @classmethod
    def bytesToList(cls, b_list, width, height):
        # amount
        amount = width * height
        # output
        output = [[0 for i in range(width)] for i in range(height)]

        for i in range(0, amount):
            y = math.floor(i / width)
            x = i % width
            output[y][x] = b_list[i]

        return output

    @classmethod
    def doMedian(cls, source, side):
        s_height = len(source)
        s_width = len(source[0])

        output = [[0 for i in range(s_width)] for i in range(s_height)]

        #
        for y in range(0, s_height):
            for x in range(0, s_width):
                hash = []
                x_height = math.floor(side/2) - x
                y_height = math.floor(side/2) - y

                for i in range(y - math.floor(side / 2), y + math.floor(side / 2)):
                    if i < 0 or i >= s_height:
                        continue
                    for j in range(x - math.floor(side / 2), x + math.floor(side / 2)):
                        if j < 0 or j >= s_width:
                            continue
                        hash.append(source[i][j])
                hash = sorted(hash)
                output[y][x] = hash[math.floor(side / 2)]

        # return
        re = [0] * s_height * s_width
        for y in range(0, s_height):
            for x in range(0, s_width):
                re[y * s_width + x] = output[y][x]
        return re

    @classmethod
    def dofilter(cls, source, filter):
        # source & filter
        s_height = len(source)
        s_width = len(source[0])
        f_height = len(filter)
        f_width = len(filter[0])
        total = 0
        for i in range(0, f_height):
            total += sum(filter[i])
        output = [[0 for i in range(s_width)] for i in range(s_height)]

        #
        half_h = math.floor(f_height / 2)
        half_w = math.floor(f_width / 2)
        for y in range(0, s_height):
            for x in range(0, s_width):
                hash = 0
                x_height = half_w - x
                y_height = half_h - y

                for i in range(y - half_h, y + half_h + 1):
                    if i < 0 or i >= s_height:
                        continue
                    for j in range(x - half_w, x + half_w + 1):
                        if j < 0 or j >= s_width:
                            continue
                        hash += source[i][j] * filter[i + y_height][j + x_height]

                output[y][x] = math.floor(hash / total)

        # return
        re = [0] * s_height * s_width
        for y in range(0, s_height):
            for x in range(0, s_width):
                re[y * s_width + x] = output[y][x]
        return re

    @classmethod
    def genMean(cls, side = 5):
        output = [[1 for i in range(side)] for i in range(side)]
        return output

    @classmethod
    def genGauss(cls, side = 5, sigma = 1):
        sig2 = sigma * sigma

        step = 1
        s_y = - math.floor(side / 2) * step
        s_x = s_y
        output = [[0 for i in range(side)] for i in range(side)]

        y = s_y
        x = s_x
        for i in range(0, math.floor(side / 2) + 1):
            fac1 = - y * y / sig2
            for j in range(0, side):
                fac2 = - x * x / sig2
                output[i][j] = math.exp(fac1 + fac2)
                x += step
            y += step
            x = s_x

        for i in range(side - 1, math.floor(side / 2), -1):
            for j in range(0, side):
                output[i][j] = output[side - i - 1][j]

        fac = 1 / output[0][0]
        print(fac)
        for i in range(0, side):
            for j in range(0, side):
                output[i][j] = round(output[i][j] * fac)

        for i in range(0, side):
            print(output[i])

        return output

