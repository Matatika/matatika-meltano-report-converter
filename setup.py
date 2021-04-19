from setuptools import find_packages, setup

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
    install_requires=[
          'pyyaml==5.4.1',
          'meltano'
    ],
    packages=['matatika_meltano_report_converter'],
    include_package_data=True,
)
