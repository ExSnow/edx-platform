from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'ccx.tests.test_models')

from lms.djangoapps.ccx.tests.test_models import *
