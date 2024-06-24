# Generated documentation for module arcpy.geocoding


class RebuildAddressLocator(object):
    """
    Rebuilds an address locator to update the locator with the current reference data. Because a locator contains a snapshot of the reference data when it was created, it will not geocode addresses with the updated data when the geometry and attributes of the reference data are changed. To geocode addresses with the current version of the reference data, the locator must be rebuilt to update the changes in the locator.
    """

    @property
    def description(self) -> str:
        return """

        RebuildAddressLocator_geocoding(in_address_locator)

        Rebuilds an address locator to update the locator with the current
        reference data. Because a locator contains a snapshot of the reference
        data when it was created, it will not geocode addresses with the
        updated data when the geometry and attributes of the reference data
        are changed. To geocode addresses with the current version of the
        reference data, the locator must be rebuilt to update the changes in
        the locator.

     INPUTS:
      in_address_locator (Address Locator):
          The address locator that will be rebuilt.

        """