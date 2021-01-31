import os

class files():
    imageNames = []
    root = os.getcwd() + "/imageSet/"
    def load_imageNames(self):  # scan working directory for images
        for dirName, subdirList, fileList in os.walk(self.root):
            for fname in fileList:
                if fname.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.webp')):
                    self.imageNames.append(fname)

    def get_imageName(self, i):  # getter for image name
        return self.imageNames[i]

    def get_arraySize(self):  # getter for array size
        return len(self.imageNames)

    def store_image(self, image, n):  # function that does the actual storing of images based off selection

        if n == 1:
            os.replace(self.root + image, self.root + "/folder1/" + image)

        elif n == 2:
            os.replace(self.root + image, self.root + "/folder2/" + image)


