# Generated documentation for module arcpy.ca


class CellSiteRecordsToFeatureClass(object):
    """
    Creates cell site points and sector polygons based on input latitude, longitude, azimuth, beamwidth, and radius information from a cell site table.
    """

    @property
    def description(self) -> str:
        return """

        CellSiteRecordsToFeatureClass_ca(in_table, out_site_feature_class, out_sector_feature_class, id_fields;id_fields..., x_field, y_field, in_coordinate_system, out_coordinate_system, {azimuth_field}, {default_azimuth}, {beamwidth_field}, {beamwidth_type}, {default_beamwidth}, {radius_field}, {radius_unit}, {default_radius_length})

        Creates cell site points and sector polygons based on input latitude,
        longitude, azimuth, beamwidth, and radius information from a cell site
        table.

     INPUTS:
      in_table (Table View):
          The input table containing cell site information provided by the
          wireless network provider.
      id_fields (Value Table):
          Specifies the unique ID field type and the fields that will be added
          to the output feature. Use thevalue when theparameter has a
          unique identifier for all
          cell sector antennas. Use a combination of othervalues when
          theparameter does not contain a universal unique identifier for all
          cell sector antennas. Unique IDInput Cell Site TableID
          TypeInput Cell Site TableID Type-The field name to be included in the
          output feature
          classes.Field-The name of the fields that uniquely identify the cell
          sector
          antennas. These will be added to the output feature class.
          options are as follows:        ID TypeUnique ID-Uniquely identifies a
          cell sector antennaSite ID-Uniquely
          identifies a cell siteSector ID-Uniquely identifies a cell
          sectorSwitch ID-Uniquely identifies a wireless network switchLAC
          ID-Uniquely identifies the Location Area CodeCascade ID-Uniquely
          identifies the sector in the wireless network
          cascadeCell ID-Identifies the sector within an Location Area Code
      x_field (Field):
          The field in the input table that contains the x-coordinate of the
          cell site.
      y_field (Field):
          The field in the input table that contains the y-coordinate of the
          cell site.
      in_coordinate_system (Coordinate System):
          The coordinate system of the coordinates specified in
          theandparameters. X FieldY Field
      out_coordinate_system (Coordinate System):
          The projected coordinate system of the output sites and sectors.
      azimuth_field {Field}:
          The field in the input table that contains the direction of the
          antenna signal (cell sector).The azimuth field values must be
          expressed in positive degrees from 0
          to 360, measured clockwise from north.
      default_azimuth {Double}:
          The starting azimuth value of the antenna signals (cell sectors) that
          will be used when the azimuth field is not specified.For example,
          three cell sectors exist at the same location and this
          parameter is set to 0 degrees. The first sector is generated with an
          azimuth of 0 degrees, the second sector is generated with an azimuth
          of 120 degrees, and the third sector is generated with an azimuth of
          240 degrees.This parameter is used when the azimuth field is not
          specified.The azimuth value must be expressed in positive degrees from
          0 to 360.
          The default is 0.
      beamwidth_field {Field}:
          The field in the input table containing the full or half beamwidth
          value (angle) of the antenna signal (cell sector).The beamwidth must
          be expressed in positive degrees from 0 to 360. Use
          360 for omnidirectional antennas.
      beamwidth_type {String}:
          Specifies the type of beamwidth value represented in the input cell
          type table.FULL_BEAMWIDTH-Full beamwidth is represented in the input.
          This is the
          default.HALF_BEAMWIDTH-Half beamwidth is represented in the input
      default_beamwidth {Double}:
          The beamwidth (in degrees) of the antenna signal (cell sector) that
          will be used when the beamwidth field is not specified.The default is
          90 degrees.
      radius_field {Field}:
          The field in the input table that contains the radial length (signal
          distance) of the antenna signal (cell sector).
      radius_unit {String}:
          Specifies the linear unit that will be used with the radius
          field.KILOMETERS-The unit will be kilometers.METERS-The unit will be
          meters.MILESINT-The unit will be statute miles.YARDSINT-The unit will
          be international yards.FEETINT-The unit will be international
          feet.MILES-The unit will be US Survey miles. This is the
          default.YARDS-The unit will be US Survey yards.FEET-The unit will be
          US Survey feet.
      default_radius_length {Double}:
          The radius length (signal distance) of the antenna signal (cell
          sector) that will be used when the radial field is not specified.The
          default is 2.

     OUTPUTS:
      out_site_feature_class (Feature Class):
          The feature class containing the output cell site points.
      out_sector_feature_class (Feature Class):
          The feature class containing the output cell site sectors.

        """