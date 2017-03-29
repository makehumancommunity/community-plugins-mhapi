# Assets

These are calls related to reading, parsing and manipulating assets.

## openAssetFile(path, strip = False)

This opens an asset file and returns an [assetInfo](assetInfo.md) dict. If strip is set to True, the raw data is excluded from the dict. 

## writeAssetFile(assetInfo, createBackup = True)

This (over)writes the asset file named in the assetInfo's "absolute path" key. If createBackup is set to True, any pre-existing file will be backed up to it's former name + ".bak"


