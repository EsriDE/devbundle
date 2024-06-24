# Generated documentation for module arcpy.ga


class DensifySamplingNetwork(object):
    """
    Uses a predefined geostatistical kriging layer to determine where new monitoring stations should be built. It can also be used to determine which monitoring stations should be removed from an existing network.
    """

    @property
    def description(self) -> str:
        return """

        DensifySamplingNetwork_ga(in_geostat_layer, number_output_points, out_feature_class, {selection_criteria}, {threshold}, {in_weight_raster}, {in_candidate_point_features}, {inhibition_distance})

        Uses a predefined geostatistical kriging layer to determine where new
        monitoring stations should be built. It can also be used to determine
        which monitoring stations should be removed from an existing network.

     INPUTS:
      in_geostat_layer (Geostatistical Layer):
          Input a geostatistical layer resulting from a Kriging model.
      number_output_points (Long):
          Specify how many sample locations to generate.
      selection_criteria {String}:
          Methods to densify a sampling network.STDERR-Standard error of
          prediction criteriaSTDERR_THRESHOLD-Standard
          error threshold criteriaQUARTILE_THRESHOLD-Lower quartile threshold
          criteriaQUARTILE_THRESHOLD_UPPER-Upper quartile threshold criteriaThe
          STERR option will give extra weight to locations where the
          standard error of prediction is large. The STDERR_THRESHOLD,
          QUARTILE_THRESHOLD, and QUARTILE_THRESHOLD_UPPER options are useful
          when there is a critical threshold value for the variable under study
          (such as the highest admissible ozone level). The STDERR_THRESHOLD
          option will give extra weight to locations whose values are close to
          the threshold. The QUARTILE_THRESHOLD option will give extra weight to
          locations that are least likely to exceed the critical threshold. The
          QUARTILE_THRESHOLD_UPPER option will give extra weight to locations
          that are most likely to exceed the critical threshold. The
          equations for each option are:                 Standard
          error of prediction = stderr Standard error
          threshold = stderr(s)(1 - 2 · abs(prob[Z(s) > threshold] - 0.5)) Lower
          quartile threshold = (Z(s) - Z(s)) · (prob[Z(s) < threshold]) Upper
          quartile threshold = (Z(s) - Z(s)) · (prob[Z(s) > threshold])
          0.750.250.750.25
      threshold {Double}:
          The threshold value used to densify the sampling network. This
          parameter is only applicable when,, orselection criteria
          is used. Standard error thresholdLower quartile thresholdUpper
          quartile threshold
      in_weight_raster {Raster Layer}:
          A raster used to determine which locations to weight for preference.
      in_candidate_point_features {Feature Layer}:
          Sample locations to pick from.
      inhibition_distance {Linear Unit}:
          Used to prevent any samples being placed within this distance from
          each other.

     OUTPUTS:
      out_feature_class (Feature Class):
          The name of the output feature class.

        """