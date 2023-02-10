from io import open
from setuptools import find_packages, setup
from footprint import __version__ as version

setup(
    name='footprint-py',
    version=f'v{version}',
    url='https://github.com/Frikallo/footprint',
    license='Apache',
    author='Noah Kay',
    author_email='noahkay13@gmail.com',
    description='A python OSINT tool to discover and analyze the digital footprint of a targets email or username across millions of sites.',
    long_description=''.join(open('README.md', encoding='utf-8').readlines()),
    long_description_content_type='text/markdown',
    keywords=['cli', 'email', 'osint'],
    packages=find_packages(include=['footprint', 'footprint.*']),
    install_requires=['halo==0.0.31', 'email-validator==1.3.0', 'dnspython==2.3.0', 'pyfiglet==0.8.post1', 'termcolor==2.2.0', 'requests==2.28.2'],
    python_requires='>=3.6',
    include_package_data=True,
    package_data={'': ['data/*.blocklist']},
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
    ],
    entry_points={
        'console_scripts': [
            'footprint=footprint.__main__:run'
        ],
    },
)