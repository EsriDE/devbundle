# Generated documentation for module arcpy.na


class TurnTableToTurnFeatureClass(object):
    """
    Converts an ArcView turn table or ArcInfo Workstation coverage turn table to an ArcGIS turn feature class.
    """

    @property
    def description(self) -> str:
        return """

        TurnTableToTurnFeatureClass_na(in_turn_table, reference_line_features, out_feature_class_name, {reference_nodes_table}, {maximum_edges}, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})

        Converts an ArcView turn table or ArcInfo Workstation coverage turn
        table to an ArcGIS turn feature class.

     INPUTS:
      in_turn_table (Table View):
          The .dbf file or INFO turn table from which the new turn feature class
          will be created.INFO tables do not support mixed case path names on
          Linux and Solaris.
      reference_line_features (Feature Class):
          The line feature class to which the input turn table refers. The
          feature class must be a source in a network dataset.
      out_feature_class_name (String):
          The name of the new turn feature class to create.
      reference_nodes_table {dBASE Table}:
          The nodes.dbf table in the .nws folder containing the original ArcView
          GIS network in which the input turn table participated.This parameter
          is ignored if the input turn table is an INFO table.If the input turn
          table is a .dbf table and this parameter is omitted,
          then U-turns and turns that traverse between edges connected to each
          other at both ends will not be created in the output turn feature
          class.Errors will be reported in an error file written to the
          directory
          defined by the TEMP system variable. The full path name to the error
          file is reported as a warning message.
      maximum_edges {Long}:
          The maximum number of edges per turn in the new turn feature class.
          The default value is 5. The maximum value is 50.
      config_keyword {String}:
          Specifies the configuration keyword that determines the storage
          parameters of the output turn feature class. This parameter is used
          only if the output turn feature class is created in a workgroup or
          enterprise geodatabase.
      spatial_grid_1 {Double}:
          This parameter has been deprecated in ArcGIS Pro. Any value you enter
          is ignored.
      spatial_grid_2 {Double}:
          This parameter has been deprecated in ArcGIS Pro. Any value you enter
          is ignored.
      spatial_grid_3 {Double}:
          This parameter has been deprecated in ArcGIS Pro. Any value you enter
          is ignored.

        """