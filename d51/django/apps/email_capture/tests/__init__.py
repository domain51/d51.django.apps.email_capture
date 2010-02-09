import pkg_resources
pkg_resources.declare_namespace(__name__)

from d51.django.apps.email_capture.tests.managers import *
from d51.django.apps.email_capture.tests.models import *
from d51.django.apps.email_capture.tests.views import *

