class Config(object):
    TESTONG=False
    DEBUG=False


class Development(Config):
    DEBUG=True

class TESTING(Config):
    TESTING=True

config = {
    "development":Development,
    "testing":TESTING
}