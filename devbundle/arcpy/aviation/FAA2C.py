# Generated documentation for module arcpy.aviation


class FAA2C(object):
    """
    Generates an obstruction identification surface (OIS) for helipads based on specifications from FAA Advisory Circular 150/5390-2C.
    """

    @property
    def description(self) -> str:
        return """

        FAA2C_aviation(input_fato_features, target_ois_features, surface_classification, {surface_shape}, {approach_bearing}, {in_flightpath_features}, {helipad_elevation}, {custom_json_file})

        Generates an obstruction identification surface (OIS) for helipads
        based on specifications from FAA Advisory Circular 150/5390-2C.

     INPUTS:
      input_fato_features (Feature Layer):
          The input Final Approach and Takeoff (FATO) features.
      target_ois_features (Feature Layer):
          The target polygon or multipatch feature layer containing the OIS.
      surface_classification (String):
          Specifies the classification type of the FATO
          surface.NON_PRIOR_PERMISSION_REQUIRED_FACILITIES-These are publically
          available helipads for general use by pilots. This is the
          default.PRIOR_PERMISSION_REQUIRED_FACILITIES-These are heliports used
          exclusively by the owner and individuals authorized by the owner to
          use the facility.
      surface_shape {String}:
          Specifies the shape of the take off or approach
          surface.STRAIGHT_SURFACE-The take off or approach surface is straight.
          This is
          the default.CURVED_SURFACE-The take off or approach surface is curved.
      approach_bearing {Double}:
          The absolute bearing that an approaching aircraft will travel along
          the surface. A value of 0 will align the surface to true north. The
          default is 0.
      in_flightpath_features {Feature Layer}:
          The polyline flight path features that the curved surface will follow.
      helipad_elevation {Double}:
          The elevation of the highest point of the helipad. The value must be
          in the vertical coordinate system linear units of the target feature
          class. If no value is provided, the highest point of the
          input_fato_features parameter value will be used. The default is 0.
      custom_json_file {File}:
          The import configuration file, in JSON format, that creates the custom
          OIS.

        """