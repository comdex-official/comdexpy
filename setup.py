from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.4'
DESCRIPTION = 'Python SDK for interacting with comdex node'
LONG_DESCRIPTION = 'The comdexpy is a comprehensive Python library designed to provide developers with easy access to the Comdex blockchain and its ecosystem. This library enables developers to interact with the blockchain, query data, and perform various operations within the Comdex ecosystem.'

# Setting up
setup(
    name="comdexpy",
    version=VERSION,
    author="Comdex",
    author_email="<dheeraj@comdex.one>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[
        'asn1crypto==1.5.1',
        'base58==2.1.1',
        'bech32==1.2.0',
        'betterproto==2.0.0b5',
        'bip32==3.4',
        'certifi==2022.12.7',
        'cffi==1.15.1',
        'charset-normalizer==3.1.0',
        'coincurve==18.0.0',
        'ecdsa==0.18.0',
        'ECPy==1.2.5',
        'future==0.18.3',
        'grpcio==1.53.0',
        'grpcio-tools==1.53.0',
        'grpclib==0.4.3',
        'h2==4.1.0',
        'hidapi==0.13.1',
        'hpack==4.0.0',
        'hyperframe==6.0.1',
        'idna==3.4',
        'ledgerblue==0.1.46',
        'libusb1==3.0.0',
        'mnemonic==0.20',
        'multidict==6.0.4',
        'ndeflib==0.3.3',
        'nfcpy==1.0.4',
        'Pillow==9.5.0',
        'protobuf==4.22.3',
        'pycparser==2.21',
        'pycryptodomex==3.17',
        'pyDes==2.0.1',
        'pyelftools==0.29',
        'pyserial==3.5',
        'python-dateutil==2.8.2',
        'python-u2flib-host==3.0.3',
        'requests==2.28.2',
        'six==1.16.0',
        'stringcase==1.2.0',
        'urllib3==1.26.15',
        'websocket-client==1.5.1',
    ],
    keywords=['python', 'comdex', 'comdex sdk', 'comdexpy', 'pycomdex', 'comdex python sdk'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)