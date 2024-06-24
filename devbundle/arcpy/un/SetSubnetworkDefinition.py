# Generated documentation for module arcpy.un


class SetSubnetworkDefinition(object):
    """
    Sets the domain network tier's properties for a subnetwork in a utility network.
    """

    @property
    def description(self) -> str:
        return """

        SetSubnetworkDefinition_un(in_utility_network, domain_network, tier_name, support_disjoint_subnetwork, {valid_devices;valid_devices...}, {valid_subnetwork_controller;valid_subnetwork_controller...}, {valid_lines;valid_lines...}, {aggregated_line;aggregated_line...}, {diagram_template;diagram_template...}, {summaries;summaries...}, {condition_barriers;condition_barriers...}, {function_barriers;function_barriers...}, {include_barriers}, {traversability_scope}, {propagators;propagators...}, {update_structure_features}, {update_container_features}, {edit_mode_for_default_version}, {edit_mode_for_named_version}, {valid_junctions;valid_junctions...}, {valid_junction_objects;valid_junction_objects...}, {valid_junction_object_subnetwork_controller;valid_junction_object_subnetwork_controller...}, {valid_edge_objects;valid_edge_objects...}, {manage_subnetwork_isdirty}, {include_containers}, {include_content}, {include_structures}, {validate_locatability})

        Sets the domain network tier's properties for a subnetwork in a
        utility network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The input utility network that contains the tier's subnetwork.
      domain_network (String):
          The domain network that contains the tier.
      tier_name (String):
          The name of the tier that contains the subnetwork.
      support_disjoint_subnetwork (Boolean):
          Specifies whether the input tier will support disjoint subnetworks.
          Disjoint subnetworks are two or more subnetworks that belong to the
          same tier and have the same subnetwork name but are not traversable.
          This parameter is only available for tiers in domain networks with a
          partitioned tier definition. This parameter is set to SUPPORT_DISJOINT
          by default for tiers in a domain network with a hierarchical tier
          definition to support disjoint subnetworks.SUPPORT_DISJOINT-The input
          tier will support disjoint
          subnetworks.NO_DISJOINT-The input tier will not support disjoint
          subnetworks. This
          is the default except as noted.
      valid_devices {String}:
          The asset group/asset type pairs identified as valid devices for the
          subnetwork.
      valid_subnetwork_controller {String}:
          The asset group/asset type pairs identified as valid device subnetwork
          controllers in the subnetwork.
      valid_lines {String}:
          The asset group/asset type pairs identified as valid lines for the
          subnetwork.
      aggregated_line {String}:
          The valid lines with geometry that will be aggregated to generate the
          SubnetLine features. This list is a subset of the values specified in
          the valid_lines parameter.
      diagram_template {String}:
          The templates that will be used to generate subnetwork system diagrams
          for each subnetwork.
      summaries {Value Table}:
          Sets the Summary Attribute field to store function results when
          inserting or updating SubnetLine features. The summaries can be
          calculated on all the features in the subnetwork. Calculations can be
          filtered to apply only to network features with a particular attribute
          value or category. Summaries components are as follows:
          Function-Choose
          from a number of calculation
          functions.Attribute-Filter by any network attribute defined in the
          system.Filter Name-Filter the function results by attribute
          name.Filter Operator-Choose from a number of operators.Filter
          Type-Choose from a number of filter types.Filter Value-Provide a
          specific value for the input filter attribute.Summary Attribute-The
          field in the SubnetLine feature class that will
          persist the function result. Depending on the specified function and
          network attribute type, only the applicable type of user-added
          subnetwork attributes will be valid for this parameter. If a field to
          store the summary result does not exist in the SubnetLine feature
          class, the Add Field tool can be used to create one. A field can only
          support the result of one summary; each summary requires its own field
          in the SubnetLine feature class. See the Usages section for a matrix
          of valid field types for the summary attribute field based on the
          specified function.The summaries Function value options are as
          follows:AVERAGE-The average of the input values will be
          calculated.COUNT-The
          number of features will be identified.MAX-The maximum of the input
          values will be identified.MIN-The minimum of the input values will be
          identified.ADD-The sum of the input values will be
          calculated.SUBTRACT-The difference of the input values will be
          calculated.
          Subnetwork controllers and loops trace types do not support the
          subtract function.The summaries Filter Operator value options are as
          follows:IS_EQUAL_TO-The attribute is equal to the
          value.DOES_NOT_EQUAL-The
          attribute is not equal to the value.IS_GREATER_THAN-The attribute is
          greater than the value.IS_GREATER_THAN_OR_EQUAL_TO-The attribute is
          greater than or equal to
          the value.IS_LESS_THAN-The attribute is less than the
          value.IS_LESS_THAN_OR_EQUAL_TO-The attribute is less than or equal to
          the
          value.INCLUDES_THE_VALUES-A bitwise AND operation in which all bits in
          the
          value are present in the attribute (bitwise AND ==
          value).DOES_NOT_INCLUDE_THE_VALUES-A bitwise AND operation in which
          not all
          of the bits in the value are present in the attribute (bitwise AND !=
          value).INCLUDES_ANY-A bitwise AND operation in which at least one bit
          in the
          value is present in the attribute (bitwise AND ==
          True).DOES_NOT_INCLUDE_ANY-A bitwise AND operation in which none of
          the bits
          in the value are present in the attribute (bitwise AND == False).The
          summaries Filter Type value options are as
          follows:SPECIFIC_VALUE-Filter by a specific
          value.NETWORK_ATTRIBUTE-Filter by
          a network attribute.
      condition_barriers {Value Table}:
          Sets a traversability barrier condition on features based on a
          comparison to a network attribute or check for a category string. A
          condition barrier uses a network attribute, an operator and a type,
          and an attribute value. For example, stop a trace when a feature has
          theattribute equal to the specific value of Open. When a feature meets
          this condition, the trace stops. If you're using more than one
          attribute, you can use theparameter to define an And or an Or
          condition. Device StatusCombine using        Condition barrier
          components are as follows:
          Name-Filter by any network attribute or network category defined in
          the system.Operator-Choose from a number of operators.Type-Choose a
          specific value or network attribute from the value that
          is specified in the name parameter.Value-Provide a specific value of
          the input attribute type that would
          cause termination based on the operator value.Combine Using-Set this
          value if you have multiple attributes to add.
          You can combine them using an And or an Or condition.The condition
          barriers Operator values are as follows:IS_EQUAL_TO-The attribute is
          equal to the value.DOES_NOT_EQUAL-The
          attribute is not equal to the value.IS_GREATER_THAN-The attribute is
          greater than the value.IS_GREATER_THAN_OR_EQUAL_TO-The attribute is
          greater than or equal to
          the value.IS_LESS_THAN-The attribute is less than the
          value.IS_LESS_THAN_OR_EQUAL_TO-The attribute is less than or equal to
          the
          value.INCLUDES_THE_VALUES-A bitwise AND operation in which all bits in
          the
          value are present in the attribute (bitwise AND ==
          value).DOES_NOT_INCLUDE_THE_VALUES-A bitwise AND operation in which
          not all
          of the bits in the value are present in the attribute (bitwise AND !=
          value).INCLUDES_ANY-A bitwise AND operation in which at least one bit
          in the
          value is present in the attribute (bitwise AND ==
          True).DOES_NOT_INCLUDE_ANY-A bitwise AND operation in which none of
          the bits
          in the value are present in the attribute (bitwise AND == False).The
          condition barriers Type value options are as
          follows:SPECIFIC_VALUE-Filter by a specific
          value.NETWORK_ATTRIBUTE-Filter by
          a network attribute.The Combine Using values are as
          follows:AND-Combine the condition barriers.OR-Use if either condition
          barrier
          is met.
      function_barriers {Value Table}:
          Sets a traversability barrier on features based on a function.
          Function barriers can be used to do such things as restrict how far
          the trace travels from the starting point, or set a maximum value to
          stop a trace. For example, the length of each line traveled is added
          to the total distance traveled so far. When the total length traveled
          reaches the value specified, the trace stops. Function barrier
          components are as follows:
          Function-Choose from a number of calculation
          functions.Attribute-Filter by any network attribute defined in the
          system.Operator-Choose from a number of operators.Value-Provide a
          specific value of the input attribute type that, if
          discovered, will cause the termination.Use Local Values-Calculate
          values in each direction as opposed to an
          overall global value, for example, for a function barrier that is
          calculating the sum of a shape length in which the trace terminates if
          the value is greater than or equal to 4. In the global case, after you
          have traversed two edges with a value of 2, you have already reached a
          shape length sum of 4, so the trace stops. If local values are used,
          the local values along each path change, and the trace continues.The
          function barrier Function value options are as follows:AVERAGE-The
          average of the input values will be calculated.COUNT-The
          number of features will be identified.MAX-The maximum of the input
          values will be identified.MIN-The minimum of the input values will be
          identified.ADD-The sum of the input values will be calculated.
          SUBTRACT-The difference in the input values will be
          calculated. Subnetwork controllers and loops trace types do
          not support the
          subtract function.The function barrier Operator value options are as
          follows:IS_EQUAL_TO-The attribute is equal to the
          value.DOES_NOT_EQUAL-The
          attribute is not equal to the value.IS_GREATER_THAN-The attribute is
          greater than the value.IS_GREATER_THAN_OR_EQUAL_TO-The attribute is
          greater than or equal to
          the value.IS_LESS_THAN-The attribute is less than the
          value.IS_LESS_THAN_OR_EQUAL_TO-The attribute is less than or equal to
          the
          value.INCLUDES_THE_VALUES-A bitwise AND operation in which all bits in
          the
          value are present in the attribute (bitwise AND ==
          value).DOES_NOT_INCLUDE_THE_VALUES-A bitwise AND operation in which
          not all
          of the bits in the value are present in the attribute (bitwise AND !=
          value).INCLUDES_ANY-A bitwise AND operation in which at least one bit
          in the
          value is present in the attribute (bitwise AND ==
          True).DOES_NOT_INCLUDE_ANY-A bitwise AND operation in which none of
          the bits
          in the value are present in the attribute (bitwise AND == False).The
          function barrier Use Local Values value options are as
          follows:TRUE-Use local values.FALSE-Use global values. This is the
          default.
      include_barriers {Boolean}:
          Specifies whether the traversability barrier features will be included
          in the trace results. Traversability barriers are optional even if
          they have been preset in the subnetwork
          definition.INCLUDE_BARRIERS-Traversability barriers will be included
          in the trace
          results. This is the default.EXCLUDE_BARRIERS-Traversability barriers
          will not be included in the
          trace results.
      traversability_scope {String}:
          The type of traversability that will be applied. Traversability scope
          determines whether traversability is applied at junctions, edges, or
          both. For example, if a condition barrier is defined to stop the trace
          if Device Status is equal to Open and traversability scope is set to
          edges only, the trace will not stop-even if it encounters an open
          device-because Device Status is only applicable to junctions. In other
          words, this parameter indicates to the trace whether to ignore
          junctions, edges, or both.BOTH_JUNCTIONS_AND_EDGES-Traversability will
          be applied to both
          junctions and edges. This is the default.JUNCTIONS_ONLY-Traversability
          will be applied to junctions only.EDGES_ONLY-Traversability will be
          applied to edges only.
      propagators {Value Table}:
          Specifies the network attributes to propagate as well as how that
          propagation will occur during a trace. Propagated class attributes
          denote the key values on subnetwork controllers that are disseminated
          to the rest of the features in the subnetwork. For example, in an
          electric distribution model, you can propagate the phase value.
          Propagators components are as follows:        Attribute-Filter
          by any network attribute defined in the
          system.Substitution Attribute-Use a substituted value instead of
          bitset
          network attribute values. Substitutions are encoded based on the
          number of bits in the network attribute being propagated. A
          substitution is a mapping of each bit in a phase to another bit. For
          example, for Phase AC, one substitution could map bit A to B and bit C
          to null. In this example, the substitution for 1010 (Phase AC) is
          0000-0010-0000-0000 (512). The substitution captures the mapping so
          you know that Phase A was mapped to B and Phase C was mapped to null
          and not the opposite (that is, Phase A was not mapped to null and
          Phase C was not mapped to B).Function-Choose from a number of
          calculation functions.Operator-Choose from a number of
          operators.Value-Provide a specific value for the input attribute type
          that would
          cause termination based on the operator value.Propagated Attribute-The
          name of the field in the network class that
          is used to store the calculated propagated values. The field type
          should be the same as the field type of the network attribute
          specified for the Attribute value.The propagators Function value
          options are as follows:PROPAGATED_BITWISE_AND-The values of one
          feature to the next will be
          compared.PROPAGATED_MIN-Get the minimum value.PROPAGATED_MAX-Get the
          maximum value.The propagators Operator value options are as
          follows:IS_EQUAL_TO-The attribute is equal to the
          value.DOES_NOT_EQUAL-The
          attribute is not equal to the value.IS_GREATER_THAN-The attribute is
          greater than the value.IS_GREATER_THAN_OR_EQUAL_TO-The attribute is
          greater than or equal to
          the value.IS_LESS_THAN-The attribute is less than the
          value.IS_LESS_THAN_OR_EQUAL_TO-The attribute is less than or equal to
          the
          value.INCLUDES_THE_VALUES-A bitwise AND operation in which all bits in
          the
          value are present in the attribute (bitwise AND ==
          value).DOES_NOT_INCLUDE_THE_VALUES-A bitwise AND operation in which
          not all
          of the bits in the value are present in the attribute (bitwise AND !=
          value).INCLUDES_ANY-A bitwise AND operation in which at least one bit
          in the
          value is present in the attribute (bitwise AND ==
          True).DOES_NOT_INCLUDE_ANY-A bitwise AND operation in which none of
          the bits
          in the value are present in the attribute (bitwise AND == False).This
          parameter is only available in Python.
      update_structure_features {Boolean}:
          Specifies whether the update subnetwork process will update the
          supported subnetwork name attribute for structure network
          containers.UPDATE-The structure network containers will be updated.
          This is the
          default.NOT_UPDATE-The structure network containers will not be
          updated. This parameter requires avalue of 4 or later.
          Utility
          Network Version
      update_container_features {Boolean}:
          Specifies whether the update subnetwork process will update the
          supported subnetwork name for domain network containers.UPDATE-The
          domain network containers will be updated. This is the
          default.NOT_UPDATE-The domain network containers will not be updated.
          This parameter requires avalue of 4 or later. Utility
          Network Version
      edit_mode_for_default_version {String}:
          Specifies the edit mode that will be used for subnetwork updates on
          the default version and with file and mobile
          geodatabases.WITHOUT_EVENTING-Eventing will not be used for subnetwork
          updates on
          the default version or in a file or mobile geodatabase. This edit mode
          updates the subnetwork name and propagated values in place. This is
          the default.WITH_EVENTING-Eventing will be used for subnetwork updates
          on the
          default version and in a file or mobile geodatabase. This edit mode
          applies geodatabase behavior (for example, attribute rules, editor
          tracking, and so on) when the subnetwork is updated and updates the
          subnetwork name and propagated values for all applicable features and
          objects. This parameter requires avalue of 4 or later.
          Utility
          Network Version
      edit_mode_for_named_version {String}:
          Specifies the edit mode that will be used for subnetwork updates on a
          named version.WITHOUT_EVENTING-Eventing will not be used for
          subnetwork updates on
          named versions. This edit mode updates the subnetwork name and
          propagated values in place for features and objects edited in the
          version. This is the default.WITH_EVENTING-Eventing will be used for
          subnetwork updates on named
          versions. This edit mode applies geodatabase behavior (for example,
          attribute rules, editor tracking, and so on) when the subnetwork is
          updated and updates the subnetwork name and propagated values for all
          applicable features and objects. This parameter requires avalue
          of 4 or later and is only
          applicable to enterprise geodatabases. Utility Network Version
      valid_junctions {String}:
          The asset group/asset type pairs identified as valid junctions for the
          subnetwork. This parameter requires avalue of 4 or later.
          Utility
          Network Version
      valid_junction_objects {String}:
          The asset group/asset type pairs identified as valid junction objects
          for the subnetwork. This parameter requires avalue of 4 or
          later. Utility
          Network Version
      valid_junction_object_subnetwork_controller {String}:
          The asset group/asset type pairs identified as valid junction object
          subnetwork controllers for the subnetwork. This parameter
          requires avalue of 4 or later. Utility
          Network Version
      valid_edge_objects {String}:
          The asset group/asset type pairs identified as valid edge objects for
          the subnetwork. This parameter requires avalue of 4 or later.
          Utility
          Network Version
      manage_subnetwork_isdirty {Boolean}:
          Specifies whether theattribute in the subnetworks table will
          be managed by the update subnetwork operation. If no subnetwork
          controllers are defined for the tier, the NOT_MANAGE option is used by
          default. Is dirty         MANAGE-Theattribute will be managed
          by the update subnetwork
          operation. This is the default except as noted. Is dirty
          NOT_MANAGE-Theattribute will not be managed by the update
          subnetwork operation. Is dirty        This parameter requires
          avalue of 5 or later. Utility
          Network Version
      include_containers {Boolean}:
          Specifies whether the container features and objects will be included
          in the trace results.INCLUDE_CONTAINERS-Container features and
          objects will be included in
          the trace results.EXCLUDE_CONTAINERS-Container features and objects
          will not be
          included in the trace results. This is the default. This
          parameter requires avalue of 5 or later. Utility
          Network Version
      include_content {Boolean}:
          Specifies whether the trace will include content of containers in the
          results.INCLUDE_CONTENT-Content of container features and objects
          will be
          included in the trace results.EXCLUDE_CONTENT-Content of container
          features and objects will not be
          included in the trace results. This is the default. This
          parameter requires avalue of 5 or later. Utility
          Network Version
      include_structures {Boolean}:
          Specifies whether structure features and objects will be included in
          the trace results.INCLUDE_STRUCTURES-Structure features and objects
          will be included in
          the trace results.EXCLUDE_STRUCTURES-Structure features and objects
          will not be
          included in the trace results. This is the default. This
          parameter requires avalue of 5 or later. Utility
          Network Version
      validate_locatability {Boolean}:
          Specifies whether an error will be returned during a trace or update
          subnetwork operation if nonspatial junction or edge objects are
          encountered without the necessary containment, attachment, or
          connectivity association in their association hierarchy of the
          traversed objects. This option ensures that nonspatial objects
          returned by a trace or update subnetwork operation can be located
          through an association with features or other locatable
          objects.VALIDATE_LOCATABILITY-An error will be returned if nonspatial
          junction
          or edge objects are encountered without the necessary containment,
          attachment, or connectivity association in their association hierarchy
          of the traversed objects.DO_NOT_VALIDATE_LOCATABILITY-The trace will
          not check for unlocatable
          objects and will return results regardless of whether unlocatable
          objects are present in the association hierarchy of the traversed
          objects. This is the default. This parameter requires avalue of
          5 or later. Utility
          Network Version

        """