# Generated documentation for module arcpy.ga


class DiffusionInterpolationWithBarriers(object):
    """
    Interpolates a surface using a kernel that is based upon the heat equation and allows one to use raster and feature barriers to redefine distances between input points.
    """

    @property
    def description(self) -> str:
        return """

        DiffusionInterpolationWithBarriers_ga(in_features, z_field, {out_ga_layer}, {out_raster}, {cell_size}, {in_barrier_features}, {bandwidth}, {number_iterations}, {weight_field}, {in_additive_barrier_raster}, {in_cumulative_barrier_raster}, {in_flow_barrier_raster})

        Interpolates a surface using a kernel that is based upon the heat
        equation and allows one to use raster and feature barriers to redefine
        distances between input points.

     INPUTS:
      in_features (Feature Layer):
          The input point features containing the z-values to be interpolated.
      z_field (Field):
          Field that holds a height or magnitude value for each point. This can
          be a numeric field or the Shape field if the input features contain
          z-values or m-values.
      cell_size {Analysis Cell Size}:
          The cell size at which the output raster will be created. This
          value can be explicitly set in theby theparameter.
          EnvironmentsCell SizeIf not set, it is the shorter of the width or the
          height of the extent
          of the input point features, in the input spatial reference, divided
          by 250.
      in_barrier_features {Feature Layer}:
          Absolute barrier features using non-Euclidean distances rather than
          line-of-sight distances.
      bandwidth {Double}:
          Used to specify the maximum distance at which data points are used for
          prediction. With increasing bandwidth, prediction bias increases and
          prediction variance decreases.
      number_iterations {Long}:
          The iteration count controls the accuracy of the numerical solution
          because the model solves the diffusion equation numerically. The
          larger this number, the more accurate the predictions, yet the longer
          the processing time. The more complex the barrier's geometry and the
          larger the bandwidth, the more iterations are required for accurate
          predictions.
      weight_field {Field}:
          Used to emphasize an observation. The larger the weight, the more
          impact it has on the prediction. For coincident observations, assign
          the largest weight to the most reliable measurement.
      in_additive_barrier_raster {Raster Layer}:
          The travel distance from one raster cell to the next based on this
          formula:(average cost value in the neighboring cells) x (distance
          between cell
          centers)
      in_cumulative_barrier_raster {Raster Layer}:
          The travel distance from one raster cell to the next based on this
          formula:(difference between cost values in the neighboring cells) +
          (distance
          between cell centers)
      in_flow_barrier_raster {Raster Layer}:
          A flow barrier is used when interpolating data with preferential
          direction of data variation, based on this formula:        Indicator
          (cost values in theneighboring cell > cost values in
          theneighboring cell) * (cost values in theneighboring cell - cost
          values in theneighboring cell) + (distance between cell centers),
          tofromtofromwhere indicator(true) = 1 and indicator(false) = 0.

     OUTPUTS:
      out_ga_layer {Geostatistical Layer}:
          The geostatistical layer produced. This layer is required output only
          if no output raster is requested.
      out_raster {Raster Dataset}:
          The output raster. This raster is required output only if no output
          geostatistical layer is requested.

        """