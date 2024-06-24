# Generated documentation for module arcpy.na


class Solve(object):
    """
    Solves the network analysis layer problem based on its network locations and properties.
    """

    @property
    def description(self) -> str:
        return """

        Solve_na(in_network_analysis_layer, {ignore_invalids}, {terminate_on_solve_error}, {simplification_tolerance}, {overrides})

        Solves the network analysis layer problem based on its network
        locations and properties.

     INPUTS:
      in_network_analysis_layer (Network Analyst Layer):
          The network analysis layer on which the analysis will be computed.
      ignore_invalids {Boolean}:
          Specifies whether invalid input locations will be ignored. Typically,
          locations are invalid if they cannot be located on the network. When
          invalid locations are ignored, the solver will skip them and attempt
          to perform the analysis using the remaining locations.SKIP-Invalid
          input locations will be ignored and only valid locations
          will be used.HALT-All input locations will be used. Any invalid
          locations will
          cause the solve to fail.The default value will match the
          ignoreInvalidLocations property of
          the designated in_network_analysis_layer value.
      terminate_on_solve_error {Boolean}:
          Specifies whether the tool will stop running and terminate if an error
          is encountered during the solve.TERMINATE-The tool will stop running
          and terminate when the solver
          encounters an error. This is the default. When you use this option,
          the Result object is not created when the tool terminates due to a
          solver error. Review the geoprocessing messages from the ArcPy
          object.CONTINUE-The tool will not fail and will continue to run when
          the
          solver encounters an error. All error messages returned by the solver
          will be converted to warning messages. When you use this option, the
          Result object is always created and the maxSeverity property of the
          Result object is set to 1. Use the getOutput method of the Result
          object with an index value of 1 to determine if the solve was
          successful.
      simplification_tolerance {Linear Unit}:
          The tolerance that determines the degree of simplification for the
          output geometry. If a tolerance is specified, it must be greater than
          zero. You can choose a preferred unit; the default unit is decimal
          degrees.Specifying a simplification tolerance tends to reduce the time
          it
          takes to render routes or service areas. The drawback, however, is
          that simplifying geometry removes vertices, which may lessen the
          spatial accuracy of the output at larger scales.Because a line with
          only two vertices cannot be simplified any
          further, this parameter has no effect on drawing times for single-
          segment output, such as straight-line routes, OD cost matrix lines,
          and location-allocation lines.
      overrides {String}:
          This parameter is for internal use only.

        """