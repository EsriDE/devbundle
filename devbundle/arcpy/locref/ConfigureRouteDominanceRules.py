# Generated documentation for module arcpy.locref


class ConfigureRouteDominanceRules(object):
    """
    Configures a set of rules to determine the dominant route in a network where there are concurrent routes.
    """

    @property
    def description(self) -> str:
        return """

        ConfigureRouteDominanceRules_locref(in_feature_class, configure_type, rule_name, {updated_rule_name}, {source_table_name}, {fields;fields...}, {order_method}, {order_type}, {prioritized_exceptions})

        Configures a set of rules to determine the dominant route in a network
        where there are concurrent routes.

     INPUTS:
      in_feature_class (Feature Layer):
          The input feature class. Only a registered LRS Network feature class
          can be used.
      configure_type (String):
          Specifies the type of configuration that will be applied to the
          in_feature_class parameter value.ADD-A new rule will be added to the
          configuration.UPDATE-An existing
          rule will be updated.DELETE-An existing rule will be deleted.
      rule_name (String):
          The name of the rule that will be added, updated, or deleted. The rule
          name can be up to 30 characters.
      updated_rule_name {String}:
          The updated name of the rule. This parameter is only used when UPDATE
          is specified as the configure_type parameter value.
      source_table_name {String}:
          The source event table or feature class registered to the
          in_feature_class parameter value. Alternatively, the network feature
          class can be used. Only nonspanning line events are supported.
      fields {String}:
          The attribute field aliases in the source table. If multiple fields
          are used, they will be concatenated.
      order_method {String}:
          Specifies whether route dominance ordering will be determined by
          lesser or greater values.
      order_type {String}:
          Specifies the ordering type that will be used when evaluating numeric
          or alphanumeric strings.
      prioritized_exceptions {String}:
          A comma-separated list of user-provided exceptions.

        """