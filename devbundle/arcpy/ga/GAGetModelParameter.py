# Generated documentation for module arcpy.ga


class GAGetModelParameter(object):
    """
    Gets model parameter value from an existing geostatistical model source.
    """

    @property
    def description(self) -> str:
        return """

        GAGetModelParameter_ga(in_ga_model_source, model_param_xpath)

        Gets model parameter value from an existing geostatistical model
        source.

     INPUTS:
      in_ga_model_source (Geostatistical Layer / File):
          The geostatistical model source to be analyzed.
      model_param_xpath (String):
          XML path to the required model parameter.

        """