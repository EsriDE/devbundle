# Generated documentation for module arcpy.management


class AlterAttributeRule(object):
    """
    Alters the properties of an attribute rule.
    """

    @property
    def description(self) -> str:
        return """

        AlterAttributeRule_management(in_table, name, {description}, {error_number}, {error_message}, {tags;tags...}, {triggering_events;triggering_events...}, {script_expression}, {exclude_from_client_evaluation})

        Alters the properties of an attribute rule.

     INPUTS:
      in_table (Table View):
          The table containing the attribute rule that will be altered.
      name (String):
          The name of the attribute rule that will be altered.
      description {String}:
          The description of the attribute rule. To keep the current value of
          the description, leave this parameter empty. To clear the current
          value of the description, use the RESET keyword.RESET-Clear the value
          of the current rule description.
      error_number {String}:
          The error number of the attribute rule. To keep the current value of
          the error number, leave this parameter empty. To clear the current
          value of the error number for a calculation rule, use the RESET
          keyword. Error number is a required property for constraint and
          validation rules and cannot be cleared.RESET-Clear the value of the
          current rule error number.
      error_message {String}:
          The error message of the attribute rule. To keep the current value of
          the error message, leave this parameter empty. To clear the current
          value of the error message for a calculation rule, use the RESET
          keyword. Error message is a required property for constraint and
          validation rules and cannot be cleared.RESET-Clear the value of the
          current rule error message.
      tags {String}:
          The tags for the attribute rule. The new values will replace all
          existing tags; to keep any current tags, include them in this list.
          For multiple tags, use a semicolon delimiter, for example,
          Tag1;Tag2;Tag3. To keep the current tags, leave this parameter empty.
          To clear the current tags, use the RESET keyword.RESET-Clear the tags
          for the rule.
      triggering_events {String}:
          Specifies the editing events that will trigger the attribute rule to
          take effect. Triggering events are only applicable for constraint
          rules and immediate calculation rules. The new values will replace
          existing triggering events. To keep the current triggering events,
          leave this parameter empty.INSERT-The rule will be applied when a new
          feature is added.UPDATE-The
          rule will be applied when a feature is updated.DELETE-The rule will be
          applied when a feature is deleted.
      script_expression {Calculator Expression}:
          An Arcade expression that defines the rule. To keep the current
          expression, leave this parameter empty. If an expression is provided
          for this parameter, it will replace the existing Arcade expression of
          the rule. If you alter the script expression of a batch calculation or
          validation rule, the rule must be reevaluated.
      exclude_from_client_evaluation {Boolean}:
          Specifies whether the application will evaluate the rule locally
          before applying the edits to the workspace.The default for this
          parameter corresponds to the current value set
          for the rule. That is, if the input rule has the exclude from client
          evaluation parameter set to false, the default for this parameter will
          be INCLUDE so the rule will not be automatically excluded. This
          parameter is not applicable for validation rules or batch calculation
          rules.EXCLUDE-The rule will be excluded from client
          evaluation.INCLUDE-The
          rule will not be excluded from client evaluation.

        """