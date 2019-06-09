# -*- coding: utf-8 -*-

import importlib.abc
import importlib.util
import sys

###############################################################################
# See: importlib.machinery.PathFinder

class ImpFxxkPathFinder(importlib.abc.MetaPathFinder):

    pass


###############################################################################
# See: importlib.machinery.FileFinder


class ImpFxxkFileFinder(importlib.abc.PathEntryFinder):

    pass


###############################################################################
# See: importlib.machinery.SourceFileLoader


class ImpFxxkSourceLoader(importlib.abc.SourceLoader):

    pass


###############################################################################
# Setting up impfxxk.

# Setting up loader details.
loader_details = (ImpFxxkSourceLoader,
                  importlib.machinery.SOURCE_SUFFIXES)

# Setting up a meta path finder.
sys.meta_path.append(ImpFxxkPathFinder())

# Setting up a path entry finder.
sys.path_hooks.append(ImpFxxkFileFinder.path_hook(loader_details))

# Setting up __main__.__spec__
__main__ = sys.modules['__main__']
if __main__.__spec__ is None:
    __main__.__spec__ = importlib.util.spec_from_loader(__main__.__name__, ImpFxxkPathFinder,
                                                        origin=__main__.__file__)
