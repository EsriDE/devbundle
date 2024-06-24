# Generated documentation for module arcpy.ga


class GaussianGeostatisticalSimulations(object):
    """
    Performs a conditional or unconditional geostatistical simulation based on a Simple Kriging model. The simulated rasters can be considered equally probable realizations of the kriging model.
    """

    @property
    def description(self) -> str:
        return """

        GaussianGeostatisticalSimulations_ga(in_geostat_layer, number_of_realizations, output_workspace, output_simulation_prefix, {in_conditioning_features}, {conditioning_field}, {cell_size}, {in_bounding_dataset}, {save_simulated_rasters}, {quantile}, {threshold}, {in_stats_polygons}, {raster_stat_type;raster_stat_type...}, {conditioning_measurement_error_field})

        Performs a conditional or unconditional geostatistical simulation
        based on a Simple Kriging model. The simulated rasters can be
        considered equally probable realizations of the kriging model.

     INPUTS:
      in_geostat_layer (Geostatistical Layer):
          Input a geostatistical layer resulting from a Simple Kriging model.
      number_of_realizations (Long):
          The number of simulations to perform.
      output_workspace (Workspace):
          Stores all the simulation results. The workspace can be either a
          folder or a geodatabase.
      output_simulation_prefix (String):
          A one- to three-character alphanumeric prefix that is automatically
          added to the output dataset names.
      in_conditioning_features {Feature Layer}:
          The features used to condition the realizations. If left blank,
          unconditional realizations are produced.
      conditioning_field {Field}:
          The field used to condition the realizations. If left blank,
          unconditional realizations are produced.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created. This
          value can be explicitly set in theby theparameter.
          EnvironmentsCell SizeIf not set, it is the shorter of the width or the
          height of the extent
          of the input point features, in the input spatial reference, divided
          by 250.
      in_bounding_dataset {Feature Layer}:
          Limits the analysis to these features' bounding polygon. If point
          features are entered, then a convex hull polygon is automatically
          created. Realizations are then performed within that polygon. If
          bounding features are supplied, any features or rasters supplied in
          the Mask environment will be ignored.
      save_simulated_rasters {Boolean}:
          Specifies whether or not the simulated rasters are saved to
          disk.SAVE_SIMULATIONS-Indicates that the simulated rasters will be
          saved to
          disk.DO_NOT_SAVE_SIMULATIONS-Indicates that the simulated rasters will
          not
          be saved to disk.
      quantile {Double}:
          The quantile value for which the output raster will be generated.
      threshold {Double}:
          The threshold value for which the output raster will be generated, as
          the percentage of the number of times the set threshold was exceeded,
          on a cell-by-cell basis.
      in_stats_polygons {Feature Layer}:
          These polygons represent areas of interest for which summary
          statistics are calculated.If in_stats_polygons are provided, the
          output polygon feature class
          will be saved in the location defined by output_workspace, and it will
          have the same name as the input polygons, preceded by the
          output_simulation_prefix. For example, if the input statistical
          polygons were named myPolys and you entered aaa as the output prefix,
          then the output polygons will be named aaamyPolys and will be saved in
          the specified output workspace.
      raster_stat_type {String}:
          The simulated rasters are postprocessed on a cell-by-cell basis, and
          each selected statistics type is calculated and reported in an output
          raster.MIN-Calculates the minimum (smallest value).MAX-Calculates the
          maximum
          (largest value).MEAN-Calculates the mean (average).STDDEV-Calculates
          the standard deviation.QUARTILE1-Calculates the 25th
          quantile.MEDIAN-Calculates the median.QUARTILE3-Calculates the 75th
          quantile.QUANTILE-Calculates a user-specified quantile (0 < Q <
          1).P_THRSHLD-Calculates the percentage of the simulations where the
          cell
          value exceeds a user-specified threshold value.
      conditioning_measurement_error_field {Field}:
          A field that specifies the measurement error for each input point in
          the conditioning features. For each conditioning feature, the value of
          this field should correspond to one standard deviation of the measured
          value of the feature. Use this field if the measurement error values
          are not the same at each sampling location.A common source of
          nonconstant measurement error is when the data is
          measured with different devices. One device might be more precise than
          another, which means that it will have a smaller measurement error.
          For example, one thermometer rounds to the nearest degree and another
          thermometer rounds to the nearest tenth of a degree. The variability
          of measurements is often provided by the manufacturer of the measuring
          device, or it may be known from empirical practice.Leave this
          parameter blank if there are no measurement error values or
          the measurement error values are unknown.

        """