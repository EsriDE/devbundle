# Generated documentation for module arcpy.aviation


class GenerateAirspaceLines(object):
    """
    Generates line features in the AirspaceLine feature class from the edges of input Airspace polygon features.
    """

    @property
    def description(self) -> str:
        return """

        GenerateAirspaceLines_aviation(in_airspace_features;in_airspace_features..., target_airspace_line_features, aoi_features, preference_table, preference;preference..., {label_airspaces})

        Generates line features in the AirspaceLine feature class from the
        edges of input Airspace polygon features.

     INPUTS:
      in_airspace_features (Feature Layer):
          The polygon feature classes containing the airspace boundaries.
      target_airspace_line_features (Feature Layer):
          The polyline feature class containing the airspace line data.
      aoi_features (Feature Layer):
          The polygon feature class containing the AOI data.The selected polygon
          features will be used to filter the airspace
          lines that will be added, modified, or deleted.
      preference_table (Table View):
          The table of preferences that define how the airspace lines will be
          added, modified, or deleted.
      preference (String):
          The name of a selected preference in the preference_table parameter
          value. The selected preference defines how the airspace lines will be
          added, modified, or deleted.
      label_airspaces {Boolean}:
          Specifies whether the output line's left and right labels will
          aggregate and show the labels of the intersecting airspaces that the
          line is within.NO_INTERSECTING_AIRSPACES-The left and right labels of
          the output
          lines will contain the airspace labels of the coincident airspaces
          only. Intersecting airspaces will not be included. Only coincident
          airspaces that touch the airspace line within the preference cluster
          tolerance will be identified. This is the
          default.INTERSECTING_AIRSPACES-The left and right labels of the output
          lines
          will contain airspace labels of intersecting airspaces and coincident
          airspaces. Only coincident airspaces that touch the airspace line
          within the default cluster tolerance will be identified.

        """