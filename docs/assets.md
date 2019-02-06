# Assets

This namespace wraps all calls that are related to reading and managing assets.

## assetTitleToDirName(assetTitle)

Convert an asset title (as shown for example in a list) to a normalized file name

## getAssetTypes()

Returns a non-live list of known asset types

## getAssetLocation(assetTitle, assetType)

Get the full normal (user) path for an asset based on its title and type

## openAssetFile(path, strip = False)

Opens an asset file and returns a hash describing it

## writeAssetFile(assetInfo, createBackup = True)

This (over)writes the asset file named in the assetInfo's "absolute path" key. If createBackup is set to True, any pre-existing file will be backed up to it's former name + ".bak"

## materialToHash(material)

Convert a material object to a hash containing all its settings

## getAvailableSystemSkins()

Get a list with full paths to all system skins (the MHMAT files)

## getAvailableUserSkins()

Get a list with full paths to all user skins (the MHMAT files)

## getAvailableSystemHair()

Get a list with full paths to all system hair (the MHCLO files)

## getAvailableUserHair()

Get a list with full paths to all user hair (the MHCLO files)

## getAvailableSystemEyebrows()

Get a list with full paths to all system eyebrows (the MHCLO files)

## getAvailableUserEyebrows()

Get a list with full paths to all user eyebrows (the MHCLO files)

## getAvailableSystemEyelashes()

Get a list with full paths to all system eyelashes (the MHCLO files)

## getAvailableUserEyelashes()

Get a list with full paths to all user eyelashes (the MHCLO files)

## getAvailableSystemClothes()

Get a list with full paths to all system clothes (the MHCLO files)

## getAvailableUserClothes()

Get a list with full paths to all user clothes (the MHCLO files)

## equipHair(mhclofile)

Equip a MHCLO file with hair. This will automatically unequip previously equipped hair.

## unequipHair(mhclofile)

Unequip a MHCLO file with hair

## getEquippedHair()

Get the currently equipped hair, if any

## equipEyebrows(mhclofile)

Equip a MHCLO file with eyebrows. This will automatically unequip previously equipped eyebrows.

## unequipEyebrows(mhclofile)

Unequip a MHCLO file with eyebrows

## getEquippedEyebrows()

Get the currently equipped eyebrows, if any

## equipEyelashes(mhclofile)

Equip a MHCLO file with eyelashes. This will automatically unequip previously equipped eyelashes.

## unequipEyelashes(mhclofile)

Unequip a MHCLO file with eyelashes

## getEquippedEyelashes()

Get the currently equipped eyelashes, if any

## equipClothes(mhclofile)

Equip a MHCLO file with clothes

## unequipClothes(mhclofile)

Unequip a MHCLO file with clothes

## getEquippedClothes()

Get a list of all currently equipped clothes

## unequipAllClothes()

Unequip all clothes

