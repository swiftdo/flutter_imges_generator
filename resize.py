from PIL import Image
import os

def main():
    #文件夹下所有文件名
    list = os.listdir('.')
    #images收集图片名
    images = []
    for file in list:
        if file.endswith('.png') or file.endswith('.jpg'):
            images.append(file)


    image = images[0]

    path_1x = "assets/"
    if not os.path.exists(path_1x):
        os.makedirs(path_1x)

    path_2x = "assets/2x"
    if not os.path.exists(path_2x):
        os.makedirs(path_2x)

    path_3x = "assets/3x"
    if not os.path.exists(path_3x):
        os.makedirs(path_3x)

    for image in images:
        print(image)
        # 打开3倍图
        im = Image.open(image)
        (w,h) = im.size

        # 生成三倍图
        size = (w,h)
        im.thumbnail(size)
        im.save(path_3x + '/' + image, 'png')

        # 生成二倍图
        size = (w/3*2,h/3*2)
        im.thumbnail(size)
        im.save(path_2x + '/' + image, 'png')

        # 生成一倍图
#        os.remove("./" + image)
        size = (w/3,h/3)
        im.thumbnail(size)
        im.save(path_1x + '/' + image, 'png')
        im.close

if __name__ == '__main__':
    main()
    print("done")
    # 上面只定义函数，可共享于其他文件
    # from module2 import foo 或者 import module3 或者 import module3 as m3
    # 下面代码只在本文件夹可执行