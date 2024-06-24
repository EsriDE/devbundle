# Generated documentation for module arcpy.stats


class CollectEvents(object):
    """
    Converts event data, such as crime or disease incidents, to weighted point data.
    """

    @property
    def description(self) -> str:
        return """

        CollectEvents_stats(Input_Incident_Features, Output_Weighted_Point_Feature_Class)

        Converts event data, such as crime or disease incidents, to weighted
        point data.

     INPUTS:
      Input_Incident_Features (Feature Layer):
          The features representing event or incident data.

     OUTPUTS:
      Output_Weighted_Point_Feature_Class (Feature Class):
          The output feature class that will contain the weighted point data.

        """