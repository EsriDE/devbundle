# Generated documentation for module arcpy.topographic


class GenerateElevationBands(object):
    """
    Creates an elevation bands feature class from a digital elevation model (DEM).
    """

    @property
    def description(self) -> str:
        return """

        GenerateElevationBands_topographic(in_raster;in_raster..., in_aoi, out_feature_class, contour_interval, min_area, smooth_tolerance, {in_hydro_features}, {number_of_bands})

        Creates an elevation bands feature class from a digital elevation
        model (DEM).

     INPUTS:
      in_raster (Raster Layer / Mosaic Layer):
          The rasters that will be used to create elevation bands.
      in_aoi (Feature Layer):
          The layer that will define the processing extent.
      contour_interval (Long):
          Specifies the contour interval that will be used to determine the
          closest available contour when calculating the elevation band
          area.10-A contour interval of 10 will be used.20-A contour interval of
          20
          will be used. This is the default.40-A contour interval of 40 will be
          used.80-A contour interval of 80 will be used.
      min_area (Double):
          The minimum area of the output polygons. Features smaller than
          this value will be removed. The default is 0.00016 square decimal
          degrees. If you're creating an output dataset with a projected
          coordinate
          system, ensure that this value reflects the square units of that
          coordinate system-for example, square meters for a UTM dataset.
          Otherwise, the default value may result in an empty output dataset.
      smooth_tolerance (Linear Unit):
          The tolerance that will be used by the smoothing algorithm. The larger
          the value, the more generalized the output band features. The default
          is 0.002 decimal degrees.
      in_hydro_features {Feature Layer}:
          The bodies of water that will be excluded when calculating the
          elevation band area.
      number_of_bands {Long}:
          Specifies the number of elevation bands that will be generated.1-One
          elevation band will be generated.2-Two elevation bands will be
          generated.3-Three elevation bands will be generated.4-Four elevation
          bands will be generated.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class containing the output elevation band features.

        """