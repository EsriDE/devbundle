# Generated documentation for module arcpy.management


class AddAttributeRule(object):
    """
    Adds an attribute rule to a dataset.
    """

    @property
    def description(self) -> str:
        return """

        AddAttributeRule_management(in_table, name, type, script_expression, {is_editable}, {triggering_events;triggering_events...}, {error_number}, {error_message}, {description}, {subtype}, {field}, {exclude_from_client_evaluation}, {batch}, {severity}, {tags;tags...})

        Adds an attribute rule to a dataset.

     INPUTS:
      in_table (Table View):
          The table or feature class that will have the new rule applied.
      name (String):
          A unique name for the new rule.
      type (String):
          Specifies the type of attribute rule that will be added.
          CALCULATION-Attribute values will be automatically populated
          for features when another attribute is set on a feature. These rules
          are applied based on the triggering events specified. Long running
          calculations can be set to run in batch mode and will be evaluated at
          a user-defined time. When adding multiple
          calculation rules, the order in which
          the rules are added is important if there are circular dependencies.
          For example, Rule A calculatesis equal to the value of $feature.Field2
          + $feature.Field3, and Rule B calculatesis equal to $feature.Field1 +
          $feature.Field5; the results of the calculation may be different
          depending on the order in which the rules are added.
          Field1Field4         CONSTRAINT-Permissible attribute configurations
          will be
          specified on a feature. When the constraint rule is violated, an error
          is generated and the feature is not stored. For example, if the value
          ofmust be less than the sum ofand, an error will be generated when
          that constraint is violated. Field AField BField
          CVALIDATION-Existing features will be identified with a batch
          validation process. Rules are evaluated at a user-defined time. When a
          rule is violated, an error feature is created.
      script_expression (Calculator Expression):
          The Arcade expression that defines the rule.
      is_editable {Boolean}:
          Specifies whether the attribute value can be edited. Attribute rules
          can be configured to either block or allow editors to edit the
          attribute values of the field being calculated. This parameter is only
          applicable for the calculation attribute rule type.EDITABLE-The
          attribute value can be edited. This is the
          default.NONEDITABLE-The attribute value cannot be edited.
      triggering_events {String}:
          Specifies the editing events that will trigger the attribute rule to
          take effect. This parameter is valid for calculation and constraint
          rule types only. At least one triggering event must be provided for
          calculation rules in which the batch parameter is set to NOT_BATCH.
          Triggering events are not applicable for calculation rules that have
          the batch parameter set to BATCH.INSERT-The rule will be applied when
          a new feature is added.UPDATE-The
          rule will be applied when a feature is updated.DELETE-The rule will be
          applied when a feature is deleted.
      error_number {String}:
          An error number that will be returned when this rule is violated. This
          value is not required to be unique, so the same custom error number
          may be returned for multiple rules.This parameter is required for the
          constraint and validation rule
          types. It is optional for the calculation rule type.
      error_message {String}:
          An error message that will be returned when this rule is violated. It
          is recommended that you use a descriptive message to help the editor
          understand the violation when it occurs. The message is limited to 256
          characters.This parameter is required for the constraint and
          validation rule
          types. It is optional for the calculation rule type.
      description {String}:
          The description of the new attribute rule. The description is limited
          to 256 characters.
      subtype {String}:
          The subtype to which the rule will be applied if the dataset has
          subtypes.
      field {String}:
          The name of an existing field to which the rule will be applied. This
          parameter is only applicable for the calculation attribute rule type.
      exclude_from_client_evaluation {Boolean}:
          Specifies whether the application will evaluate the rule locally
          before applying the edits to the workspace.Not all clients have the
          capability to run all of the available rules
          so authors can exclude certain rules from client evaluation. For
          example, some rules may refer to data that has not been made available
          to all clients (reasons can include the data is offline, size, or
          security), or some rules may depend on the user or context (that is, a
          lightweight field update in a data collection app may not run a rule
          that requires additional user input or knowledge; however, a client
          such as ArcGIS Pro may support it).This parameter is not applicable
          for validation rule or calculation
          rule types if the batch parameter value is set to BATCH.EXCLUDE-The
          rule will be excluded from client evaluation.INCLUDE-The
          rule will not be excluded from client evaluation. This is
          the default.
      batch {Boolean}:
          Specifies whether the rule evaluation will be run in batch
          mode.BATCH-The rule evaluation will be run in batch mode at a later
          time by
          running validate.NOT_BATCH-The rule evaluation will not be run in
          batch mode.
          Triggering events will be used to determine when the rule is evaluated
          for insert, update, or delete operations. This is the
          default.Calculation rules can be either BATCH or NOT_BATCH. Validation
          rules
          are always BATCH for this parameter, and constraint rules are always
          NOT_BATCH.
      severity {Long}:
          The severity of the error.A value within the range of 1 through 5 can
          be chosen to define the
          severity of the rule. A value of 1 is high, being the most severe, and
          a value of 5 is low, being the least severe. For example, you can
          provide a low severity for a specific attribute rule and ignore the
          error during data production workflows, or set a high severity in
          which the error must be fixed for accuracy of data collected.This
          parameter is only applicable to validation rules.
      tags {String}:
          A set of tags that identify the rule (for searching and indexing) as a
          way to map to a functional requirement in a data model. To enter
          multiple tags, use a semicolon delimiter, for example, Tag1;Tag2;Tag3.

        """