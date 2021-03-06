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
        image_name = image
        if '@3x' in image:
            image_name = image.replace("@3x", "")
        # 打开3倍图
        im = Image.open(image)
        (w,h) = im.size

        # 生成三倍图
        size = (w,h)
        im.thumbnail(size)
        im.save(path_3x + '/' + image_name, 'png')

        # 生成二倍图
        size = (w/3*2,h/3*2)
        im.thumbnail(size)
        im.save(path_2x + '/' + image_name, 'png')

        # 生成一倍图
        size = (w/3,h/3)
        im.thumbnail(size)
        im.save(path_1x + '/' + image_name, 'png')
        im.close

if __name__ == '__main__':
    main()
    print("done")