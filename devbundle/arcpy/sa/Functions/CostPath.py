# Generated documentation for module arcpy.sa.Functions


class CostPath(object):
    """
    Calculates the least-cost path from a source to a destination.
    """

    @property
    def description(self) -> str:
        return """

        CostPath_sa(in_destination_data, in_cost_distance_raster, in_cost_backlink_raster, {path_type}, {destination_field}, {force_flow_direction_convention})

        Calculates the least-cost path from a source to a destination.

     INPUTS:
      in_destination_data (Composite Geodataset):
          A raster or feature dataset that identifies those cells from which the
          least-cost path is determined to the least costly source.If the input
          is a raster, the input consists of cells that have valid
          values (zero is a valid value), and the remaining cells must be
          assigned NoData.
      in_cost_distance_raster (Composite Geodataset):
          The name of a cost distance raster to be used to determine the least-
          cost path from the destination locations to a source.The cost distance
          raster is usually created with the Cost Distance,
          Cost Allocation or Cost Back Link tools. The cost distance raster
          stores, for each cell, the minimum accumulative cost distance over a
          cost surface from each cell to a set of source cells.
      in_cost_backlink_raster (Composite Geodataset):
          The name of a cost back link raster used to determine the path to
          return to a source via the least-cost path.For each cell in the back
          link raster, a value identifies the neighbor
          that is the next cell on the least accumulative cost path from the
          cell to a single source cell or set of source cells.
      path_type {String}:
          A keyword defining the manner in which the values and zones on the
          input destination data will be interpreted in the cost path
          calculations.EACH_CELL-For each cell with valid values on the input
          destination
          data, a least-cost path is determined and saved on the output raster.
          With this option, each cell of the input destination data is treated
          separately, and a least-cost path is determined for each from
          cell.EACH_ZONE-For each zone on the input destination data, a least-
          cost
          path is determined and saved on the output raster. With this option,
          the least-cost path for each zone begins at the cell with the lowest
          cost distance weighting in the zone.BEST_SINGLE-For all cells on the
          input destination data, the least-
          cost path is derived from the cell with the minimum of the least-cost
          paths to source cells.
      destination_field {Field}:
          The field used to obtain values for the destination locations.Input
          feature data must contain at least one valid field.
      force_flow_direction_convention {Boolean}:
          Specifies whether the input backlink raster will be treated as a flow
          direction raster. Flow direction rasters can have integer values that
          range from 0-255.INPUT_RANGE-The in_cost_backlink_raster value will be
          interpreted
          based on the range of values and if it is integer or float. For a
          value range of 0-8, the in_cost_backlink_raster value will be treated
          as a backlink raster. For values 0-255 and integer, the
          in_cost_backlink_raster value will be treated as a flow direction
          raster. For a value range of 0-360 and floating point, the
          in_cost_backlink_raster value will be treated as a back direction
          raster.FLOW_DIRECTION-The raster supplied for the
          in_cost_backlink_raster
          parameter will be treated as a flow direction raster. This is
          necessary if the flow direction raster has a maximum value of 8 or
          less.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output cost path raster.The output raster is of integer type.

        """