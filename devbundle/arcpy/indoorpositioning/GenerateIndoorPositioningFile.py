# Generated documentation for module arcpy.indoorpositioning


class GenerateIndoorPositioningFile(object):
    """
    Generates a positioning file from ArcGIS IPS Setup survey recordings.
    """

    @property
    def description(self) -> str:
        return """

        GenerateIndoorPositioningFile_indoorpositioning(in_ips_recordings, target_ips_positioning, {in_ips_transitions}, {in_ips_comment})

        Generates a positioning file from ArcGIS IPS Setup survey recordings.

     INPUTS:
      in_ips_recordings (Feature Layer):
          The feature class or feature service that contains IPS Setup survey
          recordings.
      target_ips_positioning (Table View):
          The table or feature service where the generated IPS positioning file
          will be stored.
      in_ips_transitions {Feature Layer}:
          The line feature class that contains the,, andfields that
          define facility entrances and exits. These are used by ArcGIS IPS to
          improve indoor and outdoor localization and switching. Thefield for
          entrances and exits must contain a value of 7 to be used by this tool.
          TRANSITION_TYPEVERTICAL_ORDER_FROMVERTICAL_ORDER_TOTRANSITION_TYPE
      in_ips_comment {String}:
          The text that will be used to populate thefield of the
          positioning file entry in the target_ips_positioning value.
          Comment

        """