# Generated documentation for module arcpy.management


class ConsolidateLocator(object):
    """
    Consolidate a locator or composite locator by copying all locators into a single folder.
    """

    @property
    def description(self) -> str:
        return """

        ConsolidateLocator_management(in_locator, output_folder, {copy_arcsde_locator})

        Consolidate a locator or composite locator by copying all locators
        into a single folder.

     INPUTS:
      in_locator (Address Locator):
          The input locator or composite locator that will be consolidated.
      copy_arcsde_locator {Boolean}:
          This parameter has no effect in ArcGIS Pro. It remains only to support
          backward compatibility.

     OUTPUTS:
      output_folder (Folder):
          The output folder that will contain the consolidated locator or
          composite locator with its participating locators.If the specified
          folder does not exist, a new folder will be created.

        """