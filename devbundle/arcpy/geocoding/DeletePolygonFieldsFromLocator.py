# Generated documentation for module arcpy.geocoding


class DeletePolygonFieldsFromLocator(object):
    """
    Deletes all polygon fields from a locator that were added using the Add Polygon Fields To Locator tool.
    """

    @property
    def description(self) -> str:
        return """

        DeletePolygonFieldsFromLocator_geocoding(in_locator)

        Deletes all polygon fields from a locator that were added using the
        Add Polygon Fields To Locator tool.

     INPUTS:
      in_locator (Address Locator):
          The locator (.loc file) containing the fields to be deleted.Composite
          locators, locators published as a geocode service, and
          locators that do not contain a polygon layer are not supported.

        """