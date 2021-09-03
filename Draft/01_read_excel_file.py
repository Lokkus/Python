import pandas as pd

def read_file(file):
    with open(file, 'r') as f:
        for path in f:
            print(''.join(path.split('/')[-1]), end='')

if __name__ == '__main__':
    read_file(r'C:\Work\01_Projekty\02_Aptiv_DRT\LCA\Tasks\01_Postprocessing_verification_for_video_decoded_files\list_of_non_exising_avi_files_2.txt')