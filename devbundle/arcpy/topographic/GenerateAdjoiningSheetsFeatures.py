# Generated documentation for module arcpy.topographic


class GenerateAdjoiningSheetsFeatures(object):
    """
    Generates features necessary for display in a typical topographic map adjoining sheets diagram.
    """

    @property
    def description(self) -> str:
        return """

        GenerateAdjoiningSheetsFeatures_topographic(in_feature_dataset, area_of_interest, {land_features}, {scale}, {clip_aoi_to_sheets})

        Generates features necessary for display in a typical topographic map
        adjoining sheets diagram.

     INPUTS:
      in_feature_dataset (Feature Dataset):
          An existing feature dataset that will contain the ASG_ feature
          classes. The tool will create these feature classes if they do not
          exist.
      area_of_interest (Feature Layer):
          A feature layer with a single selected feature used to identify the
          center and surrounding AOIs. Adjoining sheets features will be created
          from the selected AOI and the intersecting AOIs as required.
      land_features {Feature Layer}:
          Land features used to generate adjoining sheets features in the
          ASG_COAST_A and ASG_COAST_L feature classes in the target feature
          dataset.
      scale {String}:
          Defines a factor by which the extent of the area_of_interest
          is expanded. The expanded extent is used to select adjoining areas of
          interest. Data from the adjoining areas of interest is included in the
          adjoining sheets diagram. 1:25000-Uses specification
          MIL-T-89301A as a guide to determine how to
          expand the width and height of the extent of the
          area_of_interest.1:50000-Uses specification MIL-T-89301A to determine
          how to expand the
          width and height of the extent of the area_of_interest. This is the
          default.1:100000-Uses specification MIL-T-89306 to determine how to
          expand the
          width and height of the extent of the area_of_interest.
      clip_aoi_to_sheets {Boolean}:
          Determines if the AOI created for the extent of the adjoining sheets
          diagram will be clipped to the extents of the sheets to be displayed.
          If set to CLIP_AOI, the AOI for the adjoining sheets diagram will be
          modified from its originally calculated rectangular shape to include
          any irregular map sheet extents that will be included or excluded in
          the diagram.CLIP_AOI-The AOI feature will be clipped by the sheets to
          be displayed
          in the adjoining sheet diagram and may have an irregular shape. This
          is the default.DONT_CLIP_AOI-The AOI feature will not be clipped and
          will retain its
          originally calculated rectangular shape. This may result in partial
          sheets being displayed in the adjoining sheets diagram.

        """