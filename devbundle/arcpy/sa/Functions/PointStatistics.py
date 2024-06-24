# Generated documentation for module arcpy.sa.Functions


class PointStatistics(object):
    """
    Calculates a statistic on the points in a neighborhood around each output cell.
    """

    @property
    def description(self) -> str:
        return """

        PointStatistics_sa(in_point_features, field, {cell_size}, {neighborhood}, {statistics_type})

        Calculates a statistic on the points in a neighborhood around each
        output cell.

     INPUTS:
      in_point_features (Composite Geodataset):
          The input points to use in the neighborhood operation.For each output
          cell, any input points that fall within the defined
          neighborhood shape around it are identified. For the selected points,
          values from the specified attribute are obtained, and a statistic is
          calculated.The input can be either a point or multipoint feature
          class.
      field (Field):
          The field for which the specified statistic will be calculated. It can
          be any numeric field of the input point features. It can be
          thefield if the input features contain z-values.
          Shape
      cell_size {Analysis Cell Size}:
          The cell size of the output raster that will be created.This parameter
          can be defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value will
          be used if specified; otherwise, additional rules will be used to
          calculate it from the other inputs. See the usage section for more
          detail.
      neighborhood {Neighborhood}:
          The area around each processing cell within which any input points
          found will be used in the statistics calculation. There are several
          predefined neighborhood types to choose from.Once the neighborhood
          type is selected, other parameters can be set to
          fully define the shape, size, and units of measure. The default
          neighborhood is a square rectangle with a width and height of three
          cells.The shape of the neighborhoods around each input point are
          defined by
          the Neighborhood class. The available neighborhood types are
          NbrAnnulus, NbrCircle, NbrRectangle, and NbrWedge.The following are
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
          default wedge is from 0 to 90 degrees, with a radius of 3 cells.The
          distance units for the parameters can be specified in CELL units
          or MAP units. Cell units is the default.The default neighborhood type
          is NbrRectangle with a height and width
          of three cells.
      statistics_type {String}:
          Specifies the statistic type to be calculated.The calculation is
          performed on the values of the specified field of
          the points that fall within the specified neighborhood of each output
          raster cell.MEAN-The average of the field values in each neighborhood
          will be
          calculated.MAJORITY-The most frequently occurring field value in each
          neighborhood will be identified. In the case of a tie, the lower value
          is used.MAXIMUM-The largest field value in each neighborhood will be
          identified.MEDIAN-The median field value in each neighborhood will be
          calculated.
          In the case of an even number of points in the neighborhood, the
          result will be the lower of the two middle values.MINIMUM-The smallest
          field value in each neighborhood will be
          identified.MINORITY-The least frequently occurring field value in each
          neighborhood will be identified. In the case of a tie, the lower value
          is used.RANGE-The range (the difference between the largest and
          smallest) of
          the field values in each neighborhood will be calculated.STD-The
          standard deviation of the field values in each neighborhood
          will be calculated.SUM-The sum of the field values in the neighborhood
          will be
          calculated.VARIETY-The number of unique field values in each
          neighborhood will be
          calculated.The default statistic type is MEAN.The available choices
          for the statistic type are determined by the
          numeric type of the specified field. If the field is integer, all the
          statistics types will be available. If the field is floating point,
          only the maximum, mean, minimum, range, standard deviation, and sum
          statistics will be available.

     OUTPUTS:
      out_raster (Raster Dataset):
          The output point statistics raster.

        """