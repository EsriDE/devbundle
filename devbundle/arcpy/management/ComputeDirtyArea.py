# Generated documentation for module arcpy.management


class ComputeDirtyArea(object):
    """
    Identifies areas within a mosaic dataset that have changed since a specified point in time. This is used commonly when a mosaic dataset is updated or synchronized, or when derived products, such as cache, need to be updated. This tool will enable you to limit such processes to only the areas that have changed.
    """

    @property
    def description(self) -> str:
        return """

        ComputeDirtyArea_management(in_mosaic_dataset, {where_clause}, timestamp, out_feature_class)

        Identifies areas within a mosaic dataset that have changed since a
        specified point in time. This is used commonly when a mosaic dataset
        is updated or synchronized, or when derived products, such as cache,
        need to be updated. This tool will enable you to limit such processes
        to only the areas that have changed.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that you want to analyze for changes.
      where_clause {SQL Expression}:
          SQL expression to select specific rasters within the mosaic dataset on
          which to compute dirty areas.
      timestamp (String):
          Compute the areas that have changed since the input time. XML
          time syntax:        YYYY-MM-DDThh:mm:ssYYYY-MM-
          DDThh:mm:ss.ssssZ2002-10-10T12:00:00.ssss-
          00:002002-10-10T12:00:00+00:00Non-XML time syntax:2002/12/25
          23:59:58.123

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class containing the areas that have changed.

        """