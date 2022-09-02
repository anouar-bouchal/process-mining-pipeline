import os


def _file_exists(file_name):
    return os.path.isfile(os.path.join(os.getcwd(), file_name))


def log_records(dataframe, file_name):
    path = os.path.join(os.getcwd(), file_name)
    if _file_exists(file_name):
        dataframe.to_csv(path, mode='a', index=False, header=False)
    else:
        dataframe.to_csv(path)