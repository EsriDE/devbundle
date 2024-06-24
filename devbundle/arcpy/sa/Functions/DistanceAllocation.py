# Generated documentation for module arcpy.sa.Functions


class DistanceAllocation(object):
    """
    Calculates distance allocation for each cell to the provided sources based on straight-line distance, cost distance, and true surface distance, as well as vertical and horizontal cost factors.
    """

    @property
    def description(self) -> str:
        return """

        DistanceAllocation_sa(in_source_data, {in_barrier_data}, {in_surface_raster}, {in_cost_raster}, {in_vertical_raster}, {vertical_factor}, {in_horizontal_raster}, {horizontal_factor}, {out_distance_accumulation_raster}, {out_back_direction_raster}, {out_source_direction_raster}, {out_source_location_raster}, {source_field}, {source_initial_accumulation}, {source_maximum_accumulation}, {source_cost_multiplier}, {source_direction}, {distance_method})

        Calculates distance allocation for each cell to the provided sources
        based on straight-line distance, cost distance, and true surface
        distance, as well as vertical and horizontal cost factors.

     INPUTS:
      in_source_data (Composite Geodataset):
          The input source locations.This is a raster or feature (point, line,
          or polygon) identifying the
          cells or locations that will be used to calculate the least
          accumulated cost distance for each output cell location.For rasters,
          the input type can be integer or floating point.
      in_barrier_data {Composite Geodataset}:
          The dataset that defines the barriers.The barriers can be defined by
          an integer or a floating-point raster,
          or by a point, line, or polygon feature.For a raster barrier, the
          barrier must have a valid value, including
          zero, and the areas that are not barriers must be NoData.
      in_surface_raster {Composite Geodataset}:
          A raster defining the elevation values at each cell location.The
          values are used to calculate the actual surface distance covered
          when passing between cells.
      in_cost_raster {Composite Geodataset}:
          A raster defining the impedance or cost to move planimetrically
          through each cell.The value at each cell location represents the cost-
          per-unit distance
          for moving through the cell. Each cell location value is multiplied by
          the cell resolution while also compensating for diagonal movement to
          obtain the total cost of passing through the cell.The values of the
          cost raster can be integer or floating point, but
          they cannot be negative or zero (you cannot have a negative or zero
          cost).
      in_vertical_raster {Composite Geodataset}:
          A raster defining the z-values for each cell location.The values are
          used for calculating the slope used to identify the
          vertical factor incurred when moving from one cell to another.
      vertical_factor {Vertical Factor}:
          The Vertical factor object defines the relationship between the
          vertical cost factor and the vertical relative moving angle
          (VRMA).There are several factors with modifiers that identify a
          defined
          vertical factor graph. Additionally, a table can be used to create a
          custom graph. The graphs are used to identify the vertical factor used
          in calculating the total cost for moving into a neighboring cell.In
          the descriptions below, two acronyms are used: VF stands for
          vertical factor, which defines the vertical difficulty encountered in
          moving from one cell to the next; and VRMA stands for vertical
          relative moving angle, which identifies the slope angle between the
          FROM or processing cell and the TO cell. The object comes in
          the following forms:        VfBinary,
          VfLinear, VfInverseLinear, VfSymLinear, VfSymInverseLinear,
          VfCos, VfSec, VfSec, VfCosSec, VfSecCos, VfHikingTime,
          VfBidirHikingTime, VfTable.The definitions and parameters of these are
          the following:         VfBinary({zeroFactor}, {lowCutAngle},
          {highCutAngle})
          If the VRMA is greater than the low-cut angle and less than the high-
          cut angle, the VF is set to the value associated with the zero factor;
          otherwise, it is infinity. VfLinear({zeroFactor},
          {lowCutAngle}, {highCutAngle},
          {slope})         The VF is a linear function of the VRMA.
          VfInverseLinear({zeroFactor}, {lowCutAngle}, {highCutAngle},
          {slope})         The VF is an inverse linear function of the VRMA.
          VfSymLinear({zeroFactor}, {lowCutAngle}, {highCutAngle},
          {slope})         The VF is a linear function of the VRMA in either the
          negative or
          positive side of the VRMA, respectively, and the two linear functions
          are symmetrical with respect to the VF (y) axis.
          VfSymInverseLinear({zeroFactor}, {lowCutAngle},
          {highCutAngle}, {slope})         The VF is an inverse linear function
          of the VRMA in either the
          negative or positive side of the VRMA, respectively, and the two
          linear functions are symmetrical with respect to the VF (y) axis.
          VfCos({lowCutAngle}, {highCutAngle}, {cosPower})         The
          VF is the cosine-based function of the VRMA.
          VfSec({lowCutAngle}, {highCutAngle}, {secPower})         The
          VF is the secant-based function of the VRMA.
          VfCosSec({lowCutAngle}, {highCutAngle}, {cosPower},
          {secPower})         The VF is the cosine-based function of the VRMA
          when the VRMA is
          negative and is the secant-based function of the VRMA when the VRMA is
          not negative. VfSecCos({lowCutAngle}, {highCutAngle},
          {secPower},
          {cos_power})         The VF is the secant-based function of the VRMA
          when the VRMA is
          negative and is the cosine-based function of the VRMA when the VRMA is
          not negative. VfHikingTime({lowCutAngle}, {highCutAngle})
          The VF is
          the hiking time function of the VRMA.
          VfBidirHikingTime({lowCutAngle}, {highCutAngle})         The
          VF is a bidirectional modified hiking time function of the VRMA.
          VfTable(inTable)         A table file will be used to define
          the vertical-factor graph used to
          determine the VFs.The modifiers to the vertical parameters are the
          following:zeroFactor-The vertical factor used when the VRMA is zero.
          This factor
          positions the y-intercept of the specified function. By definition,
          the zero factor is not applicable to any of the trigonometric vertical
          functions (Cos, Sec, Cos-Sec, or Sec-Cos). The y-intercept is defined
          by these functions.lowCutAngle-The VRMA angle below which the VF will
          be set to infinity.highCutAngle-The VRMA angle above which the VF will
          be set to
          infinity.slope-The slope of the straight line used with the VfLinear
          and
          VfInverseLinear parameters. The slope is specified as a fraction of
          rise over run (for example, 45 percent slope is 1/45, which is input
          as 0.02222).inTable-The name of the table defining the VF.
      in_horizontal_raster {Composite Geodataset}:
          A raster defining the horizontal direction at each cell.The values on
          the raster must be integers ranging from 0 to 360, with
          0 degrees being north, or toward the top of the screen, and increasing
          clockwise. Flat areas should be given a value of -1. The values at
          each location will be used in conjunction with the horizontal_factor
          parameter to determine the horizontal cost incurred when moving from a
          cell to its neighbors.
      horizontal_factor {Horizontal Factor}:
          The Horizontal Factor object defines the relationship between the
          horizontal cost factor and the horizontal relative moving angle.There
          are several factors with modifiers that identify a defined
          horizontal factor graph. Additionally, a table can be used to create a
          custom graph. The graphs are used to identify the horizontal factor
          used in calculating the total cost of moving into a neighboring
          cell.In the descriptions below, two acronyms are used: HF stands for
          horizontal factor, which defines the horizontal difficulty encountered
          when moving from one cell to the next; and HRMA stands for horizontal
          relative moving angle, which identifies the angle between the
          horizontal direction from a cell and the moving direction. The
          object comes in the following forms:        HfBinary,
          HfForward, HfLinear, HfInverseLinear, and HfTable. The
          definitions and parameters of these are the following:
          HfBinary({zeroFactor}, {cutAngle})          If the HRMA is
          less than the cut angle, the HF is set to the value
          associated with the zero factor; otherwise, it is infinity.
          HfForward({zeroFactor}, {sideValue})          Only forward
          movement is allowed. The HRMA must be greater than or
          equal to 0 and less than 90 (0 <= HRMA < 90). If the HRMA is greater
          than 0 and less than 45 degrees, the HF for the cell is set to the
          value associated with the zero factor. If the HRMA is greater than or
          equal to 45 degrees, the side value modifier value is used. The HF for
          any HRMA equal to or greater than 90 degrees is set to infinity.
          HfLinear({zeroFactor}, {cutAngle}, {slope})          The HF
          is a linear function of the HRMA.
          HfInverseLinear({zeroFactor}, {cutAngle}, {slope})
          The HF is an inverse linear function of the HRMA.
          HfTable(inTable)          A table file will be used to
          define the horizontal factor graph used
          to determine the HFs. The modifiers to the horizontal keywords
          are the following:
          zeroFactor-The horizontal factor to be used when the HRMA is 0. This
          factor positions the y-intercept for any of the horizontal factor
          functions.cutAngle-The HRMA angle beyond which the HF will be set to
          infinity.slope-The slope of the straight line used with the HfLinear
          and
          HfInverseLinear horizontal-factor keywords. The slope is specified as
          a fraction of rise over run (for example, 45 percent slope is 1/45,
          which is input as 0.02222).sideValue-The HF when the HRMA is greater
          than or equal to 45 degrees
          and less than 90 degrees when the HfForward horizontal-factor keyword
          is specified.inTable-The name of the table defining the HF.
      source_field {Field}:
          The field used to assign values to the source locations. It must be of
          integer type.
      source_initial_accumulation {Double / Field}:
          The initial accumulative cost that will be used to begin the cost
          calculation.Allows for the specification of the fixed cost associated
          with a
          source. Instead of starting at a cost of zero, the cost algorithm will
          begin with the value set by source_initial_accumulation.The values
          must be zero or greater. The default is 0.
      source_maximum_accumulation {Double / Field}:
          The maximum accumulation for the traveler for a source.The cost
          calculations continue for each source until the specified
          accumulation is reached.The values must be greater than zero. The
          default accumulation is to
          the edge of the output raster.
      source_cost_multiplier {Double / Field}:
          The multiplier that will be applied to the cost values.This allows for
          control of the mode of travel or the magnitude at a
          source. The greater the multiplier, the greater the cost to move
          through each cell.The values must be greater than zero. The default is
          1.
      source_direction {String / Field}:
          Specifies the direction of the traveler when applying horizontal and
          vertical factors.FROM_SOURCE-The horizontal factor and vertical factor
          will be applied
          beginning at the input source and travel out to the nonsource cells.
          This is the default.TO_SOURCE-The horizontal factor and vertical
          factor will be applied
          beginning at each nonsource cell and travel back to the input
          source.Specify the FROM_SOURCE or TO_SOURCE keyword, which will be
          applied to
          all sources, or specify a field in the source data that contains the
          keywords to identify the direction of travel for each source. That
          field must contain the string FROM_SOURCE or TO_SOURCE.
      distance_method {String}:
          Specifies whether the distance will be calculated using a planar (flat
          earth) or a geodesic (ellipsoid) method.PLANAR-The distance
          calculation will be performed on a projected flat
          plane using a 2D Cartesian coordinate system. This is the
          default.GEODESIC-The distance calculation will be performed on the
          ellipsoid.
          Regardless of input or output projection, the results will not change.

     OUTPUTS:
      out_distance_allocation_raster (Raster Dataset):
          The output distance allocation raster.
      out_distance_accumulation_raster {Raster Dataset}:
          The output distance raster.The distance accumulation raster contains
          the accumulative distance
          for each cell from, or to, the least-cost source.
      out_back_direction_raster {Raster Dataset}:
          The back direction raster contains the calculated direction in
          degrees. The direction identifies the next cell along the shortest
          path back to the closest source while avoiding barriers.The range of
          values is from 0 degrees to 360 degrees, with 0 reserved
          for the source cells. Due east (right) is 90, and the values increase
          clockwise (180 is south, 270 is west, and 360 is north).The output
          raster is of type float.
      out_source_direction_raster {Raster Dataset}:
          The source direction raster identifies the direction of the least
          accumulated cost source cell as an azimuth in degrees.The range of
          values is from 0 degrees to 360 degrees, with 0 reserved
          for the source cells. Due east (right) is 90, and the values increase
          clockwise (180 is south, 270 is west, and 360 is north).The output
          raster is of type float.
      out_source_location_raster {Raster Dataset}:
          The source location raster is a multiband output. The first band
          contains a row index, and the second band contains a column index.
          These indexes identify the location of the source cell that is the
          least accumulated cost distance away.

        """