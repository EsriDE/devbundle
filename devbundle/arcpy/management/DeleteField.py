# Generated documentation for module arcpy.management


class DeleteField(object):
    """
    Deletes one or more fields from a table, feature class, feature layer, or raster dataset.
    """

    @property
    def description(self) -> str:
        return """

        DeleteField_management(in_table, drop_field;drop_field..., {method})

        Deletes one or more fields from a table, feature class, feature layer,
        or raster dataset.

     INPUTS:
      in_table (Table View / Raster Layer / Mosaic Layer):
          The table containing the fields to be deleted. The existing input
          table will be modified.
      drop_field (Field):
          The fields to be dropped or kept from the input table, as specified by
          the method parameter. Only nonrequired fields can be deleted.
      method {String}:
          Specifies whether the fields specified by the drop_field parameter
          will be deleted or kept.DELETE_FIELDS-The fields specified by the
          drop_field parameter will be
          deleted. This is the default.KEEP_FIELDS-The fields specified by the
          drop_field parameter will be
          kept; all other fields will be deleted.

        """