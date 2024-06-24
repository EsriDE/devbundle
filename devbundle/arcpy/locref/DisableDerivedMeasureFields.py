# Generated documentation for module arcpy.locref


class DisableDerivedMeasureFields(object):
    """
    Disables fields that store the derived network route ID, route name, and measure fields.
    """

    @property
    def description(self) -> str:
        return """

        DisableDerivedMeasureFields_locref(in_feature_class)

        Disables fields that store the derived network route ID, route name,
        and measure fields.

     INPUTS:
      in_feature_class (Feature Layer):
          An existing event feature class or feature layer that is registered to
          an LRS.

        """