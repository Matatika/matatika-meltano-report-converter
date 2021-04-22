import os
from setuptools import find_packages, setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='matatika-meltano-report-converter',
    version='1.0',
    description='A meltano custom utility to conver meltano reports into matatika yaml datasets',
    author='DanielPDWalker',
    url='https://www.matatika.com/',
    py_modules=['matatika_meltano_report_converter'],
    entry_points='''
        [console_scripts]
        matatika-meltano-report-converter=matatika_meltano_report_converter:matatika_convert_reports
    ''',
    install_requires=required,
    packages=['matatika_meltano_report_converter'],
    include_package_data=True,
)
