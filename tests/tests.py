import tempfile
import unittest
import os
import time
from nomoreoldfiles import file_manager

class nomoreoldfiles(unittest.TestCase):

    def test_invalid_path(self):
        """
        When given an invdalid directory, the code should run but an empty list of files should be returned.
        :return:
        """
        # generate a temporary path that will be deleted for test.
        bad_dir = None
        with tempfile.TemporaryDirectory() as test_dir:
            bad_dir = test_dir

        files = file_manager.remove_old_files(bad_dir, 0)
        self.assertEqual(len(files), 0)

    def test_basic(self):
        """
        When given a directory with a single file, that single file should exist before the function remove_old_files is
        executed, and should not exist after its execution.
        :return:
        """
        with tempfile.TemporaryDirectory() as test_dir:
            temp_file_path = os.path.join(test_dir, 'test.txt')
            with open(temp_file_path, 'w') as temp_file:
                temp_file.write('Hello')
                temp_file.flush()

            self.assertEqual(os.path.exists(temp_file_path), True)
            time.sleep(1)
            files = file_manager.remove_old_files(test_dir, 0)
            self.assertEqual(len(files), 1)
            self.assertEqual(os.path.exists(temp_file_path), False)

    def test_basic_simulation(self):
        """
        When given a directory with a single file, that single file should exist before the function remove_old_files is
        executed, and should not exist after its execution. Execpt if we run in simulation mode. The file to remove
        should be listed but not removed.
        :return:
        """
        with tempfile.TemporaryDirectory() as test_dir:
            temp_file_path = os.path.join(test_dir, 'test.txt')
            with open(temp_file_path, 'w') as temp_file:
                temp_file.write('Hello')
                temp_file.flush()

            self.assertEqual(os.path.exists(temp_file_path), True)
            time.sleep(1)
            files = file_manager.remove_old_files(test_dir, 0, simulation=True)

            self.assertEqual(len(files), 1)
            self.assertEqual(os.path.exists(temp_file_path), True)

    def test_basic_recursion(self):
        """
        When given a directory with a subfolder, the script should remove the file in the main folder and its subfolder.
        :return:
        """
        with tempfile.TemporaryDirectory() as test_dir:
            temp_file_path = os.path.join(test_dir, 'test.txt')
            with open(temp_file_path, 'w') as temp_file:
                temp_file.write('Hello')
                temp_file.flush()

            temp_subdir_path = os.path.join(test_dir, 'subdir')
            os.mkdir(temp_subdir_path)
            temp_subdirfile_path = os.path.join(temp_subdir_path, 'test.txt')
            with open(temp_subdirfile_path, 'w') as temp_subdirfile:
                temp_subdirfile.write('Hello')
                temp_subdirfile.flush()

            self.assertEqual(os.path.exists(temp_file_path), True)
            time.sleep(1)
            files = file_manager.remove_old_files(test_dir, 0, recursive=True)
            self.assertEqual(len(files), 2)
            self.assertEqual(os.path.exists(temp_file_path), False)

    def test_invalid_days(self):
        with tempfile.TemporaryDirectory() as test_dir:
            self.assertRaises(
                ValueError,
                file_manager.remove_old_files,
                test_dir,
                -1,
                True,
                False
            )


if __name__ == '__main__':
    unittest.main()