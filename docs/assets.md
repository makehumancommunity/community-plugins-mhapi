# Assets

This namespace wraps all calls that are related to reading and managing assets.

## openAssetFile(path, strip = False)

Opens an asset file and returns a hash describing it

## writeAssetFile(assetInfo, createBackup = True)

This (over)writes the asset file named in the assetInfo's "absolute path" key. If createBackup is set to True, any pre-existing file will be backed up to it's former name + ".bak"

