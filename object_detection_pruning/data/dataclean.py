import os

#for i in range(0,3000):
#    os.rename("train/dog."+str(i)+".jpg","train/train/dog"+str(i)+".jpg")
#    os.rename("train/cat."+str(i)+".jpg","train/train/cat"+str(i)+".jpg")
#for i in range(3000,3500):
#    os.rename("train/dog."+str(i)+".jpg","train/test/dog"+str(i)+".jpg")
#    os.rename("train/cat."+str(i)+".jpg","train/test/cat"+str(i)+".jpg")
for i in range(0,3000):

    print("train/dog."+str(i)+".jpg")
    os.rename("train/dog."+str(i)+".jpg", "train/train/dog/dog"+str(i)+".jpg")
    os.rename("train/cat."+str(i)+".jpg", "train/train/cat/cat"+str(i)+".jpg")

for i in range(3000,3500):
    os.rename("train/dog."+str(i)+".jpg","train/test/dog/dog"+str(i)+".jpg")
    os.rename("train/cat."+str(i)+".jpg","train/test/cat/cat"+str(i)+".jpg")

