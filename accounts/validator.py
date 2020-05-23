from django.core import validators


class validator:
    def username(username):
        if not username.endswith('@gmail.com'):
            raise validators.ValidationError('Domain name should be @gmail.com')

    def mobile(mobile):
        if not mobile.isdigit():
            raise validators.ValidationError("Enter correct mobile number")

        if not len(mobile)==10:
            raise validators.ValidationError('Moblie number is not correct')

    def name(name):
        if any(c.isdigit() for c in name):
            raise validators.ValidationError('Enter correct name')