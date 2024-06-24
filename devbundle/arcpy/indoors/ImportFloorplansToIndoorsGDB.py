# Generated documentation for module arcpy.indoors


class ImportFloorplansToIndoorsGDB(object):
    """
    Imports floor plans from CAD files into an Indoors workspace that conforms to the ArcGIS Indoors Information Model. The output of this tool can be used to create floor-aware maps and scenes for use in floor-aware apps, as well as to generate an indoor network for routing.
    """

    @property
    def description(self) -> str:
        return """

        ImportFloorplansToIndoorsGDB_indoors(target_unit_features, target_detail_features, target_level_features, target_facility_features, in_excel_template, uniqueid_delimiter, {sliver_threshold}, {door_close_buffer}, {area_unit_of_measure}, {measurement_mode}, {target_section_features}, {target_zone_features})

        Imports floor plans from CAD files into an Indoors workspace that
        conforms to the ArcGIS Indoors Information Model. The output of this
        tool can be used to create floor-aware maps and scenes for use in
        floor-aware apps, as well as to generate an indoor network for
        routing.

     INPUTS:
      target_unit_features (Feature Layer):
          The target Units feature layer, feature class, or feature service that
          conforms to the ArcGIS Indoors Information Model and resides in the
          same workspace as the target Facilities, Levels, and Details features.
      target_detail_features (Feature Layer):
          The target Details feature layer, feature class, or feature service
          that conforms to the ArcGIS Indoors Information Model and resides in
          the same workspace as the target Facilities, Levels, and Units
          features.
      target_level_features (Feature Layer):
          The target Levels feature layer, feature class, or feature service
          that conforms to the ArcGIS Indoors Information Model and resides in
          the same workspace as the target Facilities, Units, and Details
          features.
      target_facility_features (Feature Layer):
          The target Facilities feature layer, feature class, or feature service
          that conforms to the ArcGIS Indoors Information Model and resides in
          the same workspace as the target Levels, Units, and Details features.
      in_excel_template (File):
          An Excel spreadsheet (.xls or .xlsx file) that contains input and
          configuration parameters.
      uniqueid_delimiter (String):
          Specifies the delimiter that will separate key values in the Indoors
          model hierarchy.PERIOD-The ID will include key values separated by
          periods. This is
          default.HYPHEN-The ID will include key values separated by
          hyphens.UNDERSCORE-The ID will include key values separated by
          underscores.
      sliver_threshold {Long}:
          The ratio of perimeter to area that defines a sliver polygon. It is
          used when importing Unit polygons to improve the quality of the
          imported data. Unit polygons that are determined to be slivers are
          placed in a review geodatabase located in the scratch folder of the
          ArcGIS Pro project. The default is 2.
      door_close_buffer {Double}:
          The distance, in inches, that will be searched from a door to find and
          snap to the nearest wall. This parameter is used when the CLOSE_DOORS
          column is set to Y in the input Excel template file. The default is 0.
      area_unit_of_measure {String}:
          Specifies the unit of measure that will be used to calculate area for
          the area fields when importing floor plans.SQUARE_FEET-Area will be
          defined in square feet. This is
          default.SQUARE_METERS-Area will be defined in square meters.
      measurement_mode {String}:
          Specifies the measurement mode that will be used to calculate the area
          fields when importing floor plans.GEODESIC-Area will be calculated
          using geodesic distance. Geodesic
          distance is calculated in a 3D spherical space as the distance across
          the curved surface of the world. This is default.PLANAR-Area will be
          calculated using planar distance. Planar distance
          is straight-line Euclidean distance calculated in a 2D Cartesian
          coordinate system.
      target_section_features {Feature Layer}:
          The target Sections feature layer, feature class, or feature service
          that conforms to the ArcGIS Indoors Information Model and resides in
          the same workspace as the target Facilities, Levels, Units, and
          Details features.
      target_zone_features {Feature Layer}:
          The target Zones feature layer, feature class, or feature service that
          conforms to the ArcGIS Indoors Information Model and resides in the
          same workspace as the target Facilities, Levels, Units, and Details
          features.

        """