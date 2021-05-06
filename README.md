# matatika-meltano-report-converter

## Branches
### Main
- Output current 'unversioned' dataset yaml
- More specific about cleaning up output metadata. (Sometimes too specific for the more generic meltano reports).

### datasetv0.2
- Output v0.2 of the dataset yaml.
- As specific about cleaning up output metadata as the main version.

### test-generic-verson
- Output current 'unversioned' dataset yaml
- No specific filtering for metadata. Returns it all leading to some very large metadata structures in some cases. (Seems the only way to get some generic meltano reports to convert and work though).

