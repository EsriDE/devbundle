# Generated documentation for module arcpy.management


class EvaluateRules(object):
    """
    Evaluates geodatabase rules and functionality.
    """

    @property
    def description(self) -> str:
        return """

        EvaluateRules_management(in_workspace, evaluation_types;evaluation_types..., {extent}, {run_async})

        Evaluates geodatabase rules and functionality.

     INPUTS:
      in_workspace (Workspace):
          A file geodatabase, mobile geodatabase, or feature service URL. An
          example of a feature service URL is
          https://myserver/server/rest/services/myservicename/FeatureServer.
      evaluation_types (String):
          Specifies the types of evaluation that will be
          used.CALCULATION_RULES-Batch calculation attribute rules will be
          evaluated.VALIDATION_RULES-Validation attribute rules will be
          evaluated.
      extent {Extent}:
          The extent to be evaluated. If there is a selection in the map, only
          selected features within the specified extent will be
          evaluated.MAXOF-The maximum extent of all inputs will be
          used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      run_async {Boolean}:
          Specifies whether the evaluation will run synchronously or
          asynchronously. This parameter is only supported when the input
          workspace is a feature service.ASYNC-The evaluation will run
          asynchronously. This option dedicates
          server resources to run the evaluation with a longer time-out. Running
          asynchronously is recommended when evaluating large datasets that
          contain many features requiring calculation or validation. This is the
          default.SYNC-The evaluation will run synchronously. This option has a
          shorter
          time-out and is best used when evaluating an extent with a small
          number of features requiring calculation or validation.

        """