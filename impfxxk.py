# -*- coding: utf-8 -*-

import importlib.abc
import importlib.machinery
import importlib.util
import sys

from importlib._bootstrap_external import _path_isdir

###############################################################################
# See: importlib.machinery.PathFinder importlib.abc.MetaPathFinder

class ImpFxxkMetaPathFinder(importlib.machinery.PathFinder):

    @classmethod
    def find_spec(cls, fullname, path=None, target=None):
        print(fullname, path, target)
        return super().find_spec(cls, fullname, path, target)


###############################################################################
# See: importlib.machinery.FileFinder importlib.abc.PathEntryFinder


class ImpFxxkPathEntryFinder(importlib.machinery.FileFinder):

    @classmethod
    def path_hook(cls, *loader_details):
        def path_hook_for_FileFinder(path):
            """Path hook for importlib.machinery.FileFinder."""
            print(path)
            if not _path_isdir(path):
                raise ImportError('only directories are supported', path=path)
            return cls(path, *loader_details)

        return path_hook_for_FileFinder


###############################################################################
# See: importlib.machinery.SourceFileLoader importlib.abc.SourceLoader


class ImpFxxkSourceLoader(importlib.machinery.SourceFileLoader):

    pass


###############################################################################
# Setting up impfxxk.

# Setting up loader details.
loader_details = (ImpFxxkSourceLoader,
                  importlib.machinery.SOURCE_SUFFIXES)

# Setting up a meta path finder.
sys.meta_path.append(ImpFxxkMetaPathFinder())

# Setting up a path entry finder.
sys.path_hooks.append(ImpFxxkPathEntryFinder.path_hook(loader_details))

# Setting up __main__.__spec__
__main__ = sys.modules['__main__']
if __main__.__spec__ is None:
    __main__.__spec__ = importlib.util.spec_from_loader(__main__.__name__,
                                                        ImpFxxkMetaPathFinder(),
                                                        origin=__main__.__file__ if hasattr(__main__, '__file__') else None)
