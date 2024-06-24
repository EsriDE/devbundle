# Generated documentation for module arcpy.management


class AddRelate(object):
    """
    Relates a layer to another layer or table based on a field value. Feature layers, table views, subtype value layers or tables, and raster layers with a raster attribute table are supported.
    """

    @property
    def description(self) -> str:
        return """

        AddRelate_management(in_layer_or_view, in_field, relate_table, relate_field, relate_name, {cardinality})

        Relates a layer to another layer or table based on a field value.
        Feature layers, table views, subtype value layers or tables, and
        raster layers with a raster attribute table are supported.

     INPUTS:
      in_layer_or_view (Table View / Raster Layer / Mosaic Layer):
          The layer or table view to which the relate table will be related.
      in_field (Field):
          The field in the input layer or table view on which the relate will be
          based.
      relate_table (Table View / Raster Layer / Mosaic Layer):
          The table or table view to be related to the input layer or table
          view.
      relate_field (Field):
          The field in the relate table that contains the values on which the
          relate will be based.
      relate_name (String):
          The unique name given to a relate.
      cardinality {String}:
          Specifies the cardinality of the relationship.ONE_TO_ONE-The
          relationship between the input table and related table
          will be one to one. For example, one record in the input table will
          have only one matching record in the related table.ONE_TO_MANY-The
          relationship between the input table and related table
          will be one to many. For example, one record in the input table can
          have multiple matching records in the related table. This is the
          default.MANY_TO_MANY-The relationship between the input table and
          related
          table will be many to many. For example, many records with the same
          value in the input table can have multiple matching records in the
          related table.

        """