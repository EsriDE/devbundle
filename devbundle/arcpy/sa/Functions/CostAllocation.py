# Generated documentation for module arcpy.sa.Functions


class CostAllocation(object):
    """
    Calculates, for each cell, its least-cost source based on the least accumulative cost over a cost surface.
    """

    @property
    def description(self) -> str:
        return """

        CostAllocation_sa(in_source_data, in_cost_raster, {maximum_distance}, {in_value_raster}, {source_field}, {out_distance_raster}, {out_backlink_raster}, {source_cost_multiplier}, {source_start_cost}, {source_resistance_rate}, {source_capacity}, {source_direction})

        Calculates, for each cell, its least-cost source based on the least
        accumulative cost over a cost surface.

     INPUTS:
      in_source_data (Composite Geodataset):
          The input source locations.This is a raster or feature (point, line,
          or polygon) identifying the
          cells or locations that will be used to calculate the least
          accumulated cost distance for each output cell location.For rasters,
          the input type can be integer or floating point.If the input source
          raster is floating point, the in_value_raster
          parameter must be set, and it must integer. The value raster will take
          precedence over the source_field parameter setting.
      in_cost_raster (Composite Geodataset):
          A raster defining the impedance or cost to move planimetrically
          through each cell.The value at each cell location represents the cost-
          per-unit distance
          for moving through the cell. Each cell location value is multiplied by
          the cell resolution while also compensating for diagonal movement to
          obtain the total cost of passing through the cell.The values of the
          cost raster can be integer or floating point, but
          they cannot be negative or zero (you cannot have a negative or zero
          cost).
      maximum_distance {Double}:
          The threshold that the accumulative cost values cannot exceed.If an
          accumulative cost distance value exceeds this value, the output
          value for the cell location will be NoData. The maximum distance is
          the extent for which the accumulative cost distances are
          calculated.The default distance is to the edge of the output raster.
      in_value_raster {Composite Geodataset}:
          The input integer raster that identifies the zone values that will be
          used for each input source location.For each source location (cell or
          feature), the in_value_raster value
          will be assigned to all cells allocated to the source location for the
          computation. The value raster will take precedence over the
          source_field parameter setting.
      source_field {Field}:
          The field used to assign values to the source locations. It must be of
          integer type.If the in_value_raster parameter has been set, the values
          in that
          input will have precedence over the source_field parameter setting.
      source_cost_multiplier {Double / Field}:
          The multiplier that will be applied to the cost values.This allows for
          control of the mode of travel or the magnitude at a
          source. The greater the multiplier, the greater the cost to move
          through each cell.The values must be greater than zero. The default is
          1.
      source_start_cost {Double / Field}:
          The starting cost that will be used to begin the cost
          calculations.Allows for the specification of the fixed cost associated
          with a
          source. Instead of starting at a cost of zero, the cost algorithm will
          begin with the value set by source_start_cost.The values must be zero
          or greater. The default is 0.
      source_resistance_rate {Double / Field}:
          This parameter simulates the increase in the effort to overcome costs
          as the accumulative cost increases. It is used to model fatigue of the
          traveler. The growing accumulative cost to reach a cell is multiplied
          by the resistance rate and added to the cost to move into the
          subsequent cell.It is a modified version of a compound interest rate
          formula that is
          used to calculate the apparent cost of moving through a cell. As the
          value of the resistance rate increases, it increases the cost of the
          cells that are visited later. The greater the resistance rate, the
          more additional cost is added to reach the next cell, which is
          compounded for each subsequent movement. Since the resistance rate is
          similar to a compound rate and generally the accumulative cost values
          are very large, small resistance rates are suggested, such as 0.02,
          0.005, or even smaller, depending on the accumulative cost values.The
          values must be zero or greater. The default is 0.
      source_capacity {Double / Field}:
          The cost capacity for the traveler for a source.The cost calculations
          continue for each source until the specified
          capacity is reached.The values must be greater than zero. The default
          capacity is to the
          edge of the output raster.
      source_direction {String / Field}:
          Specifies the direction of the traveler when applying the source
          resistance rate and the source starting cost.FROM_SOURCE-The source
          resistance rate and source starting cost will
          be applied beginning at the input source and travel out to the
          nonsource cells. This is the default.TO_SOURCE-The source resistance
          rate and source starting cost will be
          applied beginning at each nonsource cell and travel back to the input
          source.Specify the FROM_SOURCE or TO_SOURCE keyword, which will be
          applied to
          all sources, or specify a field in the source data that contains the
          keywords to identify the direction of travel for each source. That
          field must contain the string FROM_SOURCE or TO_SOURCE.

     OUTPUTS:
      out_allocation_raster (Raster Dataset):
          The output cost allocation raster.This raster identifies the zone of
          each source location (cell or
          feature) that could be reached with the least accumulative cost.The
          output raster is of integer type.
      out_distance_raster {Raster Dataset}:
          The output cost distance raster.The cost distance raster identifies,
          for each cell, the least
          accumulative cost distance over a cost surface to the identified
          source locations.A source can be a cell, a set of cells, or one or
          more feature
          locations.The output raster is of floating-point type.
      out_backlink_raster {Raster Dataset}:
          The output cost backlink raster.The backlink raster contains values 0
          through 8, which define the
          direction or identify the next neighboring cell (the succeeding cell)
          along the least accumulative cost path from a cell to reach its least-
          cost source.If the path is to pass into the right neighbor, the cell
          will be
          assigned the value 1, 2 for the lower right diagonal cell, and
          continue clockwise. The value 0 is reserved for source cells.

        """