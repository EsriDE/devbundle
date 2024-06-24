# Generated documentation for module arcpy.td


class SolveTerritories(object):
    """
    Solves the territory solution based on specified criteria such as attribute constraints or distance constraints.
    """

    @property
    def description(self) -> str:
        return """

        SolveTerritories_td(in_territory_solution, level, method, {number_territories}, {quality}, {iterations_limit}, {algorithm}, {candidate_solutions})

        Solves the territory solution based on specified criteria such as
        attribute constraints or distance constraints.

     INPUTS:
      in_territory_solution (Group Layer / Feature Dataset / String):
          The territory solution that will be used to solve territories.
      level (String):
          The level that will be used to solve territories.
      method (String):
          Specifies the method that will be used when calculating the number of
          territories.USER_DEFINED-The number of territories will be defined by
          the
          number_territories parameter value. This is the default.PREFERRED-The
          number of territories will be defined by the
          number_territories parameter value, but only territories that meet the
          criteria of the constraints will be created.OPTIMAL-The number of
          territories will be calculated automatically.OPTIMAL_MAX_COVERAGE-The
          number of territories will be calculated
          automatically using a maximum coverage of the base features.
      number_territories {Long}:
          The number of territories to be specified.
      quality {Long}:
          An integer between 1 and 200 that determines the performance of a
          solve operation. A lower value will provide better performance but
          quality may be affected. The default value is 100.
      iterations_limit {Long}:
          The number of times the territory search process will be repeated. For
          larger datasets, increasing the number is recommended to find an
          optimal solution. The default value is 50.
      algorithm {String}:
          Specifies the algorithm that will be used to solve the territory
          solution.CLASSIC-The original algorithm will be used to solve the
          territory
          solution. This is the default.GENETIC-A newer and more modern
          algorithm based on a genetic growth
          algorithm will be used to solve the territory solution.
      candidate_solutions {Long}:
          The number of possible solutions. For larger datasets, increasing this
          number will increase the search space and the probability of finding a
          better solution. The default is 10 and must be greater than 1. This
          parameter is only used when the algorithm parameter is set to GENETIC.

        """