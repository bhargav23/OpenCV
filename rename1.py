# Pythono3 code to rename multiple 
# files in a directory or folder
  
# importing os module
import os
  
# Function to rename multiple files
def main():
    path = '/content/drive/MyDrive/Data/BirdData/foreground/'
    t = 1;
    for count, filename in enumerate(os.listdir(path)):
      if(t<10):
        dst ="image00" + str(t) + ".png"
      elif(t<100):
          dst ="image0" + str(t) + ".png"
      else: 
            dst ="image" + str(t) + ".png"
      src = path + filename
      dst =path+ dst
      # rename() function will
      # rename all the files
      os.rename(src, dst)
      t = t + 1
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()
