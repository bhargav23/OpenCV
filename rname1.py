# Pythono3 code to rename multiple 
# files in a directory or folder
  
# importing os module
import os
  
# Function to rename multiple files
def main():
    path = '/content/drive/MyDrive/Data/BirdData/bgimages/'
    t = 1;
    for count, filename in enumerate(os.listdir(path)):
      if(count<9):
        dst ="bg000" + str(t) + ".jpg"
      elif(count<99):
        dst ="bg00" + str(t) + ".jpg"
      elif(count<999):
        dst ="bg0" + str(t) + ".jpg"
      src = path + filename
      dst =path+ dst
      # rename() function will
      # rename all the files
      os.rename(src, dst)
      t = t +1
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()
