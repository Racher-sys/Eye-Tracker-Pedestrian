import pandas

from util.Reader import read_event, sample_dis, sample_dis_dul, read_sample2
from util.drawPicture import draw_fixation, draw_multi_fiaxtion, draw_fixation1, draw_rawpoint, draw_fixation2

if __name__ == '__main__':
    name = ["Experiment098_hcy_5_005 Samples.txt",
            "Experiment098_hcy_6_006 Samples.txt"]
    for i in range(2):
        # eventFile = f"data/2022.12.11/{name[i]}"
        sampleFile = f"data/2022.12.12/{name[i]}"
        # df1 = read_event(eventFile)
        df2 = sample_dis(sampleFile)
        # df2 = read_sample2(sampleFile)
        imgPath = f"image/20221212/hcy{i+5}/"
        print("imgPath", imgPath)
        # draw_rawpoint(df2, imgPath)
        draw_fixation2(df2, imgPath)
        # draw_fixation1(df2, imgPath)
        # j += 1
