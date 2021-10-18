import json

def check_difference(all_generated_splits, found_splits_after_bct):
    output_dict = {}
    temp_list = []
    with open(all_generated_splits, 'r') as generated_splits, open(found_splits_after_bct, 'r') as found_splits:
        read_splits_from_json = json.load(generated_splits)

        set_from_generated_splits = {''.join(path.split('/')[-1]).rstrip() for session, list_of_paths in read_splits_from_json.items() for path in list_of_paths}
        set_from_found_splits = {''.join(path.split('/')[-1]).rstrip() for path in found_splits}

        set_difference = set_from_generated_splits - set_from_found_splits

        print(f'Len set_from_generated_splits {len(set_from_generated_splits)}')
        print(f'Len set_from_found_splits {len(set_from_found_splits)}')
        print(f'Len set_from_found_splits {len(set_difference)}')
        if set_difference:
            for session, list_of_splits in read_splits_from_json.items():
                for split in list_of_splits:
                    for mf4_name in set_difference:
                        if mf4_name in split:
                            if session not in output_dict:
                                output_dict[session] = []
                            temp_list.append(split)
                            break
                if temp_list:
                    output_dict[session] = sorted(temp_list)
                    temp_list = []


        print('a')



if __name__ == '__main__':
    check_difference(r'C:\Work\01_Projekty\02_Aptiv_DRT\LCA\Tests\all_generated_splits.json',
                     r'C:\Work\01_Projekty\02_Aptiv_DRT\LCA\Tests\20210915_1153_found_splits_after_bct.txt')