def generate_test():
    sbv_sw_dict = {'2074': 'A520_F-JSON', '2076': 'A530_F-JSON'}
    path = '/net/8k3/e0fs01/irods/PLKRA-PROJECTS/ADCAM/2-Sim/' \
           'CONTI_RENAMED/20210525_1630/2074/20210205T222841_000000_BR92434/' \
           '20210205T222841_000000_BR92434_ADCAM_BN_FASETH/' \
           '20210205T222933_20210205T222943_000000_BR92434_BN_FASETH.MF4'

    json_path = r'/data/users/sid_adcam1/DB/JSON/JSONF/JSON-F_20210401_A520_580h_FOT_NJ3_CW09_FFM_correction.json'

    generate_list_of_renamed_paths(sbv_sw_dict['2074'], path, json_path)

def generate_list_of_renamed_paths(sbv, renamed_path_from_db, json_path):

    begining_path = '/net/8k3/e0fs01/irods/PLKRA-PROJECTS/ADCAM/2-Sim/CONTI_RENAMED/'
    j = json_path.split('/')[-1].split('.')[0]+'/'
    j = '/ADCAM_'+j

    x = '/'.join(renamed_path_from_db.split('/')[-4:])
    path = begining_path+sbv+j+x
    print(path)

def renamed_file():
    with open('input_filelist.txt', 'r') as input_file:
        with open('output_renamed_file.txt', 'w') as output_file:
            for path in input_file:
                output_file.write(path.replace('net/8k3/e0fs01/irods', 'HPCC'))




if __name__ == '__main__':
    #generate_test()
    renamed_file()
