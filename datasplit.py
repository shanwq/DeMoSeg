import random
import csv
import os
import shutil
import numpy as np

path = r'H:\Brain_Vessel_Seg\Xiehe_MRA\image'
pat_list = os.listdir(path)
k=0
random.seed(3407)

'Li_Bo_23', 'WAN_SI_49', 'YIN_FANG_YUAN_58', 'MA_REN_YING_30', 'ZHANG_ZI_QIU_71'

all_length = list(np.arange(77))

test_id = sorted(random.sample(all_length, 9))
print(test_id)
for i in test_id:
    if i in [23, 49, 58, 30, 71]:
        print('!!!!',i)
    all_length.remove(i)
print(all_length, len(all_length))

# val_id = sorted(random.sample(all_length, 16))

quit()
for i in range(77):
    if i in [23, 49, 58, 30, 71]:
        continue
    idx = '{:04d}'.format(i)
    
        


quit()
for pat in pat_list:
    oripat = pat
    pat = '{:04d}'.format(k) + '_' + pat
    new_path = r'H:\Brain_Vessel_Seg\Xiehe_MRA\re_id_image'
    new_id = os.path.join(new_path, pat)
    print(new_id)
    ori_img = os.path.join(path, oripat)
    # shutil.copy(ori_img, new_id)
    
    ori_label = os.listdir(r'H:\Brain_Vessel_Seg\Xiehe_MRA\label')[k]
    ori_labelfile = os.path.join(r'H:\Brain_Vessel_Seg\Xiehe_MRA\label', ori_label)
    new_label_path = r'H:\Brain_Vessel_Seg\Xiehe_MRA\re_id_label'
    new_label_a = '{:04d}'.format(k) + '_' + ori_label
    new_label = os.path.join(r'H:\Brain_Vessel_Seg\Xiehe_MRA\re_id_label', new_label_a)
    # shutil.copy(ori_img, new_id)
    # shutil.copy(ori_labelfile, new_label)
    with open(r'H:\Brain_Vessel_Seg\Xiehe_MRA\name_id.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        print('{:04d}'.format(k))
        writer.writerow([k, oripat])
        csv_file.close()
    k = k+1
    # img_list = os.listdir(path + '%s'%pat)
    # for img in img_list:
    #     if '2Flair' in img:
    #         img_new = img.replace('2Flair_N4Corrected', '')
    #         os.rename(path + '%s/'%pat + img, path + '%s/'%pat + img_new)
    #     else:
    #         img_new = img.replace('N4Corrected_', '')
    #         os.rename(path + '%s/'%pat + img, path + '%s/'%pat + img_new)
    # label_TC = '/memory/shanwenqi/Private_data/Re_id_N4_Resam/%s/'%pat + '%s_T1ce_label.nii.gz'%pat
    # label_WT = '/memory/shanwenqi/Private_data/Re_id_N4_Resam/%s/'%pat + '%s_Flair_label.nii.gz'%pat
    # new_label_TC = label_TC.replace('Re_id_N4_Resam', 'Re_id_Resam_N4_Bias_Corrected')
    # new_label_WT = label_WT.replace('Re_id_N4_Resam', 'Re_id_Resam_N4_Bias_Corrected')
    # shutil.copy(label_TC, new_label_TC)
    # shutil.copy(label_WT, new_label_WT)
    
    # quit()
# quit()
