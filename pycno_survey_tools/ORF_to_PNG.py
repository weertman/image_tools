#%%
import rawpy
import imageio

import matplotlib.pyplot as plt

import cv2

import os
import glob

from datetime import datetime

from tqdm import tqdm
#%%
target_dir = r'E:\TG6_IMGS'
if os.path.exists(target_dir) != True:
    os.mkdir(target_dir)

path_imgs = glob.glob(r'F:\DCIM\100OLYMP\*.ORF')

name_ext = ''

show_imgs = True
img_ext = '.png'
#%%

n_doesnt_exist = 0
n_exist = 0
for path_img in path_imgs:
    c_time = str(os.path.getmtime(path_img)).split('.')[0]
    new_path_img = os.path.join(target_dir, name_ext +'_' + c_time + '_' + os.path.basename(path_img).split('.')[0]+img_ext)
    if os.path.exists(new_path_img) != True:
        n_doesnt_exist += 1
    else:
        n_exist += 1

print('out of a', n_doesnt_exist+n_exist, 'images', n_exist, 'have been transferred', n_doesnt_exist, 'need to be transferred')

#%%
#### Add get ctime code ####
pbar = tqdm(total = len(path_imgs), position=0, leave=True)
for path_img in path_imgs[0:]:
    c_time = str(os.path.getmtime(path_img)).split('.')[0]
    new_path_img = os.path.join(target_dir, name_ext +'_' + c_time + '_' + os.path.basename(path_img).split('.')[0]+img_ext)
    if os.path.exists(new_path_img) != True:
        with rawpy.imread(path_img) as raw:
            rgb = raw.postprocess()
            if show_imgs == True:
                fig, (ax) = plt.subplots(1,1,figsize=(10,10))
                ax.imshow(rgb)
                ax.axis('off')
                ax.set_title(new_path_img)
                plt.show(fig)
                plt.close(fig)
            cv2.imwrite(new_path_img, cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR))             
    pbar.update(n=1)
pbar.close()
