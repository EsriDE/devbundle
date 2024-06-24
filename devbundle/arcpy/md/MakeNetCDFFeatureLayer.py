# Generated documentation for module arcpy.md


class MakeNetCDFFeatureLayer(object):
    """
    Makes a feature layer from a netCDF file.
    """

    @property
    def description(self) -> str:
        return """

        MakeNetCDFFeatureLayer_md(in_netCDF_file, variable;variable..., x_variable, y_variable, out_feature_layer, {row_dimension;row_dimension...}, {z_variable}, {m_variable}, {dimension_values;dimension_values...}, {value_selection_method})

        Makes a feature layer from a netCDF file.

     INPUTS:
      in_netCDF_file (File):
          The input netCDF file.
      variable (String):
          The netCDF variable, or variables, that will be added as fields in the
          feature attribute table.
      x_variable (String):
          A netCDF coordinate variable used to define the x, or longitude,
          coordinates of the output layer.
      y_variable (String):
          A netCDF coordinate variable used to define the y, or latitude,
          coordinates of the output layer.
      row_dimension {String}:
          The netCDF dimension, or dimensions, used to create features with
          unique values in the feature layer. The dimension or dimensions set
          here determine the number of features in the feature layer and the
          fields that will be presented in the feature layer's attribute
          table.For instance, if StationID is a dimension in the netCDF file and
          has
          10 values, by setting StationID as the dimension to use, 10 features
          will be created (10 rows will be created in the feature layer's
          attribute table). If StationID and time are used, and there are 3 time
          slices, 30 features will be created (30 rows will be created in the
          feature layer's attribute table). If you will be animating the netCDF
          feature layer, it is recommended, for efficiency reasons, to not set
          time as a row dimension. Time will still be available as a dimension
          that you can set to animate through, but the attribute table will not
          store this information.
      z_variable {String}:
          A netCDF variable used to specify elevation values (z-values) for
          features.
      m_variable {String}:
          A netCDF variable used to specify linear measurement values (m-values)
          for features.
      dimension_values {Value Table}:
          The value (such as 01/30/05) of the dimension (such as time) or
          dimensions to use when displaying the variable in the output layer. By
          default, the first value of the dimension or dimensions will be
          used.dimension-A netCDF dimension.{value}-The dimension value to use.
      value_selection_method {String}:
          Specifies the dimension value selection method that will be
          used.BY_VALUE-The input value will be matched with the actual
          dimension
          value.BY_INDEX-The input value will be matched with the position or
          index of
          a dimension value. The index is 0 based; that is, the position starts
          at 0.

     OUTPUTS:
      out_feature_layer (Feature Layer):
          The name of the output feature layer.

        """