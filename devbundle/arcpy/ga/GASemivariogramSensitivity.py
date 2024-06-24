# Generated documentation for module arcpy.ga


class GASemivariogramSensitivity(object):
    """
    This tool performs a sensitivity analysis on the predicted values and associated standard errors by changing the model's semivariogram parameters (the nugget, partial sill, and major/minor ranges) within a percentage of the original values.
    """

    @property
    def description(self) -> str:
        return """

        GASemivariogramSensitivity_ga(in_ga_model_source, in_datasets;in_datasets..., in_locations, {nugget_span_percents}, {nugget_calc_times}, {partialsill_span_percents}, {partialsill_calc_times}, {range_span_percents}, {range_calc_times}, {minrange_span_percents}, {minrange_calc_times}, out_table)

        This tool performs a sensitivity analysis on the predicted values and
        associated standard errors by changing the model's semivariogram
        parameters (the nugget, partial sill, and major/minor ranges) within a
        percentage of the original values.

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
          Point locations where the sensitivity analysis is performed.
      nugget_span_percents {Double}:
          The percentage subtracted and added to the Nugget parameter to create
          a range for a subsequent random Nugget parameter selection.
      nugget_calc_times {Long}:
          Number of random Nugget values randomly sampled from the Nugget span.
      partialsill_span_percents {Double}:
          Percentage subtracted from and added to the Partial Sill parameter to
          create a range for a random Partial Sill selection.
      partialsill_calc_times {Long}:
          Number of Partial Sill values randomly sampled from the Partial Sill
          span.
      range_span_percents {Double}:
          Percentage subtracted and added to the Major Range parameter to create
          a range for a random Major Range selection.
      range_calc_times {Long}:
          Number of Major Range values randomly sampled from the Major Range
          span.
      minrange_span_percents {Double}:
          Percentage subtracted and added to the Minor Range parameter to create
          a range for a random Minor Range selection.
      minrange_calc_times {Long}:
          Number of Minor Range values randomly sampled from the Minor Range
          span. If Anisotropy has been set in the, a value is required.
          input geostatistical model source

     OUTPUTS:
      out_table (Table):
          Table storing the sensitivity results.

        """