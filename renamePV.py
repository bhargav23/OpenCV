# Pythono3 code to rename multiple 
# files in a directory or folder
  
# importing os module
import os
  
# Function to rename multiple files
def main():
    path = 'C:/Users/Bhargav/Downloads/Bus/New/'
    for count, filename in enumerate(os.listdir(path)):
        if count+1<10:
            dst ="image00000" + str(count+1) + ".jpg"
        elif count+1<100:
            dst ="image0000" + str(count+1) + ".jpg"
        elif count+1<1000:
            dst ="image000" + str(count+1) + ".jpg"
        elif count+1<10000:
            dst ="image00" + str(count+1) + ".jpg"
        elif count+1<100000:
            dst ="image0" + str(count+1) + ".jpg"
        else:
            dst ="image" + str(count+1) + ".jpg"
        
        src = path + filename
        dst =path+ dst
        
        # rename() function will
        # rename all the files
        os.rename(src, dst)
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()
