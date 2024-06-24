# Generated documentation for module arcpy.ga


class GASetModelParameter(object):
    """
    Sets parameter values in an existing geostatistical model source.
    """

    @property
    def description(self) -> str:
        return """

        GASetModelParameter_ga(in_ga_model_source, model_param_xpath, in_param_value, out_ga_model)

        Sets parameter values in an existing geostatistical model source.

     INPUTS:
      in_ga_model_source (Geostatistical Layer / File):
          The geostatistical model source to be analyzed.
      model_param_xpath (String):
          XML path to the required model parameter.
      in_param_value (String):
          Value for the parameter defined by the XML path.

     OUTPUTS:
      out_ga_model (File):
          Geostatistical model created with the parameter value defined in the
          XML path.

        """