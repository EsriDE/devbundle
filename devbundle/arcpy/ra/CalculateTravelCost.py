# Generated documentation for module arcpy.ra


class CalculateTravelCost(object):
    """
    Calculates the least accumulative cost distance from or to the least- cost source, while accounting for surface distance along with horizontal and vertical cost factors.
    """

    @property
    def description(self) -> str:
        return """

        CalculateTravelCost_ra(inputSourceRasterOrFeatures, outputDistanceName, {inputCostRaster}, {inputSurfaceRaster}, {maximumDistance}, {inputHorizontalRaster}, {horizontalFactor}, {inputVerticalRaster}, {verticalFactor}, {sourceCostMultiplier}, {sourceStartCost}, {sourceResistanceRate}, {sourceCapacity}, {sourceTravelDirection}, {outputBacklinkName}, {outputAllocationName}, {allocationField})

        Calculates the least accumulative cost distance from or to the least-
        cost source, while accounting for surface distance along with
        horizontal and vertical cost factors.

     INPUTS:
      inputSourceRasterOrFeatures (Image Service / Feature Layer / Raster Layer / String):
          The layer that defines the sources to calculate the distance to. The
          layer can be raster or feature.
      outputDistanceName (String):
          The name of the output distance raster service.The cost distance image
          service identifies, for each cell, the least
          accumulative cost distance over a cost surface to the identified
          source locations.
      inputCostRaster {Image Service / Raster Layer / String}:
          A raster defining the impedance or cost to move planimetrically
          through each cell.The value at each cell location represents the cost-
          per-unit distance
          for moving through the cell. Each cell location value is multiplied by
          the cell resolution while also compensating for diagonal movement to
          obtain the total cost of passing through the cell.The values of the
          cost raster can be integer or floating point, but
          they cannot be negative or zero (you cannot have a negative or zero
          cost).
      inputSurfaceRaster {Image Service / Raster Layer / String}:
          A raster defining the elevation values at each cell location. The
          values are used to calculate the actual surface distance covered when
          passing between cells.
      maximumDistance {Double}:
          Defines the threshold that the accumulative cost values cannot exceed.
      inputHorizontalRaster {Image Service / Raster Layer / String}:
          A raster defining the horizontal direction at each cell.The values on
          the raster must be integers ranging from 0 to 360, with
          0 degrees being north, or toward the top of the screen, and increasing
          clockwise. Flat areas should be given a value of -1.The values at each
          location will be used in conjunction with the
          {horizontal_factor} to determine the horizontal cost incurred when
          moving from a cell to its neighbors.
      horizontalFactor {Horizontal Factor}:
          The Horizontal Factor defines the relationship between the horizontal
          cost factor and the horizontal relative moving angle.There are several
          factors with modifiers from which to select that
          identify a defined horizontal factor graph. The graphs are used to
          identify the horizontal factor used in calculating the total cost of
          moving into a neighboring cell.In the explanations below, two acronyms
          are used: HF stands for
          horizontal factor, which defines the horizontal difficulty encountered
          when moving from one cell to the next; and HRMA stands for horizontal
          relative moving angle, which identifies the angle between the
          horizontal direction from a cell and the moving direction.There are
          several types of horizontal factor available:Binary-Indicates that if
          the HRMA is less than the cut angle, the HF
          is set to the value associated with the zero factor; otherwise, it is
          infinity.Forward-Establishes that only forward movement is allowed.
          The HRMA
          must be greater or equal to 0 and less than 90 degrees (0 <= HRMA <
          90). If the HRMA is greater than 0 and less than 45 degrees, the HF
          for the cell is set to the value associated with the zero factor. If
          the HRMA is greater than or equal to 45 degrees, the side value
          modifier value is used. The HF for any HRMA equal to or greater than
          90 degrees is set to infinity.Linear-Specifies that the HF is a linear
          function of the HRMA.Inverse Linear-Specifies that the HF is an
          inverse linear function of
          the HRMA.The default is Binary.Characteristics for the horizontal
          keywords:Zero factor-Establishes the horizontal factor to be used when
          the HRMA
          is zero. This factor positions the y-intercept for any of the
          horizontal factor functions.Cut angle-Defines the HRMA angle beyond
          which the HF will be set to
          infinity. Slope-Establishes the slope of the straight line
          used with
          theandhorizontal factor keywords. The slope is specified as a fraction
          of rise over run (for example, 45 percent slope is 1/45, which is
          input as 0.02222). LinearInverse Linear         Side
          value-Establishes the HF when the HRMA is greater than
          or equal to 45 degrees and less than 90 degrees when thehorizontal
          factor keyword is specified. Forward
      inputVerticalRaster {Image Service / Raster Layer / String}:
          A raster defining the vertical (z) value for each cell.
      verticalFactor {Vertical Factor}:
          The Vertical Factor defines the relationship between the vertical cost
          factor and the vertical relative moving angle (VRMA).There are several
          factors with modifiers from which to select that
          identify a defined vertical factor graph. The graphs are used to
          identify the vertical factor used in calculating the total cost for
          moving into a neighboring cell.In the explanations below, two acronyms
          are used: VF stands for
          vertical factor, which defines the vertical difficulty encountered in
          moving from one cell to the next; and VRMA stands for vertical
          relative moving angle, which identifies the slope angle between the
          FROM or processing cell and the TO cell.There are several types of
          vertical factor available:Binary-Specifies that if the VRMA is greater
          than the low-cut angle
          and less than the high-cut angle, the VF is set to the value
          associated with the zero factor; otherwise, it is
          infinity.Linear-Indicates that the VF is a linear function of the
          VRMA.Symmetric Linear-Specifies that the VF is a linear function of
          the
          VRMA in either the negative or positive side of the VRMA,
          respectively, and the two linear functions are symmetrical with
          respect to the VF (y) axis.Inverse Linear-Indicates that the VF is an
          inverse linear function of
          the VRMA.Symmetric Inverse Linear-Specifies that the VF is an inverse
          linear
          function of the VRMA in either the negative or positive side of the
          VRMA, respectively, and the two linear functions are symmetrical with
          respect to the VF (y) axis.Cos-Identifies the VF as the cosine-based
          function of the VRMA.Sec-Identifies the VF as the secant-based
          function of the VRMA.Cos-Sec-Specifies that the VF is the cosine-based
          function of the VRMA
          when the VRMA is negative and the secant-based function of the VRMA
          when the VRMA is nonnegative.Sec-Cos-Specifies that the VF is the
          secant-based function of the VRMA
          when the VRMA is negative and the cosine-based function of the VRMA
          when the VRMA is nonnegative.The default is Binary.Characteristics for
          the vertical keywords:Zero factor-Establishes the vertical factor used
          when the VRMA is
          zero. This factor positions the y-intercept of the specified function.
          By definition, the zero factor is not applicable to any of the
          trigonometric vertical functions (COS, SEC, COS-SEC, or SEC-COS). The
          y-intercept is defined by these functions.Low Cut angle-Defines the
          VRMA angle below which the VF will be set to
          infinity.High Cut angle-Defines the VRMA angle above which the VF will
          be set
          to infinity. Slope-Establishes the slope of the straight line
          used with
          theandvertical-factor keywords. The slope is specified as a fraction
          of rise over run (for example, 45 percent slope is 1/45, which is
          input as 0.02222). LinearInverse Linear
      sourceCostMultiplier {String}:
          Multiplier to apply to the cost values.Allows for control of the mode
          of travel or the magnitude at a source.
          The greater the multiplier, the greater the cost to move through each
          cell.The values must be greater than zero. The default is 1.
      sourceStartCost {String}:
          The starting cost from which to begin the cost calculations.Allows for
          the specification of the fixed cost associated with a
          source. Instead of starting at a cost of zero, the cost algorithm will
          begin with the value set by sourceStartCost.The values must be zero or
          greater. The default is 0.
      sourceResistanceRate {String}:
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
      sourceCapacity {String}:
          Defines the cost capacity for the traveler for a source.The cost
          calculations continue for each source until the specified
          capacity is reached.The values must be greater than zero. The default
          capacity is to the
          edge of the output raster.
      sourceTravelDirection {String}:
          Defines the direction of the traveler when applying horizontal and
          vertical factors, the source resistance rate, and the source starting
          cost.FROM_SOURCE-The horizontal factor, vertical factor, source
          resistance
          rate, and source starting cost will be applied beginning at the input
          source, and moving out to the non-source cells. This is the
          default.TO_SOURCE-The horizontal factor, vertical factor, source
          resistance
          rate, and source starting cost will be applied beginning at each non-
          source cell and moving back to the input source.Either specify the
          FROM_SOURCE or TO_SOURCE keyword, which will be
          applied to all sources, or specify a field in the source data that
          contains the keywords to identify the direction of travel for each
          source. That field must contain the strings FROM_SOURCE or TO_SOURCE.
      outputBacklinkName {String}:
          The name of the output backlink raster service.The backlink raster
          contains values of 0 through 360, which define the
          direction along the least accumulative cost path from a cell to reach
          its least-cost source, while accounting for surface distance as well
          as horizontal and vertical surface factors.
      outputAllocationName {String}:
          The name of the output allocation raster service.This raster
          identifies the zone of each source location (cell or
          feature) that could be reached with the least accumulative cost.The
          output raster is of integer type.
      allocationField {String}:
          A field on the source input that holds the values that define each
          source.

        """