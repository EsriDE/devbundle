# Generated documentation for module arcpy.geocoding


class ClipLocator(object):
    """
    Clips a locator based on an area of interest or extent and creates a locator with a smaller extent and size.
    """

    @property
    def description(self) -> str:
        return """

        ClipLocator_geocoding(in_locator, out_locator, {area_of_interest}, {extent})

        Clips a locator based on an area of interest or extent and creates a
        locator with a smaller extent and size.

     INPUTS:
      in_locator (Address Locator):
          The locator (.loc file) that will be clipped.Geocode services or
          composite locators that contain geocode services,
          including services from ArcGIS Enterprise or ArcGIS Online, as
          participating locators are not supported. If the service is a
          participating locator in a composite locator it will not be clipped.
      area_of_interest {Feature Layer}:
          The polygon layer that defines an area of interest that will be used
          to clip the locator.This parameter overrides the extent parameter.
      extent {Extent}:
          Specifies the extent that will be used to clip the locator.DISPLAY-The
          extent will be equal to the visible display.Layer name-The
          extent of the specified layer will be used.Extent object-The extent of
          the specified object will be used.Space delimited string of
          coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.

     OUTPUTS:
      out_locator (Address Locator):
          The clipped output locator (.loc file).

        """