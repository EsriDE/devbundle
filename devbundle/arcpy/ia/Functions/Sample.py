# Generated documentation for module arcpy.ia.Functions


class Sample(object):
    """
    Creates a table or a point feature class that shows the values of cells from a raster, or a set of rasters, for defined locations. The locations are defined by raster cells, points, polylines, or polygons.
    """

    @property
    def description(self) -> str:
        return """

        Sample_ia(in_rasters;in_rasters..., in_location_data, out_table, {resampling_type}, {unique_id_field}, {process_as_multidimensional}, {acquisition_definition;acquisition_definition...}, {statistics_type}, {percentile_value}, {buffer_distance}, {layout}, {generate_feature_class})

        Creates a table or a point feature class that shows the values of
        cells from a raster, or a set of rasters, for defined locations. The
        locations are defined by raster cells, points, polylines, or polygons.

     INPUTS:
      in_rasters (Composite Geodataset):
          The rasters with values that will be sampled based on the input
          location data.The process_as_multidimensional parameter is only
          supported when the
          input is a single, multidimensional raster.
      in_location_data (Composite Geodataset):
          The data identifying positions where a sample will be taken.The input
          can be a raster or a feature class.
      resampling_type {String}:
          The resampling algorithm that will be used to sample a raster to
          determine how the values will be obtained from the
          raster.NEAREST-Nearest neighbor assignment will be used. This is the
          default.BILINEAR-Bilinear interpolation will be used.CUBIC-Cubic
          convolution will be used.
      unique_id_field {Field}:
          A field containing a different value for every location or feature in
          the input location raster or features.
      process_as_multidimensional {Boolean}:
          Specifies how the input rasters will be processed.This parameter is
          only available when the input is a single,
          multidimensional raster.ALL_SLICES-Samples will be processed for all
          dimensions (such as time
          or depth) of a multidimensional dataset.CURRENT_SLICE-Samples will be
          processed from the current slice of a
          multidimensional dataset. This is the default.
      acquisition_definition {Value Table}:
          Specifies the time, depth, or other acquisition data associated with
          the location features. Only the following combinations are
          supported:
          Dimension + Start field or valueDimension + Start field or value + End
          field or valueDimension + Start field or value + Relative value or
          days before +
          Relative value or days afterRelative value or days before and Relative
          value or days after only
          support nonnegative values.Statistics will be calculated using the
          statistics_type parameter for
          variables within this dimension range.
      statistics_type {String}:
          Specifies the statistic type to be calculated.MINIMUM-The minimum
          value within the specified range will be
          calculated.MAXIMUM-The maximum value within the specified range will
          be
          calculated.MEDIAN-The median value within the specified range will be
          calculated.MEAN-The average for the specified range will be
          calculated.SUM-The total value of the variables within the specified
          range will
          be calculated.MAJORITY-The value that occurs most frequently will be
          calculated.MINORITY-The value that occurs least frequently will be
          calculated.STD-The standard deviation will be calculated.PERCENTILE-A
          defined percentile within the specified range will be
          calculated.
      percentile_value {Double}:
          The percentile to calculate when theparameter is set to.
          Statistics TypePercentileThe percentile to calculate when the
          statistics_type parameter is set
          to PERCENTILE.This value can range from 0 to 100. The default is 90.
      buffer_distance {Double / Field}:
          The distance around the location data features. The buffer distance is
          specified in the linear unit of the location feature's spatial
          reference. If the feature uses a geographic reference, the unit will
          be degrees.Statistics will be calculated within this buffer area.
      layout {Boolean}:
          Specifies whether sampled values will appear in rows or columns in the
          output table.ROW_WISE-Sampled values will appear in separate rows in
          the output
          table. This is the default.COLUMN_WISE-Sampled values will appear in
          separate columns in the
          output table. This option is only valid when the input
          multidimensional raster contains one variable and one dimension, and
          each slice is a single-band raster.
      generate_feature_class {Boolean}:
          Specifies whether a point feature class with sampled values in its
          attribute table or a table with sampled values will be
          generated.TABLE-A table with sampled values will be generated. This is
          the
          default.FEATURE_CLASS-A point feature class with sampled values in its
          attribute table will be generated.

     OUTPUTS:
      out_table (Table):
          The output table or feature class containing the sampled cell
          values.The output format is determined by the output location and
          path. By
          default, the output will be a geodatabase table or a geodatabase
          feature class in a geodatabase workspace or a dBASE table or a
          shapefile feature class in a folder workspace.The output data type to
          generate a table or a feature class is
          controlled by the generate_feature_class parameter.

        """