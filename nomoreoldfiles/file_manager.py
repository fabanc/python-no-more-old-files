import datetime
import logging
import os
import pathlib

from datetime import timedelta


def get_file_or_folder_age(path):
    """
    Returns the time since epoch a file or folder has been created.
    :param path: The path to the folder or file for wich the timestamp will be created.
    :return: A timestamp in seconds since epoch when the file was updated.
    """

    # getting ctime of the file/folder
    # time will be in seconds
    ctime = os.stat(path).st_ctime

    # returning the time
    return ctime


def get_old_files(path, cutoff_date, recursive):
    """
    Returns a list of file that are older that the current date.
    :param path: The path used to look for old files.
    :param cutoff_date: The cutoff date. All the files that were last edited before that date will be returned.
    :param recursive: If true, the code will return files in subdirectories.
    :return: A list of files that were not edited after the cutoff date. The array will be empty if the path does not
    exist.
    """
    output = []
    # checking whether the file is present in path or not
    if not os.path.exists(path):
        logging.warning(f'Path {path} does not exist.')
    else:
        path_1 = pathlib.Path(path)
        # iterating over each and every folder and file in the path
        for root_folder, folders, files in os.walk(path):
            path_2 = pathlib.Path(root_folder)
            if not recursive and path_1.resolve() != path_2.resolve():
                continue

            for file in files:
                file_path = os.path.join(root_folder, file)
                file_seconds = get_file_or_folder_age(file_path)
                file_time = datetime.datetime.fromtimestamp(file_seconds)

                logging.debug(f'File path: {file_path} - Time: {file_time}')
                if file_time < cutoff_date:
                    output.append(file_path)

    return output


def remove_old_files(folder, days, recursive=False, simulation=False):
    logging.info(f'Folder: {folder}, Days: {days}, Recursive: {recursive}, Simulation: {simulation}')
    # Attribute validation
    if folder is None:
        raise ValueError('Folders cannot be null.')
    if days < 0:
        raise ValueError('Number of days must be equals or greater than 0')

    # Compute the cutoff date.
    current_date = datetime.datetime.now()
    delta = timedelta(
        days=days,
    )
    cutoff_date = current_date - delta
    logging.info(f'Cutoff date: {cutoff_date}')

    old_file = get_old_files(folder, cutoff_date, recursive)
    logging.info(f'Detected {len(old_file)} files to delete.')
    for file in old_file:
        if not simulation:
            os.remove(file)
    return
