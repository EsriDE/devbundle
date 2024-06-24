# Generated documentation for module arcpy.un


class AddTerminalConfiguration(object):
    """
    Adds a terminal configuration to an existing utility network.
    """

    @property
    def description(self) -> str:
        return """

        AddTerminalConfiguration_un(in_utility_network, terminal_configuration_name, traversability_model, {terminals_directional;terminals_directional...}, {terminals_bidirectional;terminals_bidirectional...}, {valid_paths;valid_paths...}, {default_path})

        Adds a terminal configuration to an existing utility network.

     INPUTS:
      in_utility_network (Utility Network / Utility Network Layer):
          The input utility network to which the terminal configuration will be
          added.
      terminal_configuration_name (String):
          The name of the terminal configuration.
      traversability_model (String):
          Specifies the directionality of the terminal configuration. A
          directional traversability model means the flow for the terminal will
          only go in one direction. A bidirectional traversability model means
          the terminal allows flow in both directions.DIRECTIONAL-Only one flow
          direction is permitted.BIDIRECTIONAL-Both
          flow directions are permitted.
      terminals_directional {Value Table}:
          The name and directional flow of each directional terminal. A minimum
          of two terminals must be specified, and a maximum of eight can be
          specified. The name of each terminal cannot exceed 32 characters. This
          parameter is required if the traversability_model parameter value is
          DIRECTIONAL.Name-Provide the name of the terminal.
          Upstream-Indicate
          whether the terminal is upstream or
          downstream. True-The terminal is upstream.False-The terminal
          is downstream.
      terminals_bidirectional {Value Table}:
          The name of each bidirectional terminal. A minimum of two
          terminals must be specified, and a maximum of eight can be specified.
          The name of each terminal cannot exceed 32 characters. This parameter
          is required if theparameter value is(traversability_model =
          "BIDIRECTIONAL" in Python). DirectionalityBidirectional
      valid_paths {Value Table}:
          The name or names and valid path or paths for the terminal
          configuration. For bidirectional traversability, this parameter is
          required if you have three or four terminals. If you are using
          directional traversability, one of the terminals must be upstream to
          have valid configurations. Valid paths must be created to indicate
          which path or paths in a device or junction object are valid for a
          resource to travel through. Provide a name for each valid path as well
          as a value.Name-The name of the valid path. Value-The value of
          the valid
          path. All-Enter a value
          of All to create an option that indicates all paths
          are valid.None-Enter a value of None to create an option that
          indicates that no
          paths are valid.Terminal pair(s)-Enter a single or collection of
          terminal pairs. Enter
          a single terminal pair by specifying the path from one terminal to
          another separated by a hyphen, for example, A-B. Enter a collection of
          terminal pairs separated by a comma, for example, A-B, A-C.
      default_path {String}:
          The default path of the valid configurations. This will be assigned to
          new features that have this terminal configuration assigned to their
          asset type. If no valid paths have been specified, the default path
          All will be used.ALL-All paths are valid. This is the default.NONE-No
          paths are valid.

        """