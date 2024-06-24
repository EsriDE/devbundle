# Generated documentation for module arcpy.ca


class FeatureTo3DByTime(object):
    """
    Creates a 3D feature class using date values from input features.
    """

    @property
    def description(self) -> str:
        return """

        FeatureTo3DByTime_ca(in_features, out_feature_class, date_field, {time_z_unit}, {base_z}, {base_date})

        Creates a 3D feature class using date values from input features.

     INPUTS:
      in_features (Feature Layer):
          The features used to create 3D features.
      date_field (Field):
          A date field from the input that will be used to calculate the
          extrusion of the feature..
      time_z_unit {Time Unit}:
          The time interval and unit that will be represented by one vertical
          linear unit in the output feature class.For example, if the output
          feature class has a vertical coordinate
          system based in meters and this parameter has a value of 1 second, the
          resulting feature class will have features extruded in which 1 meter
          of elevation is equal to 1 second of time.
      base_z {Long}:
          The base z-value from which the output feature will start the
          extrusion.
      base_date {Date}:
          The date and time on which the time extrusion will be based.When no
          value is specified, the minimum date value of the input will
          be used.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output z-enabled feature class.

        """