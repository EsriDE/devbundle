# Generated documentation for module arcpy.bathymetry


class RemoveDataFromBIS(object):
    """
    Removes data from a Bathymetric Information System (BIS) geodatabase.
    """

    @property
    def description(self) -> str:
        return """

        RemoveDataFromBIS_bathymetry(target_biscatalog, {where_clause}, {delete_overview_images}, {update_overviews})

        Removes data from a Bathymetric Information System (BIS) geodatabase.

     INPUTS:
      target_biscatalog (Feature Layer):
          The catalog dataset in the BIS workspace.
      where_clause {SQL Expression}:
          An SQL expression to select the datasets that will be removed from the
          BIS.If no datasets are selected, either from the BisCatalog attributes
          table or through a definition query, a warning is generated. To delete
          all records from a BIS, specify a query that selects all datasets; for
          example, OBJECTID >= 0.
      delete_overview_images {Boolean}:
          Specifies whether the overviews associated with the selected rasters
          will be deleted.DELETE_OVERVIEW_IMAGES-The overviews will be deleted.
          This is the
          default.NO_DELETE_OVERVIEW_IMAGES-The overviews will not be deleted.
      update_overviews {Boolean}:
          Specifies whether the overviews and statistics will be
          updated.UPDATE_OVERVIEWS-The overviews and statistics for a mosaic
          dataset
          will be updated.NO_UPDATE_OVERVIEWS-The overviews and statistics for a
          mosaic dataset
          will not be updated. This is the default.

        """