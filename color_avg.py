import cv2 as cv
import matplotlib.pyplot as plt
import os
from PIL import Image
base_path = os.path.dirname(os.path.abspath(__file__))
images_total = 0
try_number = 0 # Tries file numbers to write csv to until it gets unoccupied one
done = False

while not(done):
    output_filename = os.path.join(base_path,'truth_'+str(try_number)+'.csv')
    if os.path.exists(output_filename):
        try_number += 1
    else:
        done = True

with open(output_filename, 'w') as f:
    for my_path, my_subdirs, my_files in os.walk(base_path):
        for my_file in my_files:
            if (my_file.endswith(".jpg")):
                    images_total += 1
                    
                    temp_string = os.path.join(my_path,my_file)
                    f.write(temp_string[len(base_path)+1:]) # Strip the base path off to allow sharing of data files
                    f.write(",")
                    
                    in_image = plt.imread(os.path.join(my_path,my_file))
                    
                    plt.figure(1)
                    plt.clf()
                    plt.imshow(in_image)
                    
                    if (False):
                        #color_dist = color_distance(in_image,np.array([0,1,0]))
                        color_dist = color_correlation(in_image,np.array([0,1,0]))
        
                        plt.figure(2)
                        plt.clf()
                        plt.imshow(color_dist,cmap='hot')
                    
                    plt.draw()
                    plt.show()
                    plt.pause(0.1)
    
                    # BIG ASSUMPTION - WE FORCE THE USER OF THIS TOOL TO FIND 5 BOXES
                    # BIG ASSUMPTION #2 - THE BOXES ARE FOUND LEFT TO RIGHT
                    # BIG ASSUMPTION #3 - first click on a box is upper left (UL) and the second is lower right (LR)
                    # BIG ASSUMPTION #4 - clicked box spans all of the detectable energy for a reflected target
                    
                    v = plt.ginput(10,timeout=0)
                    for index in range(10):
                        f.write(str(v[index])+",")
                    f.write("\n")
    
    # EXAMPLE OUTPUT LINE:
    # 220in/debug5_exposure-10.png,(306.1321361922536, 430.16001447233117),(309.78830407129533, 432.44511939673225),(315.27255588985804, 428.7889515176905),(322.5848916479416, 431.0740564420916),(330.8112693757855, 427.8749095479301),(338.58062611874936, 431.5310774269718),(346.3499828617131, 427.8749095479301),(353.2052976349165, 430.6170354572114),(359.60359142323955, 430.16001447233117),(364.1738012720418, 433.35916136649274),
    # PROCESSING PROGRAM NEEDS TO BE ABLE TO READ AND PROCESS THIS INFO
    
    print("Total images:  "+str(images_total))

