# Pythono3 code to rename multiple 
# files in a directory or folder
  
# importing os module
import os
  
# Function to rename multiple files
def main():
    path = 'C:/Users/Bhargav/Downloads/Bus/'
    for count, filename in enumerate(os.listdir(path)):
        dst ="img" + str(count) + ".jpg"
        src = path + filename
        dst =path+ dst
        # rename() function will
        # rename all the files
        os.rename(src, dst)
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()
