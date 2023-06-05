import argparse
import logging
from nomoreoldfiles import file_manager

parser = argparse.ArgumentParser(
    prog='No more old files ...',
    description='This program removes old files. It requires a folder, and a number days',
)


def argument_setup():
    parser.add_argument(
        '-d',
        '--days',
        default=-1,
        required=True,
        type=int,
        help='The number of days. Files older than this number of days will be removed.'
    )

    parser.add_argument(
        '-f',
        '--folder',
        required=True,
        type=str,
        help='The folder in which files will be removed.'
    )

    parser.add_argument(
        '-r',
        '--recursive',
        action='store_true',
        required=False,
        help='If used, the files in sub-folders will also be removed.'
    )

    parser.add_argument(
        '-s',
        '--simulation',
        action='store_true',
        required=False,
        help='If used, the code will list the files but will not delete them.'
    )


def logging_setup():
    logging.basicConfig(
        format='%(levelname)s:%(asctime)s:%(message)s',
        level=logging.DEBUG
    )


def execute():
    args = parser.parse_args()
    file_manager.remove_old_files(args.folder, args.days, args.recursive, args.simulation)


if __name__ == "__main__":
    logging_setup()
    logging.info('Script starting.')
    argument_setup()
    execute()
    logging.info('Script completed.')
