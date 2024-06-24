# Generated documentation for module arcpy.locref


class EnableDerivedMeasureFields(object):
    """
    Enables fields to store the derived route ID, derived route name, and derived measure fields for the specified LRS event feature class.
    """

    @property
    def description(self) -> str:
        return """

        EnableDerivedMeasureFields_locref(in_feature_class, {derived_route_id_field}, {derived_route_name_field}, {derived_from_measure_field}, {derived_to_measure_field})

        Enables fields to store the derived route ID, derived route name, and
        derived measure fields for the specified LRS event feature class.

     INPUTS:
      in_feature_class (Feature Layer):
          An existing event feature class or feature layer that is registered to
          an LRS.
      derived_route_id_field {Field}:
          The derived route ID field.
      derived_route_name_field {Field}:
          The derived route name field.
      derived_from_measure_field {Field}:
          The derived from measure field.
      derived_to_measure_field {Field}:
          The derived to measure field.

        """