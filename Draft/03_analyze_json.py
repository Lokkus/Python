import json


def analyse_json(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        count = 0
        for key, val in data.items():
            print(key)
            count += 1
        print(count)


def sessions_difference(mongo_json, found_splits):
    temp_list1 = []
    temp_list2 = []
    with open(mongo_json, 'r') as mongo_splits, open(found_splits, 'r') as splits_after_bct:
        splits_from_mongo = json.load(mongo_splits)
        mongo_set = {''.join(path.split('/')[-1]).rstrip() for session, paths in splits_from_mongo.items() for path in
                     paths}
        found_set = {''.join(path.split('/')[-1]).rstrip() for path in splits_after_bct}

        difference_set = mongo_set - found_set
        print('txt')


def create_file_with_irods_paths_as_input_for_copy_script_to_srr(found_splits_after_bct, read_splits_from_mongo,
                                                                 copy_to_srr):
    temp_list = []
    temp_dict = {}
    counter = 0
    json_list = ['JSON-F_20210511_A520_133h_FOT_NJ3_CW08_BLR', 'JSON-F_20210513_A530_133h_FOT_NJ3_CW08_BLR',
                 'JSON-F_20210515_A540_133h_FOT_NJ3_CW08_BLR']
    main_part = '/HPCC/PLKRA-PROJECTS/BMW-SRR5/9-Upload/ADCAM_UPLOAD/BCT/'
    with open(found_splits_after_bct, 'r') as found_splits, \
            open(read_splits_from_mongo, 'r') as read_splits_from_mongo_json, \
            open(copy_to_srr, 'w') as output_file:
        mongo_splits = json.load(read_splits_from_mongo_json)
        found_splits_names_set = {''.join(path.split('/')[-1]).rstrip() for path in found_splits}
        found_splits.seek(0)
        for mf4 in found_splits:
            mf4 = mf4.rstrip()
            get_part_of_path = mf4.split('/')[-3:]
            temp_dict[get_part_of_path[-1]] = get_part_of_path
        for session, paths in mongo_splits.items():
            for path in paths:
                path = path.rstrip()
                get_mf4_name = ''.join(path.split('/')[-1])
                if get_mf4_name in found_splits_names_set:
                    for json_name in json_list:
                        get_json_name = '_'.join([pos for pos in path.split('/') if json_name in pos][0].split('_')[1:])
                        if get_json_name:
                            break
                    if get_mf4_name in temp_dict:
                        temp_dict[get_mf4_name].insert(0, get_json_name)

        found_splits.seek(0)
        for path in found_splits:
            path = path.rstrip()
            first_part = path.replace('net/8k3/e0fs01/irods', 'HPCC')
            get_mf4_name = ''.join(path.split('/')[-1])
            if get_mf4_name in temp_dict:
                second_part = main_part + '/'.join(temp_dict[get_mf4_name])
                temp_list.append(first_part + ':' + second_part)
        print('t')
        for path in temp_list:
            output_file.write(path + '\n')


if __name__ == '__main__':
    # analyse_json(r'C:\Users\kubicmar\AppData\Local\Temp\Mxt211\RemoteFiles\198274_4_29\Splits_read_from_mongo1500.json')
    # sessions_difference(r'C:\Work\01_Projekty\02_Aptiv_DRT\LCA\Tests\Splits_read_from_mongo.json',
    #                     r'C:\Work\01_Projekty\02_Aptiv_DRT\LCA\Tests\20211006_1032_Found_splits_after_bct.txt')

    create_file_with_irods_paths_as_input_for_copy_script_to_srr(
        r'C:\Work\01_Projekty\02_Aptiv_DRT\LCA\Tests\copy\20210906_1639_found_splits_after_bct.txt',
        r'C:\Work\01_Projekty\02_Aptiv_DRT\LCA\Tests\copy\all_generated_splits.json',
        r'C:\Work\01_Projekty\02_Aptiv_DRT\LCA\Tests\copy\copy_to_srr_2.txt')
