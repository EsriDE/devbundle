# Generated documentation for module arcpy.management


class ExportMosaicDatasetGeometry(object):
    """
    Creates a feature class showing the footprints, boundary, seamlines or spatial resolutions of a mosaic dataset.
    """

    @property
    def description(self) -> str:
        return """

        ExportMosaicDatasetGeometry_management(in_mosaic_dataset, out_feature_class, {where_clause}, {geometry_type})

        Creates a feature class showing the footprints, boundary, seamlines or
        spatial resolutions of a mosaic dataset.

     INPUTS:
      in_mosaic_dataset (Mosaic Layer):
          The mosaic dataset that you want to export the geometry from.
      where_clause {SQL Expression}:
          An SQL expression to export specific rasters in the mosaic dataset.
      geometry_type {String}:
          The type of geometry to export.FOOTPRINT-Create a feature class
          showing the footprints of each
          image.BOUNDARY-Create a feature class showing the boundary of the
          mosaic
          dataset.SEAMLINE-Create a feature class showing the seamlines.LEVEL-
          Create a feature class based on cell size level of features in
          your mosaic dataset.

     OUTPUTS:
      out_feature_class (Feature Class):
          Name the feature class you are creating.

        """