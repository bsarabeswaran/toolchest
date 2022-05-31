#!/usr/bin/env python
import os


def generate_gitreview(path, host, host_port, project,
                       def_branch, def_remote, rebase=1):

    '''
    Writes a new .gitreview file to the specified path with specified arguments
    Derived from patch_rebaser

    :param str path: path in which the .gitreview should be placed
    :param str host: Gerrit host
    :param str host_port: port of the Gerrit host
    :param str project: name of the project
    :param str def_branch: name of the Git branch
    :param str def_remote: name of the Git remote
    :param int rebase: if 0, then changes will not be rebased by default.
                       if 1, then changes will be rebased by default.
    '''

    with open(os.path.join(path, '.gitreview'), 'w') as fp:
        fp.write('[gerrit]\n')
        fp.write(f'host={host}\n')
        fp.write(f'port={host_port}\n')
        fp.write(f'project={project}.git\n')
        fp.write(f'defaultbranch={def_branch}\n')
        fp.write(f'defaultremote={def_remote}\n')
        fp.write(f'defaultrebase={rebase}\n')
