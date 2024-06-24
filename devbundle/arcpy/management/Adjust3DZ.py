# Generated documentation for module arcpy.management


class Adjust3DZ(object):
    """
    Modifies z-values of 3D features.
    """

    @property
    def description(self) -> str:
        return """

        Adjust3DZ_management(in_features, {reverse_sign}, {adjust_value}, {from_units}, {to_units})

        Modifies z-values of 3D features.

     INPUTS:
      in_features (Feature Layer):
          The 3D features with the z-values that will be modified.
      reverse_sign {String}:
          Specifies whether features will be inverted along the
          z-axis.REVERSE-The sign of z-values will be inverted causing the
          feature to
          flip upside down.NO_REVERSE-The sign of z-values will not be inverted;
          it will be
          maintained. This is the default.
      adjust_value {Double / Field}:
          A numeric value or field from the input features that will be used to
          adjust the z of each vertex in the input features. A positive value
          will shift the feature higher, while a negative number will shift it
          lower along the z-axis.
      from_units {String}:
          Specifies the existing units of the z-values. This parameter is used
          in conjunction with the to_units parameter.MILLIMETERS-The units will
          be millimeters.CENTIMETERS-The units will
          be centimeters.METERS-The units will be meters.INCHES-The units will
          be inches.FEET-The units will be feet.YARDS-The units will be
          yards.FATHOMS-The units will be fathoms.
      to_units {String}:
          Specifies the units that existing z-values will be converted
          to.MILLIMETERS-The units will be millimeters.CENTIMETERS-The units
          will
          be centimeters.METERS-The units will be meters.INCHES-The units will
          be inches.FEET-The units will be feet.YARDS-The units will be
          yards.FATHOMS-The units will be fathoms.

        """