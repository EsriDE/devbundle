# Generated documentation for module arcpy.aviation


class FAA18B(object):
    """
    Creates obstruction identification surfaces (OIS) based on the FAA Advisory Circular 150/5300-18B specification. These OIS assist in the identification of possible hazards to air navigation and critical approach and departure obstructions within the vicinity of the airport and are used to support planning and design activities. The type, function, and dimension of a surface differ by its runway classification. This tool creates surfaces as polygon or multipatch features.
    """

    @property
    def description(self) -> str:
        return """

        FAA18B_aviation(in_features, target, runway_type, {highend_clear_way_length}, {lowend_clear_way_length}, {airport_elevation}, {include_merged_surface}, {custom_json_file}, {airport_control_point_feature_class})

        Creates obstruction identification surfaces (OIS) based on the FAA
        Advisory Circular 150/5300-18B specification. These OIS assist in the
        identification of possible hazards to air navigation and critical
        approach and departure obstructions within the vicinity of the airport
        and are used to support planning and design activities. The type,
        function, and dimension of a surface differ by its runway
        classification. This tool creates surfaces as polygon or multipatch
        features.

     INPUTS:
      in_features (Feature Layer):
          The input runway dataset. The feature class must be z-enabled and
          contain polylines.
      target (Feature Layer):
          The target feature class that will contain the generated OIS.
      runway_type (String):
          Specifies the runway classification for the in_features
          value.NON_VERTICAL_GUIDANCE_TYPE_1-A runway designed for visual
          maneuvers,
          nonvertically guided operations, and instrument departure
          procedures.NON_VERTICAL_GUIDANCE_TYPE_2-A specially prepared hard
          surface (SPHS)
          runway designed for visual maneuvers, nonvertically guided operations,
          and instrument departure procedures. SPHS runways have a primary
          surface that extends 200 feet beyond each end of the
          runway.VERTICAL_GUIDANCE-A runway that uses precision guidance systems
          to
          support aircraft approach and landing.
      highend_clear_way_length {Double}:
          The length of the area at the high end of the runway. The unit of
          measurement is based on the input runway features.
      lowend_clear_way_length {Double}:
          The length of the area at the low end of the runway. The unit of
          measurement is based on the input runway features.
      airport_elevation {Double}:
          The highest elevation on any of the runways of the airport.
          The value should be in the vertical coordinate system linear units of
          the target feature class. If no value is provided, the highest point
          from theparameter value will be used. Input Runway Features
      include_merged_surface {Boolean}:
          Specifies whether merged horizontal and conical surfaces will be
          included in the OIS in addition to the regular
          surfaces.INCLUDE_MERGED_SURFACE-Merged surfaces will be included in
          the OIS
          output. This is the default.NOT_INCLUDE_MERGED_SURFACE-Merged surfaces
          will not be included in the
          OIS output.
      custom_json_file {File}:
          The import configuration, in JSON format, that will be used to create
          the custom OIS.
      airport_control_point_feature_class {Feature Layer}:
          The point features containing anfeature, displaced threshold
          features, or both. Values provided for theparameter will take
          precedence over these point features. Airport ElevationAirport
          Elevation

        """