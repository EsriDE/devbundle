# Generated documentation for module arcpy.management


class TableToRelationshipClass(object):
    """
    Creates an attributed relationship class from the origin, destination, and relationship tables.
    """

    @property
    def description(self) -> str:
        return """

        TableToRelationshipClass_management(origin_table, destination_table, out_relationship_class, relationship_type, forward_label, backward_label, message_direction, cardinality, relationship_table, attribute_fields;attribute_fields..., origin_primary_key, origin_foreign_key, destination_primary_key, destination_foreign_key)

        Creates an attributed relationship class from the origin, destination,
        and relationship tables.

     INPUTS:
      origin_table (Table View):
          The table or feature class that will be associated to the destination
          table.
      destination_table (Table View):
          The table or feature class that will be associated to the origin
          table.
      relationship_type (String):
          Specifies the type of association that will be created between the
          origin and destination tables.SIMPLE-Each object will be independent
          of each other (a parent-to-
          parent relationship). This is the default.COMPOSITE-The lifetime of
          one object will control the lifetime of its
          related object (a parent-child relationship).
      forward_label (String):
          A label describing the relationship as it is traversed from the origin
          table or feature class to the destination table or feature class.
      backward_label (String):
          A label describing the relationship as it is traversed from the
          destination table or feature class to the origin table or feature
          class.
      message_direction (String):
          Specifies the direction messages that will be propagated between the
          objects in the relationship. For example, in a relationship between
          poles and transformers, when the pole is deleted, it sends a message
          to its related transformer objects informing them it was
          deleted.NONE-No messages will be propagated. This is the
          default.FORWARD-Messages will be propagated from the origin to the
          destination.BACKWARD-Messages will be propagated from the destination
          to the
          origin.BOTH-Messages will be propagated from the origin to the
          destination
          and from the destination to the origin.
      cardinality (String):
          Specifies the cardinality of the relationship between the origin and
          destination.ONE_TO_ONE-Each object of the origin table or feature
          class can be
          related to zero or one object of the destination table or feature
          class. This is the default.ONE_TO_MANY-Each object of the origin table
          or feature class can be
          related to multiple objects in the destination table or feature
          class.MANY_TO_MANY-Multiple objects of the origin table or feature
          class can
          be related to multiple objects in the destination table or feature
          class.
      relationship_table (Table View):
          The table containing attributes that will be added to the relationship
          class.
      attribute_fields (Field):
          The names of the fields containing attribute values that will be added
          to the relationship class. The fields must be present in the
          relationship_table parameter value.
      origin_primary_key (String):
          The field in the origin table that will be used to create the
          relationship.
      origin_foreign_key (String):
          The name of the field in the relationship table that refers to the
          primary key field in the origin table or feature class. For table-
          based relationship classes, these values are used to populate the
          relationships in the relationship class so they cannot be null.
      destination_primary_key (String):
          The field in the destination table that will be used to create the
          relationship.
      destination_foreign_key (String):
          The field in the relationship table that refers to the primary key
          field in the destination table or feature class. For table-based
          relationship classes, these values are used to populate the
          relationships in the relationship class so they cannot be null.

     OUTPUTS:
      out_relationship_class (Relationship Class):
          The relationship class that will be created.

        """