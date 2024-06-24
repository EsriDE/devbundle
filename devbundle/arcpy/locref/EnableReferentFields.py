# Generated documentation for module arcpy.locref


class EnableReferentFields(object):
    """
    Enables or modifies the referent fields so that you can manage referent information for the registered LRS event.
    """

    @property
    def description(self) -> str:
        return """

        EnableReferentFields_locref(in_feature_class, {from_referent_method_field}, {from_referent_location_field}, {from_referent_offset_field}, {to_referent_method_field}, {to_referent_location_field}, {to_referent_offset_field}, {offset_units})

        Enables or modifies the referent fields so that you can manage
        referent information for the registered LRS event.

     INPUTS:
      in_feature_class (Feature Layer):
          The feature class that will be used for the LRS event.
      from_referent_method_field {Field}:
          The From referent method field.
      from_referent_location_field {Field}:
          The From referent location field.
      from_referent_offset_field {Field}:
          The From referent offset field.
      to_referent_method_field {Field}:
          The To referent method field.
      to_referent_location_field {Field}:
          The To referent location field.
      to_referent_offset_field {Field}:
          The To referent offset field.
      offset_units {String}:
          Specifies the offset units that will be used.MILES-The unit of measure
          will be miles. This is the
          default.INCHES-The unit of measure will be inches.FEET-The unit of
          measure will be feet.YARDS-The unit of measure will be
          yards.NAUTICAL_MILES-The unit of measure will be nautical
          miles.INTFEET-The unit of measure will be international
          feet.MILLIMETERS-The unit of measure will be
          millimeters.CENTIMETERS-The unit of measure will be
          centimetersMETERS-The unit of measure will be meters.KILOMETERS-The
          unit of measure will be kilometers.DECIMETERS-The unit of measure will
          be decimeters.

        """