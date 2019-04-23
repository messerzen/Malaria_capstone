import os


def rename_files(src_path, dst_path, frmt, dataset=False, label=False,
                 checker=True):
    """ This function rename a filename and save in a speficic directory.
    =======
    Params:
        - src_path: Source File Path
        - dst_path: Destination File path
        - dataset: String input ('train' / 'test' / 'valid)'.
                    If None, the folder name of file path is used.
                    It's necessary pre structured the folders.
                    Ex. '../train/label01'
                    Dataset = 'train'
        - label: String input. If None, the folder name of file path is used.
                    It's necessary pre structured the folders.
                    Ex. '../train/label01'
                    label = 'label01'
        - checker: If True, only print the new filename
                   If False, apply the rename function
                   (create the files in dst_path)
    """

    if not dataset:
        dataset = src_path.split('/')[-2]

    if not label:
        label = src_path.split('/')[-1]

    file_num = 0

    total_num_files = len(str(len(os.listdir(src_path))))
    num_digits = total_num_files - 1
    for filename in os.listdir(src_path):
        file_num += 1
        num_zeros = '0' * (num_digits)
        tot_str = len(str(num_zeros)) + len(str(file_num))
        if tot_str > total_num_files:
            num_digits -= 1
        number_name = '0' * (num_digits) + str(file_num)
        target_name = f'{number_name}_' + dataset + f'_{label}' + f'.{frmt}'

        if checker:
            print(f'Actual filename: {filename}')
            print(f'Target name: {target_name} \n')

        if checker == False:
            src_path = src_path
            old_name = src_path + '/' + filename

            dst_path = dst_path
            new_name = dst_path + '/' + target_name

            os.rename(old_name, new_name)
