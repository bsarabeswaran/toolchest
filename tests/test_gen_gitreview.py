from unittest import mock, TestCase

import toolchest.gen_gitreview


class test_generate_gitreview(TestCase):

    def test_gen_single_gitreview(self):
        mocked = mock.mock_open()
        path = "/tmp/testing_tmp"
        host = "random_host_str"
        host_port = "1234"
        project = "test_project"
        branch = "test_branch_name"
        remote = "test_remote"
        rebase = 0

        with mock.patch("toolchest.gen_gitreview.open", mocked, create=True):
            toolchest.gen_gitreview.generate_gitreview(path,
                                                       host,
                                                       host_port,
                                                       project,
                                                       branch,
                                                       remote,
                                                       rebase)

        # checks that we wrote to the right path
        mocked.assert_called_with(f'{path}/.gitreview', 'w')

        # collects the writes to the .gitreview file in order
        writes_in_order = [
            mock.call("[gerrit]\n"),
            mock.call("host=random_host_str\n"),
            mock.call("port=1234\n"),
            mock.call("project=test_project.git\n"),
            mock.call("defaultbranch=test_branch_name\n"),
            mock.call("defaultremote=test_remote\n"),
            mock.call("defaultrebase=0\n"),
        ]

        # checks if the above calls are called in order
        mocked.return_value.write.assert_has_calls(writes_in_order)

    def test_gen_single_default_rebase_gitreview(self):
        mocked = mock.mock_open()
        path = "/tmp/testing_tmp"
        host = "random_host_str"
        host_port = "1234"
        project = "test_project"
        branch = "test_branch_name"
        remote = "test_remote"

        with mock.patch("toolchest.gen_gitreview.open", mocked, create=True):
            toolchest.gen_gitreview.generate_gitreview(path,
                                                       host,
                                                       host_port,
                                                       project,
                                                       branch,
                                                       remote)

        # checks that we wrote to the right path
        mocked.assert_called_with(f'{path}/.gitreview', 'w')

        # collects the writes to the .gitreview file in order
        writes_in_order = [
            mock.call("[gerrit]\n"),
            mock.call("host=random_host_str\n"),
            mock.call("port=1234\n"),
            mock.call("project=test_project.git\n"),
            mock.call("defaultbranch=test_branch_name\n"),
            mock.call("defaultremote=test_remote\n"),
            mock.call("defaultrebase=1\n"),
        ]

        # checks if the above calls are called in order
        mocked.return_value.write.assert_has_calls(writes_in_order)
