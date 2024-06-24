# Generated documentation for module arcpy.topographic


class GenerateElevationGuideFeatures(object):
    """
    Creates data required for an elevation guide diagram surround element as required by various supported map product specifications. This tool uses existing banding and thinning parameters to generate output elevation band features, spot height features, and hydrology features.
    """

    @property
    def description(self) -> str:
        return """

        GenerateElevationGuideFeatures_topographic(in_feature_dataset, area_of_interest, in_rasters;in_rasters..., {hydro_exclusion_features}, {spot_height_features}, {hydro_line_features;hydro_line_features...}, {hydro_area_features;hydro_area_features...}, {contour_interval}, {bands_minarea}, {smooth_tolerance}, {number_of_bands}, {height_field}, {search_distance}, {hydroline_minlength}, {hydroline_minspacing}, {hydroarea_minlength}, {hydroarea_minwidth}, {min_island_area})

        Creates data required for an elevation guide diagram surround element
        as required by various supported map product specifications. This tool
        uses existing banding and thinning parameters to generate output
        elevation band features, spot height features, and hydrology features.

     INPUTS:
      in_feature_dataset (Feature Dataset):
          An existing feature dataset that will contain the EGB feature classes.
          Data created for the elevation guide box is maintained in these
          feature classes in this feature dataset.
      area_of_interest (Feature Layer):
          A feature layer with a single selected feature that will define the
          processing extent for banding operations and a clipping extent for
          spot heights, and input hydrology areas and lines.
      in_rasters (Raster Layer / Mosaic Layer):
          One or more rasters that will be used to create elevation bands and
          supply elevation values to the created features.
      hydro_exclusion_features {Feature Layer}:
          A feature layer that defines a large water body area that will be
          excluded from the elevation band area computation.
      spot_height_features {Feature Layer}:
          A feature layer or class that contains spot heights.
      hydro_line_features {Feature Layer}:
          Hydrology line features that will be used to generate the output of a
          thinned hydrology dataset. Only the output features will be
          generalized through this thinning process.
      hydro_area_features {Feature Layer}:
          Hydrology area features that will be used to generate the thinned
          hydrology dataset. Only the output features will be generalized
          through this thinning process.
      contour_interval {Long}:
          Specifies the contour interval that will be used to determine the
          closest available contour when calculating the elevation band area.
          Elevation bands are created with their limits aligned to the specified
          contour interval, except low and high values, which will represent
          their actual calculated values.10-A contour interval of 10 will be
          used.20-A contour interval of 20
          will be used. This is the default.40-A contour interval of 40 will be
          used.80-A contour interval of 80 will be used.
      bands_minarea {Double}:
          The minimum area for output polygons. Features smaller than
          this value will be removed. The default is 0.00016 square decimal
          degrees. If you are creating an output dataset with a projected
          coordinate
          system, ensure that this value reflects the square units of that
          coordinate system-for example, square meters for a UTM dataset.
          Otherwise, the default value may result in an empty output dataset.
      smooth_tolerance {Linear Unit}:
          The tolerance that will be used by the smoothing algorithm. The larger
          the value, the more generalized the output band features. The default
          is 0.002 decimal degrees.
      number_of_bands {Long}:
          Specifies the number of elevation bands that will be generated.1-One
          elevation band will be generated.2-Two elevation bands will be
          generated.3-Three elevation bands will be generated.4-Four elevation
          bands will be generated.
      height_field {Field}:
          The field that identifies the elevation values of the spot height
          features. These values will be evaluated during the thinning process.
      search_distance {Linear Unit}:
          The minimum distance between spot heights. The default is 0 meters.
      hydroline_minlength {Linear Unit}:
          The minimum length that will be used to eliminate hydrology features.
          Hydrology features that have a length less than this value will be
          thinned. This value is used when generalizing input hydro lines and
          areas.
      hydroline_minspacing {Linear Unit}:
          The shortest distance between hydrographic segments that will display
          at the output scale. If the spacing between two parallel trending
          features is smaller than this value, one of the features will be
          hidden. This parameter defines the density of the resulting thinned
          hydrography. It should correspond to the distance between two parallel
          trending features that is visually significant to include at the final
          scale. When the density of features is too high (that is, the features
          are too closely spaced), at least one feature will be hidden. This can
          result in important features or features longer than the
          hydroline_minlength value being hidden.
      hydroarea_minlength {Linear Unit}:
          The length that will be used to split and classify hydrographic
          polygons as short or long. Polygons will be split at any location
          where the edge-to-edge distance is equal to the this value.
      hydroarea_minwidth {Linear Unit}:
          The width that will be used to split and classify hydrographic
          polygons as narrow or wide. Polygons will be split at any location
          where the edge-to-edge distance is equal to this value.
      min_island_area {Areal Unit}:
          The minimum area necessary for an island or hole to be included in the
          resulting features.

        """