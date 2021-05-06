# matatika-meltano-report-converter
The `matatika-meltano-report-converter` is designed to be used as a custom uility within a meltano project.

It takes advantage of the meltano helper functions to create the metadata and sql query for the converted dataset.

## Branches
### Main
- Output v0.2 of the dataset yaml.
- More specific about cleaning up output metadata. (Sometimes too specific for the more generic meltano reports).

### test-generic-verson
- Output current 'unversioned' dataset yaml
- No specific filtering for metadata. Returns it all leading to some very large metadata structures in some cases. (Seems the only way to get some generic meltano reports to convert and work though).

# How To Use
## Installing

Initially you will need to either git clone this repositiory and install it to metlano from your system or you will need to have a custom discovery.yaml file that adds this utility as recognised by meltano by default.

### Local Installation and Use

1. `git clone` this repository to a location on your system.
2. In your terminal, move inside your meltano project's base directory.
3. Run `meltano add --custom utility matatika-meltano-report-converter`
4. You will be taken through a series of prompts fill in each as such:
    - (namespace) - Press Enter (empty = default value)
    - (pip_url) - Enter the location of your git cloned version of this repo. For me its `-e ../matatika-meltano-report-converter`
    - (executable) - Press Enter (empty = default value)
5. Make sure you have the reports you want to convert in `\analyze\reports\`
6. Run `meltano invoke matatika-meltano-report-converter`
7. The output converted yaml files will be placed in a directory called `converted_reports` at the base level of your meltano project.

![matatikareportconverterinstallexample](https://user-images.githubusercontent.com/34437496/117323235-9eeb3f00-ae86-11eb-83d3-2e47cca03552.png)

Its best to move your converted reports out to a different directory, as if you every invoke the converter again it will overwrite any changes to files still inside `converted_reports`.
