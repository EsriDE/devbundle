# Generated documentation for module arcpy.aviation


class ICAOAnnex14Heliports(object):
    """
    Generates obstruction identification surfaces (OIS) for heliports based on ICAO Annex 14 Volume II specifications.
    """

    @property
    def description(self) -> str:
        return """

        ICAOAnnex14Heliports_aviation(input_safety_area_features, target_ois_features, surface_classification, operation_type, {rotor_diameter}, {clearway_length}, {surface_shape}, {approach_bearing}, {in_flightpath_features}, {heliport_elevation}, {custom_json_file})

        Generates obstruction identification surfaces (OIS) for heliports
        based on ICAO Annex 14 Volume II specifications.

     INPUTS:
      input_safety_area_features (Feature Layer):
          The input safety area around which the OIS will be generated.
      target_ois_features (Feature Layer):
          The target feature class that will contain the generated OIS.
      surface_classification (String):
          Specifies the slope design category that will be used for the
          OIS.CATEGORY_A-Rotor aircraft operated with performance class 1 will
          be
          used.CATEGORY_B-Rotor aircraft operated with performance class 3 will
          be
          used.CATEGORY_C-Rotor aircraft operated with performance class 2 will
          be
          used.
      operation_type (String):
          Specifies the time when normal flight operations
          occur.DAY_OPERATION-Normal flight operations occur during the day.
          This is
          the default.NIGHT_OPERATION-Normal flight operations occur during the
          night.
      rotor_diameter {Double}:
          The rotor diameter, in meters, of aircraft using the heliport. The
          default is 16.5.
      clearway_length {Double}:
          The length of the clearway. The unit of measurement for the clearway
          depends on the input_safety_area_features parameter value.
      surface_shape {String}:
          Specifies the shape of the take off or approach
          surface.STRAIGHT_SURFACE-The take off climb or approach surface is
          straight.
          This is the default.CURVED_SURFACE-The take off climb or approach
          surface is curved.
      approach_bearing {Double}:
          The absolute bearing that an approaching aircraft will travel along
          the surface. A value of 0 will align the surface to true north. The
          default value is 0.
      in_flightpath_features {Feature Layer}:
          The polyline flight path features that the curved surface will follow.
      heliport_elevation {Double}:
          The elevation of the highest point of the heliport. The value must be
          in the vertical coordinate system linear units of the target feature
          class. If no value is provided, the highest point of the
          input_safety_area_features parameter value will be used. The default
          is 0.
      custom_json_file {File}:
          The import configuration, in JSON format, that will be used to create
          the custom OIS.

        """