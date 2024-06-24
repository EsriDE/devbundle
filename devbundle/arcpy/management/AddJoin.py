# Generated documentation for module arcpy.management


class AddJoin(object):
    """
    Joins a layer to another layer or table based on a common field. Feature layers, table views, and raster layers with a raster attribute table are supported.
    """

    @property
    def description(self) -> str:
        return """

        AddJoin_management(in_layer_or_view, in_field, join_table, join_field, {join_type}, {index_join_fields}, {rebuild_index}, {join_operation})

        Joins a layer to another layer or table based on a common field.
        Feature layers, table views, and raster layers with a raster attribute
        table are supported.

     INPUTS:
      in_layer_or_view (Table View / Raster Layer / Mosaic Layer):
          The layer or table view to which the join table will be joined.
      in_field (Field):
          The field in the input layer or table view on which the join will be
          based.
      join_table (Table View / Raster Layer / Mosaic Layer):
          The table or table view that will be joined to the input layer or
          table view.
      join_field (Field):
          The field in the join table that contains the values on which the join
          will be based.
      join_type {Boolean}:
          Specifies whether only records in the input that match a record in the
          join table will be included in the output.KEEP_ALL-All records in the
          input layer or table view will be included
          in the output. This is also known as an outer join. This is the
          default.KEEP_COMMON-Only those records in the input that match a row
          in the
          join table will be included in the output. This is also known as an
          inner join.
      index_join_fields {Boolean}:
          Specifies whether table attribute indexes will be added to the input
          field and join field.INDEX_JOIN_FIELDS-Both fields will be indexed. If
          the table has an
          existing index, a new index will not be
          added.NO_INDEX_JOIN_FIELDS-Indexes will not be added. This is the
          default.
      rebuild_index {Boolean}:
          Specifies whether the indexes of the input field and join field will
          be removed and rebuilt.REBUILD_INDEX-Existing indexes will be removed
          and a new index will
          be added.NO_REBUILD_INDEX-Existing indexes will not be removed or
          rebuilt.
          This is the default.
      join_operation {String}:
          Specifies whether the join will be a one-to-many join or a one-to-
          first join when the data has a one-to-many cardinality.If no parameter
          value is specified, the join operation will be based
          on the data source.JOIN_ONE_TO_FIRST-The join operation will use the
          first
          match.JOIN_ONE_TO_MANY-The join operation will perform multiple case-
          sensitive matches.

        """