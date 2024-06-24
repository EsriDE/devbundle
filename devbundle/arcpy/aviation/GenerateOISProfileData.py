# Generated documentation for module arcpy.aviation


class GenerateOISProfileData(object):
    """
    Generates a JSON string that is stored in the PROFILEJSON field on the input Obstruction Identification Surface multipatch feature class that contains the data necessary to depict the terrain, runway, and OIS in the Terrain and Obstacle Profile layout element.
    """

    @property
    def description(self) -> str:
        return """

        GenerateOISProfileData_aviation(in_runway_features, in_dems;in_dems..., target_ois_features, {in_flightpath_features}, {sampling_distance}, {sample_profile_ois}, {sample_profile_runways})

        Generates a JSON string that is stored in the PROFILEJSON field on the
        input Obstruction Identification Surface multipatch feature class that
        contains the data necessary to depict the terrain, runway, and OIS in
        the Terrain and Obstacle Profile layout element.

     INPUTS:
      in_runway_features (Feature Layer):
          This is the input runway dataset. The feature class must be z-enabled
          and contain polylines.
      in_dems (Raster Layer):
          The DEMs covering the runways and their approach obstruction
          identification surfaces.
      target_ois_features (Feature Layer):
          The multipatch features with defined Airport schema. The feature class
          must be z-enabled.
      in_flightpath_features {Feature Layer}:
          The polyline features that define curved approaches to the specified
          runways. If unspecified, all input features will be processed as
          straight approaches.
      sampling_distance {Double}:
          The distance, in meters, between generated points. The default is 30.
      sample_profile_ois {Boolean}:
          Specifies whether elevation points for OIS features will be
          generated.PROFILE_OIS-Generates elevation
          points.NO_PROFILE_OIS-Elevation points
          will not be generated. This is
          default.
      sample_profile_runways {Boolean}:
          Specifies whether elevation points along the runways will be
          generated.PROFILE_RUNWAY-Generates elevation points along the
          runways.NO_PROFILE_RUNWAY-Uses only the start and end points of the
          runways.
          This is default.

        """