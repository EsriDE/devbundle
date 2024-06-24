# Generated documentation for module arcpy.sa.Functions


class Kriging(object):
    """
    Interpolates a raster surface from points using kriging.
    """

    @property
    def description(self) -> str:
        return """

        Kriging_sa(in_point_features, z_field, kriging_model, {cell_size}, {search_radius}, {out_variance_prediction_raster})

        Interpolates a raster surface from points using kriging.

     INPUTS:
      in_point_features (Composite Geodataset):
          The input point features containing the z-values to be interpolated
          into a surface raster.
      z_field (Field):
          The field that holds a height or magnitude value for each point.This
          can be a numeric field or the Shape field if the input point
          features contain z-values.
      kriging_model (KrigingModel):
          The KrigingModel class defines which kriging model is to be used.There
          are two types of kriging classes. The KrigingModelOrdinary
          method has five types of semivariograms available. The
          KrigingModelUniversal method has two types of semivariograms
          available. KrigingModelOrdinary ({semivariogramType},
          {lagSize},
          {majorRange}, {partialSill}, {nugget})
          semivariogramType-The semivariogram model to be used. The
          available models include the following:           SPHERICAL-Spherical
          semivariogram model. This is the
          default.CIRCULAR-Circular semivariogram model.EXPONENTIAL-Exponential
          semivariogram model.GAUSSIAN-Gaussian (or normal distribution)
          semivariogram model.LINEAR-Linear semivariogram model with a sill.
          KrigingModelUniversal ({semivariogramType}, {lagSize},
          {majorRange}, {partialSill}, {nugget})
          semivariogramType-The semivariogram model to be used. The
          available models include the following:
          LINEARDRIFT-Universal Kriging with linear
          drift.QUADRATICDRIFT-Universal Kriging with quadratic drift.
          After the {semivariogramType}, the other parameters are
          common between Ordinary and Universal kriging. lagSize-The
          default is the output raster cell
          size.majorRange-Represents a distance beyond which there is little or
          no
          correlation.partialSill-The difference between the nugget and the
          sill.nugget-Represents the error and variation at spatial scales too
          fine
          to detect. The nugget effect is seen as a discontinuity at the origin.
      cell_size {Analysis Cell Size}:
          The cell size of the output raster that will be created.This parameter
          can be defined by a numeric value or obtained from an
          existing raster dataset. If the cell size hasn't been explicitly
          specified as the parameter value, the environment cell size value will
          be used if specified; otherwise, additional rules will be used to
          calculate it from the other inputs. See the usage section for more
          detail.
      search_radius {Radius}:
          The Radius class defines which of the input points will be used to
          interpolate the value for each cell in the output raster.There are two
          types of radius classes: RadiusVariable and RadiusFixed.
          A Variable search radius is used to find a specified number of input
          sample points for the interpolation. The Fixed type uses a specified
          fixed distance within which all input points will be used for the
          interpolation. The Variable type is the default.
          RadiusVariable ({numberofPoints}, {maxDistance})
          {numberofPoints}-An integer value specifying the number of nearest
          input sample points to be used to perform interpolation. The default
          is 12 points.{maxDistance}-Specifies the distance, in map units, by
          which to limit
          the search for the nearest input sample points. The default value is
          the length of the extent's diagonal. RadiusFixed ({distance},
          {minNumberofPoints})
          {distance}-Specifies the distance as a radius within which
          input sample points will be used to perform the interpolation.
          The value of the radius is expressed in map units. The default radius
          is five times the cell size of the output raster.
          {minNumberofPoints}-An integer defining the minimum number
          of points to be used for interpolation. The default value is 0.
          If the required number of points is not found within the specified
          distance, the search distance will be increased until the specified
          minimum number of points is found.When the search radius needs to be
          increased it is done so until the
          {minNumberofPoints} fall within that radius, or the extent of the
          radius crosses the lower (southern) and/or upper (northern) extent of
          the output raster. NoData is assigned to all locations that do not
          satisfy the above condition.

     OUTPUTS:
      out_surface_raster (Raster Dataset):
          The output interpolated surface raster.It is always a floating-point
          raster.
      out_variance_prediction_raster {Raster Dataset}:
          Optional output raster where each cell contains the predicted variance
          values for that location.

        """