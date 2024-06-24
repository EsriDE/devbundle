# Generated documentation for module arcpy.topographic


class GenerateLocationDiagramFeatures(object):
    """
    Generates location diagram features for a Joint Operations Graphic (JOG), Operational Navigation Chart (ONC), or Tactical Pilotage Chart (TPC) map sheet. The location diagram must include JOG_Index features, WAC_Index features, ONC_Index features, or LandPoly features for the area surrounding the processed sheet.
    """

    @property
    def description(self) -> str:
        return """

        GenerateLocationDiagramFeatures_topographic(in_feature_dataset, area_of_interest, sheet_id_field, wac_features, onc_features, land_features, {specification}, {tpc_features}, {smooth_tolerance}, {hydro_line_features;hydro_line_features...}, {hydro_area_features;hydro_area_features...}, {hydroline_minlength}, {hydroline_minspacing}, {hydroarea_minlength}, {hydroarea_minwidth}, {min_island_area})

        Generates location diagram features for a Joint Operations Graphic
        (JOG), Operational Navigation Chart (ONC), or Tactical Pilotage Chart
        (TPC) map sheet. The location diagram must include JOG_Index features,
        WAC_Index features, ONC_Index features, or LandPoly features for the
        area surrounding the processed sheet.

     INPUTS:
      in_feature_dataset (Feature Dataset):
          The feature dataset that will contain the location diagram feature
          classes. The tool will create these features classes if they do not
          exist.
      area_of_interest (Feature Layer):
          A polygon feature layer with a single selected feature that will be
          used to identify the center and surrounding areas of interest.
      sheet_id_field (Field):
          An attribute field that will be used to identify the generated
          sheet features. You can use thefield as the value for this parameter
          if the field is present in the layer specified by the area_of_interest
          parameter value. JOG_SHEET
      wac_features (Feature Layer):
          The World Aeronautical Chart features that will be used to generate
          the location diagram feature classes in the input geodatabase. The
          default path is specified for this parameter if the Defense Mapping
          product files are installed.
      onc_features (Feature Layer):
          The ONC features that will be used to generate the location diagram
          feature classes in the input geodatabase. The default path is
          specified for this parameter if the Defense Mapping product files are
          installed.
      land_features (Feature Layer):
          The land features that will be used to generate the location diagram
          feature classes in the input geodatabase. The default path is
          specified for this parameter if the Defense Mapping product files are
          installed.
      specification {String}:
          Specifies the type of map product for which the location diagram
          features will be generated.JOG-The location diagram features for a
          Joint Operations Graphic will
          be generated. This is the default.ONC-The location diagram features
          for an Operational Navigation Chart
          will be generated. This option activates the following additional
          parameters: tpc_features, smooth_tolerance, hydro_line_features,
          hydro_area_features, hydroline_minlength, hydroline_minspacing,
          hydroarea_minlength, and hydroarea_minwidth.TPC-The location diagram
          features for a Tactical Pilotage Chart will
          be generated. This option activates the following additional
          parameters: smooth_tolerance, hydro_line_features,
          hydro_area_features, hydroline_minlength, hydroline_minspacing,
          hydroarea_minlength, and hydroarea_minwidth.
      tpc_features {Feature Layer}:
          The TPC features that will be used to generate the location diagram
          feature classes in the input geodatabase. This parameter is available
          when generating location diagram features for an ONC map product.
      smooth_tolerance {Linear Unit}:
          The tolerance that will be used by the smoothing algorithm. The larger
          the value, the more generalized the output location diagram features.
          This parameter is available when generating location diagram features
          for ONC or TPC map products. The default is 0.002 decimal degrees.
      hydro_line_features {Feature Layer}:
          The hydrology line features that will be used to generate the output
          of a thinned hydrology dataset. Only the output features will be
          generalized through this thinning process. This parameter is available
          when generating location diagram features for ONC or TPC map products.
      hydro_area_features {Feature Layer}:
          The hydrology area features that will be used to generate the thinned
          hydrology dataset. Only the output features will be generalized
          through this thinning process. This parameter is available when
          generating location diagram features for ONC or TPC map products.
      hydroline_minlength {Linear Unit}:
          The minimum length that will be used to eliminate hydrology features.
          The tool will thin hydrology features that have a length less than
          this value. This value will be used when generalizing input hydro
          lines and areas. This parameter is available when generating location
          diagram features for ONC or TPC map products.
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
          hydroline_minlength value being hidden. This parameter is available
          when generating location diagram features for ONC or TPC map products.
      hydroarea_minlength {Linear Unit}:
          The length that will be used to split and classify hydrographic
          polygons as short or long. Polygons will be split at any location
          where the edge-to-edge distance is equal to this value. This parameter
          is available when generating location diagram features for ONC or TPC
          map products.
      hydroarea_minwidth {Linear Unit}:
          The width that will be used to split and classify hydrographic
          polygons as narrow or wide. Polygons will be split at any location
          where the edge-to-edge distance is equal to this value. This parameter
          is available when generating location diagram features for ONC or TPC
          map products.
      min_island_area {Areal Unit}:
          The minimum area necessary for an island or hole to be included in the
          resulting features.

        """