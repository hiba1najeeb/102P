import os
import shutil

from_dir = "C:/Users/user/Downloads/102 pro"
to_dir = "C:/Users/user/Desktop/DocumentFiles"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)

    if extension == '':
        continue
    if extension in ['.gif','.png','.jpeg','.jpg','.jfif']:
        path1 = from_dir+'/'+file_name
        path2 = to_dir+'/'+"Image"
        path3 =to_dir+'/'+"Image"+'/'+file_name
        if os.path.exists(path2):
            print("moving"+file_name+"...........")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving"+file_name+"...........")
            shutil.move(path1,path3)


   
    
