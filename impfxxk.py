# -*- coding: utf-8 -*-

import importlib.machinery
import sys


class ImpFxxkPathFinder(importlib.machinery.PathFinder):

    @classmethod
    def find_spec(cls, fullname, path, target=None):
        print(fullname, path, target)
        super().find_spec(fullname, path, target)


class ImpFxxkFileFinder(importlib.machinery.FileFinder):

    def __init__(self, path, *loader_details):
        print(path, loader_details)
        super().__init__(path, *loader_details)

    def find_spec(self, fullname, target=None):
        print(fullname, target)
        super().find_spec(fullname, target)

    @classmethod
    def path_hook(cls, *loader_details):
        def path_hook_for_FileFinder(path):
            """Path hook for importlib.machinery.FileFinder."""
            print(path)
            if not importlib.machinery._path_isdir(path):
                raise ImportError('only directories are supported', path=path)
            return cls(path, *loader_details)

        return path_hook_for_FileFinder


loader_details = (importlib.machinery.SourceFileLoader,
                  importlib.machinery.SOURCE_SUFFIXES)

# register sys.meta_path
sys.meta_path.insert(0, ImpFxxkPathFinder())

# register sys.path_hooks
sys.path_hooks.insert(0, ImpFxxkFileFinder.path_hook(loader_details))

# clear out the internal cache
importlib.invalidate_caches()

# cleanup __main__ cache
# sys.modules.pop('__main__')
