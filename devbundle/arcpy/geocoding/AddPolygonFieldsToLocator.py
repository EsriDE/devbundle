# Generated documentation for module arcpy.geocoding


class AddPolygonFieldsToLocator(object):
    """
    Adds custom output fields from a polygon layer to an existing locator stored locally.
    """

    @property
    def description(self) -> str:
        return """

        AddPolygonFieldsToLocator_geocoding(in_locator, polygon_features, polygon_output_fields;polygon_output_fields...)

        Adds custom output fields from a polygon layer to an existing locator
        stored locally.

     INPUTS:
      in_locator (Address Locator):
          The locator (.loc file) where the fields will be added.The locator
          cannot be a composite locator or a geocode service,
          including services from ArcGIS Enterprise or ArcGIS Online. You must
          add the polygon fields to the participating locators of a composite
          locator before publishing the locator as a geocode service.
      polygon_features (Feature Layer):
          The feature class containing the fields that will be added to the
          in_locator parameter value (fields will be appended to all geocoding
          output).
      polygon_output_fields (Value Table):
          The fields from the polygon feature class that will be appended to the
          locator.Provide the field or field alias from the polygon_features
          parameter
          value, and the default field name will be used as the field name that
          is added to the locator. The default field name can be overwritten.
          The fields or name values provided for this parameter will define the
          names of the output fields from the polygon_features parameter value
          that will be returned in the geocode result. If the fields from the
          polygon features have aliases, the field alias will be used as the
          Name value.Polygon Field(s)-The fields from the polygon_features
          parameter value
          that will be added to the locator.Name-The name of the custom output
          field that will appear in the
          geocode results and locator properties.

        """