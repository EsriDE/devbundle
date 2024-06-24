# Generated documentation for module arcpy.aviation


class GenerateAviationChartLeads(object):
    """
    Creates text graphics at intersection points between a map frame boundary and line features.
    """

    @property
    def description(self) -> str:
        return """

        GenerateAviationChartLeads_aviation(in_layout, in_mapframe, in_preferences_table, preference)

        Creates text graphics at intersection points between a map frame
        boundary and line features.

     INPUTS:
      in_layout (Layout):
          The target layout that contains the map frame for which chart leads
          will be generated.
      in_mapframe (String):
          The map frame for which chart leads will be generated.
      in_preferences_table (Table View):
          The table of preferences that controls how the chart leads will be
          calculated and placed.
      preference (String):
          The list of preferences determined from the in_preferences_table
          parameter.

        """