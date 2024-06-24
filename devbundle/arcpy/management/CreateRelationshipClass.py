# Generated documentation for module arcpy.management


class CreateRelationshipClass(object):
    """
    Creates a relationship class to store an association between fields or features in the origin table and the destination table.
    """

    @property
    def description(self) -> str:
        return """

        CreateRelationshipClass_management(origin_table, destination_table, out_relationship_class, relationship_type, forward_label, backward_label, message_direction, cardinality, attributed, origin_primary_key, origin_foreign_key, {destination_primary_key}, {destination_foreign_key})

        Creates a relationship class to store an association between fields or
        features in the origin table and the destination table.

     INPUTS:
      origin_table (Table View):
          The table or feature class that is associated with the destination
          table.
      destination_table (Table View):
          The table that is associated with the origin table.
      relationship_type (String):
          Specifies the type of relationship that will be created between the
          origin and destination tables.SIMPLE-The origin and destination tables
          will have a simple
          relationship. This is the default.COMPOSITE-The origin and destination
          tables will have a composite
          relationship.
      forward_label (String):
          A name to uniquely identify the relationship when navigating from the
          origin table to the destination table.
      backward_label (String):
          A name to uniquely identify the relationship when navigating from the
          destination table to the origin table.
      message_direction (String):
          Specifies the direction in which messages will be passed between the
          origin and destination tables. For example, in a relationship between
          poles and transformers, when a pole is deleted, a message will be sent
          to its related transformer objects indicating that it was
          deleted.FORWARD-Messages will be passed from the origin table to the
          destination table.BACKWARD-Messages will be passed from the
          destination table to the
          origin table.BOTH-Messages will be passed from the origin table to the
          destination
          table and from the destination table to the origin table.NONE-No
          messages will be passed. This is the default.
      cardinality (String):
          Specifies how many relationships will exist between rows or features
          in the origin table and rows or features in the destination
          table.ONE_TO_ONE-Each row or feature in the origin table can be
          related to
          zero or one row or feature in the destination table. This is the
          default.ONE_TO_MANY-Each row or feature in the origin table can be
          related to
          one or several rows or features in the destination
          table.MANY_TO_MANY-Several rows or features in the origin table can be
          related to one or several rows or features in the destination table.
      attributed (Boolean):
          Specifies whether the relationship class will have attributes.NONE-The
          relationship class will not have attributes. This is the
          default.ATTRIBUTED-The relationship class will have attributes.
      origin_primary_key (String):
          For many-to-many or attributed relationship classes, this is the field
          in the origin table that links to the origin_foreign_key field in the
          relationship class table.For one-to-one or one-to-many relationship
          classes that are not
          attributed, this is the field in the origin table that links to the
          origin_foreign_key field in the destination table.
      origin_foreign_key (String):
          For many-to-many or attributed relationship classes, this is the field
          in the relationship class table that links to the origin_primary_key
          field in the origin table.For one-to-one or one-to-many relationship
          classes that are not
          attributed, this is the field in the destination table that links to
          the origin_primary_key field in the origin table.
      destination_primary_key {String}:
          The field in the destination table that links to the
          destination_foreign_key field in the relationship class table. This
          value is required for many-to-many or attributed relationship classes,
          but should be left empty for one-to-one or one-to-many relationship
          classes that are not attributed.
      destination_foreign_key {String}:
          The field in the relationship class table that links to the
          destination_primary_key field in the destination table. This value is
          required for many-to-many or attributed relationship classes, but
          should be left empty for one-to-one or one-to-many relationship
          classes that are not attributed.

     OUTPUTS:
      out_relationship_class (Relationship Class):
          The relationship class that will be created.

        """