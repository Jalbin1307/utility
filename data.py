import os
import shutil

category = {}
dir_path = ""
src_path = ""

for cate in category:
    num = 0
    os.mkdir("dir_path/{}/".format(cate))
    for (path, dir, files) in os.walk(dir_path,"/{}/".format(cate)):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.jpg' or '.JPG':
                file = "%s/%s" % (path, filename)
                print(file)
                shutil.move(file, dir_path,"/{}/{}.jpg".format(cate, num))
                num+=1
