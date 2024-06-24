# Generated documentation for module arcpy.ga


class GAMovingWindowKriging(object):
    """
    Recalculates the Range, Nugget, and Partial Sill semivariogram parameters based on a smaller neighborhood, moving through all location points.
    """

    @property
    def description(self) -> str:
        return """

        GAMovingWindowKriging_ga(in_ga_model_source, in_datasets;in_datasets..., in_locations, neighbors_max, out_featureclass, {cell_size}, {out_surface_grid})

        Recalculates the Range, Nugget, and Partial Sill semivariogram
        parameters based on a smaller neighborhood, moving through all
        location points.

     INPUTS:
      in_ga_model_source (Geostatistical Layer / File):
          The geostatistical model source to be analyzed.
      in_datasets (Geostatistical Value Table):
          A GeostatisticalDatasets object.Alternatively, it can be a semicolon-
          delimited string of elements.
          Each element is comprised of the following components:The catalog path
          and name to a dataset or the name of a layer in the
          current table of contents, followed by a space.A sequence of field
          names, each field name separated by a space. In
          the case of a raster, the cell values will be used.
      in_locations (Feature Layer):
          Point locations where predictions will be performed.
      neighbors_max (Long):
          Number of neighbors to use in the moving window.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created. This
          value can be explicitly set in theby theparameter.
          EnvironmentsCell SizeIf not set, it is the shorter of the width or the
          height of the extent
          of the input point features, in the input spatial reference, divided
          by 250.

     OUTPUTS:
      out_featureclass (Feature Class):
          Feature class storing the results.
      out_surface_grid {Raster Dataset}:
          The prediction values in the output feature class are interpolated
          onto a raster using the Local polynomial interpolation method.

        """