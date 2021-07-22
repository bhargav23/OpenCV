# Pythono3 code to rename multiple 
# files in a directory or folder
  
# importing os module
import os
  
# Function to rename multiple files
def main():
    path = '/content/drive/MyDrive/Data/dowloads/'
    t = 600;
    for count, filename in enumerate(os.listdir(path)):
      if t+1<10:
          dst ="image00000" + str(t+1) + ".jpg"
      elif t+1<100:
          dst ="image0000" + str(t+1) + ".jpg"
      elif t+1<1000:
          dst ="image000" + str(t+1) + ".jpg"
      elif t+1<10000:
          dst ="image00" + str(t+1) + ".jpg"
      elif t+1<100000:
          dst ="image0" + str(t+1) + ".jpg"
      else:
          dst ="image" + str(t+1) + ".jpg"
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
