import pandas

from util.Reader import read_event, sample_dis, sample_dis_dul, read_sample2
from util.drawPicture import draw_fixation, draw_multi_fiaxtion, draw_fixation1, draw_rawpoint, draw_fixation2
from util.generateAoi import genterate_aoi
import numpy as np

# def a(path="Experiment098_hcy_5_005 Samples.txt"):
#     return [[[area1], [area2]], img_path]
#     a = []
#     sample = {'img':'asds', 'area':[[x, y], [x, y]]}
#     a.append(sample)


def generate_area(file):
    data = sample_dis(file)
    tmp = 0
    F = []
    sample = {'img': 0, 'area': 0}
    area = []
    for i in range(data.shape[0]):
        # 获取mark
        mark = data.loc[i, 'Mark']
        if tmp == mark:
            x = data.loc[i, 'Location X']
            y = data.loc[i, 'Location Y']
            dur = data.loc[i, 'Duration']
            backgroundImg = data.loc[i, 'Image Path']
            F.append([x, y, dur])
        else:
            F = np.array(F)
            # 根据注视点生成注视区域
            feature = genterate_aoi(F, 65)
            if len(feature) > 1:
                print(len(feature))
            sample['img'] = backgroundImg
            sample['area'] = np.array(feature)
            area.append({'area': np.array(feature), 'img': backgroundImg})
            F = []
            tmp = mark
            # 把tmp!=mark的存储下来
            x = data.loc[i, 'Location X']
            y = data.loc[i, 'Location Y']
            dur = data.loc[i, 'Duration']
            backgroundImg = data.loc[i, 'Image Path']
            F.append([x, y, dur])

    F = np.array(F)
    feature = genterate_aoi(F, 65)
    sample['img'] = backgroundImg
    sample['area'] = np.array(feature)
    area.append(sample)

    return area




if __name__ == '__main__':
    name = ["Experiment098_hcy_5_005 Samples.txt",
            "Experiment098_hcy_6_006 Samples.txt"]
    for i in range(2):
        # eventFile = f"data/2022.12.11/{name[i]}"
        sampleFile = f"data/2022.12.12/{name[i]}"
        # df1 = read_event(eventFile)
        # df2 = sample_dis(sampleFile)
        # # df2 = read_sample2(sampleFile)
        # imgPath = f"image/20221212/hcy{i+5}/"
        # print("imgPath", imgPath)
        # # draw_rawpoint(df2, imgPath)
        # draw_fixation2(df2, imgPath)
        # # draw_fixation1(df2, imgPath)
        # # j += 1
        print(generate_area(sampleFile))


