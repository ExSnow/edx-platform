from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'certificates.tests.test_create_fake_cert')

from lms.djangoapps.certificates.tests.test_create_fake_cert import *
