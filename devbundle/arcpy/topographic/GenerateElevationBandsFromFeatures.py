# Generated documentation for module arcpy.topographic


class GenerateElevationBandsFromFeatures(object):
    """
    Generates band features that represent elevation levels on a map product. The tool can be run with set values from standardized product specifications or with custom-defined values.
    """

    @property
    def description(self) -> str:
        return """

        GenerateElevationBandsFromFeatures_topographic(contour_features, elevation_field, area_of_interest, out_feature_class, {exclusion_features;exclusion_features...}, {product}, {band_interval}, {band_values;band_values...})

        Generates band features that represent elevation levels on a map
        product. The tool can be run with set values from standardized product
        specifications or with custom-defined values.

     INPUTS:
      contour_features (Feature Layer):
          The polyline feature layer that contains the contours. The information
          for the output bands will be derived from these features.
      elevation_field (Field):
          The field in the contour_features feature layer from which the
          elevation values will be derived.
      area_of_interest (Feature Layer):
          The AOI for the area where the elevation bands will be created. The
          AOI is typically stored in an index feature class that contains the
          extents for standard map sheets. A single feature must be selected on
          the feature class that is specified.
      exclusion_features {Feature Layer}:
          The feature layers that define areas where bands will not be created.
      product {String}:
          A supported map product, which determines the values for the
          band_values parameter unless Custom is specified for this parameter.
          If left blank, at least one pair of Low and High values is required
          for the band_values parameter.JOG-A-The Joint Operations Graphic-Air
          productONC-The Operational
          Navigation Chart productTPC-The Tactical Pilotage Chart
          productCustom-A custom product
      band_interval {Long}:
          The interval specified when the band interval type is regular. This
          parameter is only available when Custom is specified as the product
          parameter value.
      band_values {Value Table}:
          The low and high values in the bands that will be created. These
          values will be populated automatically from an .xml file if a
          particular product is specified for the product parameter value;
          however, these values must be provided manually if Custom is specified
          for the product parameter value and at least one pair of Low and High
          values is required. If no product is specified, at least one pair of
          Low and High values is still required.

     OUTPUTS:
      out_feature_class (Feature Class):
          The feature class that will contain the banding features.

        """