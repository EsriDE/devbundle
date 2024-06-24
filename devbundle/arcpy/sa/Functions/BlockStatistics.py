# Generated documentation for module arcpy.sa.Functions


class BlockStatistics(object):
    """
    Partitions the input into non-overlapping blocks and calculates the statistic of the values within each block. The value is assigned to all of the cells in each block in the output.
    """

    @property
    def description(self) -> str:
        return """

        BlockStatistics_sa(in_raster, {neighborhood}, {statistics_type}, {ignore_nodata})

        Partitions the input into non-overlapping blocks and calculates the
        statistic of the values within each block. The value is assigned to
        all of the cells in each block in the output.

     INPUTS:
      in_raster (Composite Geodataset):
          The raster for which a statistic will be calculated for blocks of
          cells.
      neighborhood {Neighborhood}:
          The cells of the processing block that will be used in the statistic
          calculation. There are several predefined neighborhood types to choose
          from, or a custom kernel can be defined.Once the neighborhood type is
          selected, other parameters can be set to
          fully define the shape, size, and units of measure. The default
          neighborhood is a square rectangle with a width and height of three
          cells.The shape of the neighborhoods are defined by the Neighborhood
          class.
          The available neighborhood types are NbrAnnulus, NbrCircle,
          NbrRectangle, NbrWedge, NbrIrregular, and NbrWeight.The following are
          the forms of the available neighborhood types:
          NbrAnnulus({innerRadius}, {outerRadius}, {units})         A
          ring or donut-shaped neighborhood defined by an inner radius and an
          outer radius. The minimum value for radius is 1 cell, and the outer
          radius must be larger than the inner. The maximum inner radius is 2046
          cells, and the maximum outer radius is 2047 cells. The default annulus
          is an inner radius of 1 cell and an outer radius of 3 cells.
          NbrCircle({radius}, {units}         A circular neighborhood
          with the given radius. The minimum value for
          radius is 1 cell, and the maximum value is 2047 cells. The default
          radius is 3 cells. NbrRectangle({width}, {height}, {units})
          A
          rectangular neighborhood defined by width and height. The minimum
          value for width or height is 1 cell, and the maximum value is 4096
          cells. The default is a square with a width and height of 3 cells.
          NbrWedge({radius}, {startAngle}, {endAngle}, {units})
          A wedge-shaped neighborhood defined by a radius, a start angle, and an
          end angle. The minimum value for radius is 1 cell, and the maximum
          value is 2047 cells. The wedge extends counterclockwise from the
          starting angle to the ending angle. Angles are specified in degrees,
          with 0 or 360 representing east. Negative angles can be used. The
          default wedge is from 0 to 90 degrees, with a radius of 3 cells.
          NbrIrregular(inKernelFile)         A custom neighborhood with
          specifications set by the identified kernel
          text file. The minimum value for width or height of the kernel is 1
          cell, and the maximum value is 4096 cells.
          NbrWeight(inKernelFile)         A custom neighborhood with
          specifications set by the identified kernel
          text file, which can apply weights to the members of the neighborhood.
          The minimum value for width or height of the kernel is 1 cell, and the
          maximum value is 4096 cells.For the NbrAnnulus, Nbrcircle,
          NbrRectangle and NbrWedge
          neighborhoods, the distance units for the parameters can be specified
          in CELL units or MAP units. Cell units is the default.For kernel
          neighborhoods, the first line in the kernel file defines
          the width and height of the neighborhood in numbers of cells. The
          subsequent lines indicate how the input value that corresponds to that
          location in the kernel will be processed. A value of 0 in the kernel
          file for either the irregular or the weight neighborhood type
          indicates the corresponding location will not be included in the
          calculation. For the irregular neighborhood, a value of 1 in the
          kernel file indicates that the corresponding input cell will be
          included in the operation. For the weight neighborhood, the value at
          each position indicates what the corresponding input cell value is to
          be multiplied by. Positive, negative, and decimal values can be used.
      statistics_type {String}:
          Specifies the statistic type to be calculated.MEAN-The mean (average
          value) of the cells in the neighborhood will be
          calculated.MAJORITY-The majority (value that occurs most often) of the
          cells in
          the neighborhood will be identified.MAXIMUM-The maximum (largest
          value) of the cells in the neighborhood
          will be identified.MEDIAN-The median of the cells in the neighborhood
          will be calculated.MINIMUM-The minimum (smallest value) of the cells
          in the neighborhood
          will be identified.MINORITY-The minority (value that occurs least
          often) of the cells in
          the neighborhood will be identified.RANGE-The range (difference
          between largest and smallest value) of the
          cells in the neighborhood will be calculated.STD-The standard
          deviation of the cells in the neighborhood will be
          calculated.SUM-The sum of the cells in the neighborhood will be
          calculated.VARIETY-The variety (the number of unique values) of the
          cells in the
          neighborhood will be calculated.The default statistic type is MEAN.If
          the input raster is integer, all the statistics types will be
          available. If the input raster is floating point, only the MEAN,
          MAXIMUM, MINIMUM, RANGE, STD, and SUM statistic types will be
          available.
      ignore_nodata {Boolean}:
          Specifies whether NoData values will be ignored by the statistic
          calculation.DATA-If a NoData value exists within a block neighborhood,
          the NoData
          value will be ignored. Only cells within the neighborhood that have
          data values will be used in determining the output value. This is the
          default.NODATA-If any cell in a block neighborhood has a value of
          NoData, the
          output for each cell in the corresponding block will be NoData. The
          presence of a NoData value implies that there is insufficient
          information to determine the statistic value for the neighborhood.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output block statistics raster.

        """