from setuptools import find_packages, setup

setup(
    name='matatika-meltano-report-converter',
    version='0.1.0',
    py_modules=['matatika_meltano_report_converter'],
    entry_points='''
        [console_scripts]
        matatika-meltano-report-converter=matatika_meltano_report_converter:matatika_convert_reports
    ''',
    packages=['matatika_meltano_report_converter'],
    include_package_data=True,
    install_requires=[
          'pyyaml==5.4.1',
          'meltano'
    ],
)
