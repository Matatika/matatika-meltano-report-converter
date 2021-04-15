import setuptools

setuptools.setup(
    name="matatika-meltano-report-converter-DanielPDWalker", # Replace with your own username
    version="0.0.1",
    author="DanielPDWalker",
    author_email="dwalker@matatika.com",
    description="Matatika's meltano report converter",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)