# Generated documentation for module arcpy.management


class SetRasterProperties(object):
    """
    Sets the data type, statistics, and NoData values on a raster or mosaic dataset.
    """

    @property
    def description(self) -> str:
        return """

        SetRasterProperties_management(in_raster, {data_type}, {statistics;statistics...}, {stats_file}, {nodata;nodata...}, {key_properties;key_properties...}, {multidimensional_info;multidimensional_info...})

        Sets the data type, statistics, and NoData values on a raster or
        mosaic dataset.

     INPUTS:
      in_raster (Mosaic Layer / Raster Layer):
          The raster or mosaic dataset with the properties to be set.
      data_type {String}:
          Specifies the type of imagery in the mosaic dataset.GENERIC-The
          mosaic dataset does not have a specified data
          type.ELEVATION-The mosaic dataset contains elevation
          data.THEMATIC-The mosaic dataset contains thematic data, which has
          discrete
          values, such as land cover.PROCESSED-The mosaic dataset has been color
          balanced.SCIENTIFIC-The data has scientific information and will be
          displayed
          with the blue to red color ramp by default.VECTOR_UV-The data is a
          two-band raster that contains a U and a V
          component of vector field data.VECTOR_MAGDIR-The data is a two-band
          raster that contains the
          magnitude and direction of vector field data.DATE-The data has date
          information and will be displayed in date
          format.
      statistics {Value Table}:
          The bands and values for the minimum, maximum, mean, and standard
          deviation.
      stats_file {File}:
          An .xml file that contains the statistics.
      nodata {Value Table}:
          The NoData value for each band. Each band can have a unique NoData
          value defined, or the same value can be specified for all bands. To
          define multiple NoData values for each band selection, use a space
          delimiter between each NoData value.
      key_properties {Value Table}:
          The natively supported properties. The data used may have additional
          properties not included in the following list. The properties are not
          case sensitive.AcquisitionDateBandNameBlockNameCloudCoverDatasetTagFlo
          wDirectionFootp
          rintHighCellSizeLowCellSizeMinCellSizeMaxCellSizeOffNadirParentRasterT
          ypeParentTemplatePerspectiveXPerspectiveYPerspectiveZProductNameRadian
          ceBiasRadianceGainReflectanceBiasReflectanceGainSegmentedSensorAzimuth
          SensorElevationSensorNameSolarIrradianceSourceBandIndexSunAzimuthSunEl
          evationThermalConstant_K1ThermalConstant_K2VerticalAccuracyWavelengthM
          inWavelengthMax
      multidimensional_info {Value Table}:
          The dimensional information for the raster dataset. Setting
          dimensional information will convert the dimensionless raster into a
          multidimensional raster.If the dimension is time, the dimension name
          must be StdTime. The
          format for time is either year-month-day (2021-10-01) or year-month-
          dayThh:mm:ss (2021-10-01T01:00:00).To define a variable with both time
          and elevation, add the variable
          with time first; then add the same variable with the z-dimension.

        """