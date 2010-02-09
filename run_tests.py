try:
    from d51.django.virtualenv.test_runner import run_tests
except ImportError:
    print "Please install d51.django.virtualenv.test_runner to run these tests"

def main():
    settings = {
        "INSTALLED_APPS": (
            "django.contrib.auth",
            "d51.django.apps.email_capture",
        ),
    }
    run_tests(settings, 'email_capture')

if __name__ == '__main__':
    main()
