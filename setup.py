from setuptools import setup

setup(
    name = "nishimasu18",
    version = ".1",
    author = "Ben Holmes",
    author_email = "ben@coolship.io",
    license = "MIT",
    keywords = "zlab",
    url = "http://github.com/coolship/nishimasu18",
    install_requires=['google-cloud-dataflow',"oauth2client<4.0.0","flask"],
    packages=['']
)

