from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('cms.djangoapps', 'course_creators.tests')

from cms.djangoapps.course_creators.tests import *
