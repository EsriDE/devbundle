# Generated documentation for module arcpy.ia.Functions


class OptimalInterpolation(object):
    """
    Statistically assimilates data combined from multiple sources to produce an output raster. The tool can be used to merge background data, such as model outputs, with observation data, such as point measurements, to perform interpolation.
    """

    @property
    def description(self) -> str:
        return """

        OptimalInterpolation_ia(in_background_raster, in_obs_data, obs_field, background_error_var, obs_error_var, {background_error_corr_length})

        Statistically assimilates data combined from multiple sources to
        produce an output raster. The tool can be used to merge background
        data, such as model outputs, with observation data, such as point
        measurements, to perform interpolation.

     INPUTS:
      in_background_raster (Raster Layer / Image Service / Raster Dataset):
          The input background raster also known as the background field.
      in_obs_data (Feature Layer / Trajectory Layer):
          The input point features that will be used for interpolation.
      obs_field (String):
          The field containing observation values that will be used for
          interpolation.
      background_error_var (Raster Layer / Image Service / Double / Raster Dataset):
          The error variance of the background measurements.The input can be a
          single value or an error variance raster. If a
          single value is provided, the value will be used as the error variance
          for all background measurements. If an error variance raster is
          provided, each cell in the background data will obtain its error
          variance from the corresponding background error variance raster. The
          error variance raster must have the same cell size and extent as the
          background data.
      obs_error_var (String / Double):
          The error variance of the observations. The input can be a single
          value or a field from the observation data. If a single value is
          provided, the value will be used as the error variance for all
          observations. If a field in the observation data is provided, values
          in the field will be used as the error variance for each corresponding
          observation point.
      background_error_corr_length {Double}:
          The correlation length between background measurements. The default is
          three times the cell size of the in_background_raster parameter value.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output multidimensional raster dataset.

        """