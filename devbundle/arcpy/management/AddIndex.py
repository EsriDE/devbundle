# Generated documentation for module arcpy.management


class AddIndex(object):
    """
    Adds an attribute index to an existing table, feature class, shapefile, or attributed relationship class.
    """

    @property
    def description(self) -> str:
        return """

        AddIndex_management(in_table, fields;fields..., {index_name}, {unique}, {ascending})

        Adds an attribute index to an existing table, feature class,
        shapefile, or attributed relationship class.

     INPUTS:
      in_table (Table View / Raster Layer / Mosaic Layer):
          The table containing the fields to be indexed.
      fields (Field):
          The list of fields that will be indexed. Any number of fields can be
          specified.
      index_name {String}:
          The name of the new index. An index name is necessary when adding an
          index to geodatabase feature classes and tables. For other types of
          input, the name is ignored.
      unique {Boolean}:
          Specifies whether the values in the index are unique.NON_UNIQUE-No
          values in the index are unique. This is the
          default.UNIQUE-All values in the index are unique.
      ascending {Boolean}:
          Specifies whether values will be indexed in ascending
          order.NON_ASCENDING-Values will not be indexed in ascending order.
          This is
          the default.ASCENDING-Values will be indexed in ascending order.

        """