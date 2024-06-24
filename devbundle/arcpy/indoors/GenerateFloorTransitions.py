# Generated documentation for module arcpy.indoors


class GenerateFloorTransitions(object):
    """
    Creates or updates transition line features that connect floors vertically.
    """

    @property
    def description(self) -> str:
        return """

        GenerateFloorTransitions_indoors(facility_features, transition_unit_features, pathway_features, target_transitions, {elevator_delay}, {delete_existing_transitions}, {stairway_unit_exp}, {elevator_unit_exp})

        Creates or updates transition line features that connect floors
        vertically.

     INPUTS:
      facility_features (Feature Layer):
          The input polygon features representing a facility or facilities. In
          the Indoors model, this is the Facilities layer. Only the facilities
          represented by these features will be processed.
      transition_unit_features (Feature Layer):
          The input polygon features representing the transition spaces in a
          facility. In the Indoors model, this is the Units layer.
      pathway_features (Feature Layer):
          The input polyline features representing preliminary pathways. The new
          transition features will snap to these polyline features. In the
          Indoors model, this is the PrelimPathways layer.
      target_transitions (Feature Layer):
          An existing feature class or layer that will be updated with the new
          transitions. In the Indoors model, this is the PrelimTransitions
          layer.
      elevator_delay {Long}:
          The average elevator transit time. It is one-half the time in seconds
          that an elevator passenger can expect to spend waiting to enter and
          exit the elevator. Using this parameter can improve routing and
          transit time calculations. The value must be equal to or greater than
          zero.
      delete_existing_transitions {Boolean}:
          Specifies whether existing transition features in selected transition
          spaces will be deleted before creating new transition features. If
          this parameter is not used, the updated_transitions value will include
          both existing and newly created transition
          features.DELETE_FEATURES-Existing transition features will be deleted.
          This is
          the default.NO_DELETE_FEATURES-Existing transition features will not
          be deleted.
      stairway_unit_exp {SQL Expression}:
          An SQL expression used to define whichvalues represent step-
          based transitions, such as stairs and escalators. Transition
          Unit Features
      elevator_unit_exp {SQL Expression}:
          An SQL expression used to define whichvalues represent lift-
          based transitions, such as elevators. Transition Unit Features

        """