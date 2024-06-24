# Generated documentation for module arcpy.aviation


class ICAOAnnex15(object):
    """
    Creates obstruction identification surfaces (OIS) based on the ICAO Annex 15 specification (Areas 2a, 2b, and 2c). These surfaces assist in determining the height restriction or removal of obstacles that pose a hazard to air navigation in and around an aerodrome. This tool creates surfaces as a polygon or multipatch features.
    """

    @property
    def description(self) -> str:
        return """

        ICAOAnnex15_aviation(in_features, target, {highend_clear_way_length}, {lowend_clear_way_length}, {custom_json_file}, {airport_control_point_feature_class})

        Creates obstruction identification surfaces (OIS) based on the ICAO
        Annex 15 specification (Areas 2a, 2b, and 2c). These surfaces assist
        in determining the height restriction or removal of obstacles that
        pose a hazard to air navigation in and around an aerodrome. This tool
        creates surfaces as a polygon or multipatch features.

     INPUTS:
      in_features (Feature Layer):
          The input runway dataset. The feature class must be z-enabled and
          contain polylines.
      target (Feature Layer):
          The target feature class that will contain the generated OIS.
      highend_clear_way_length {Double}:
          The length of the area at the high end of the runway. The unit of
          measurement is based on the input runway features.
      lowend_clear_way_length {Double}:
          The length of the area at the low end of the runway. The unit of
          measurement is based on the input runway features.
      custom_json_file {File}:
          The import configuration, in JSON format, that will be used to create
          the custom OIS.
      airport_control_point_feature_class {Feature Layer}:
          Supplies x-, y-, and z-geometry for displaced threshold features. If
          displaced thresholds are included, surfaces will be constructed based
          on their x-, y-, and z-geometry instead of their corresponding runway
          feature endpoint.

        """