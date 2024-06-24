# Generated documentation for module arcpy.aviation


class ICAOAnnex4Surfaces(object):
    """
    Creates obstruction identification surfaces (OIS) based on the ICAO Annex 4 specifications for either a Take-Off Flight Path Area or a Precision Approach Terrain Area.
    """

    @property
    def description(self) -> str:
        return """

        ICAOAnnex4Surfaces_aviation(in_features, target_ois_features, surface_generation;surface_generation..., {runway_direction}, {clear_way_length}, {threshold_point_feature_class}, {custom_json_file})

        Creates obstruction identification surfaces (OIS) based on the ICAO
        Annex 4 specifications for either a Take-Off Flight Path Area or a
        Precision Approach Terrain Area.

     INPUTS:
      in_features (Feature Layer):
          The input runway dataset. The feature class must be z-enabled and
          contain polylines.
      target_ois_features (Feature Layer):
          The target feature class that will contain the generated OIS.
      surface_generation (String):
          Specifies the types of surfaces that will be created.
          PRECISION_APPROACH_TERRAIN_AREA-A surface that is 60 meters
          either side of the extended runway centerline to a distance of 900
          meters from the threshold, with a 3 percent slope rising outward from
          the threshold will be created. The surface will be
          created pursuant to, Chapter 6, 6.5.1.
          ICAO Annex 4         TAKEOFF_FLIGHT_PATH_AREA-A surface with a 180
          meter width at
          its point of origin (end of runway or clearway), which increases at a
          rate of 0.25D to a maximum of 1800 meters, where D is the distance
          from the point of origin that will be created. This surface extends to
          a distance of 10 kilometers and has a 1.2 percent slope ascending
          outward from the point of origin. The surface will
          be created pursuant to, Chapter 3, 3.8.2.
          ICAO Annex 4
      runway_direction {String}:
          Specifies the end of the runway where the approach surface will be
          created.HIGH_END_TO_LOW_END-The approach surface will be created at
          the high
          end of the runway to the low end. If a displaced threshold point
          exists at the high end of the runway, that point will be honored when
          creating the OIS.LOW_END_TO_HIGH_END-The approach surface will be
          created at the low
          end of the runway to the high end. If a displaced threshold point
          exists at the low end of the runway, that point will be honored when
          creating the OIS.
      clear_way_length {Double}:
          The length of the area beyond the runway in meters.
      threshold_point_feature_class {Feature Layer}:
          Supplies x-, y-, and z-geometry for displaced threshold features. If
          displaced thresholds are included, surfaces will be constructed based
          on their x-, y-, and z-geometry instead of their corresponding runway
          feature endpoint.
      custom_json_file {File}:
          The import configuration, in JSON format, that will be used to create
          the custom OIS.To create a .json file for this parameter, use the
          CustomizeOIS.exe
          file that is part of the ArcGIS Aviation data package available from
          My Esri.

        """