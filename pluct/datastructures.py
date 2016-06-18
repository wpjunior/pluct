# -*- coding: utf-8 -*-

try:
    from UserDict import IterableUserDict
except ImportError:
    try:
        from collections import IterableUserDict  # noqa
    except ImportError:
        from collections import UserDict as IterableUserDict  # noqa


try:
    from UserList import UserList
except ImportError:
    from collections import UserList  # noqa
