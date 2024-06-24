# Generated documentation for module arcpy.stats


class MultiDistanceSpatialClustering(object):
    """
    Determines whether features, or the values associated with features, exhibit statistically significant clustering or dispersion over a range of distances.
    """

    @property
    def description(self) -> str:
        return """

        MultiDistanceSpatialClustering_stats(Input_Feature_Class, Output_Table, Number_of_Distance_Bands, {Compute_Confidence_Envelope}, {Display_Results_Graphically}, {Weight_Field}, {Beginning_Distance}, {Distance_Increment}, {Boundary_Correction_Method}, {Study_Area_Method}, {Study_Area_Feature_Class})

        Determines whether features, or the values associated with features,
        exhibit statistically significant clustering or dispersion over a
        range of distances.

     INPUTS:
      Input_Feature_Class (Feature Layer):
          The feature class upon which the analysis will be performed.
      Number_of_Distance_Bands (Long):
          The number of times to increment the neighborhood size and analyze the
          dataset for clustering. The starting point and size of the increment
          are specified in the Beginning_Distance and Distance_Increment
          parameters, respectively.
      Compute_Confidence_Envelope {String}:
          The confidence envelope is calculated by randomly placing feature
          points (or feature values) in the study area. The number of
          points/values randomly placed is equal to the number of points in the
          feature class. Each set of random placements is called a permutation
          and the confidence envelope is created from these permutations. This
          parameter allows you to select how many permutations you want to use
          to create the confidence envelope.0_PERMUTATIONS_-
          _NO_CONFIDENCE_ENVELOPE-Confidence envelopes are not
          created.9_PERMUTATIONS-Nine sets of points/values are randomly
          placed.99_PERMUTATIONS-99 sets of points/values are randomly
          placed.999_PERMUTATIONS-999 sets of points/values are randomly placed.
      Display_Results_Graphically {Boolean}:
          This parameter has no effect; it remains to support backward
          compatibility.NO_DISPLAY-No graphical summary will be created
          (default).DISPLAY_IT-A
          graphical summary will be created as a graph layer.
      Weight_Field {Field}:
          A numeric field with weights representing the number of
          features/events at each location.
      Beginning_Distance {Double}:
          The distance at which to start the cluster analysis and the distance
          from which to increment. The value entered for this parameter should
          be in the units of the Output Coordinate System.
      Distance_Increment {Double}:
          The distance to increment during each iteration. The distance used in
          the analysis starts at the Beginning_Distance and increments by the
          amount specified in the Distance_Increment. The value entered for this
          parameter should be in the units of the Output Coordinate System
          environment setting.
      Boundary_Correction_Method {String}:
          Method to use to correct for underestimates in the number of neighbors
          for features near the edges of the study area.NONE-No edge correction
          is applied. However, if the input feature
          class already has points that fall outside the study area boundaries,
          these will be used in neighborhood counts for features near
          boundaries.SIMULATE_OUTER_BOUNDARY_VALUES-This method simulates points
          outside
          the study area so that the number of neighbors near edges is not
          underestimated. The simulated points are the "mirrors" of points near
          edges within the study area boundary.REDUCE_ANALYSIS_AREA-This method
          shrinks the study area such that some
          points are found outside of the study area boundary. Points found
          outside the study area are used to calculate neighbor counts but are
          not used in the cluster analysis
          itself.RIPLEY_EDGE_CORRECTION_FORMULA-For all the points (j) in the
          neighborhood of point i, this method checks to see if the edge of the
          study area is closer to i, or if j is closer to i. If j is closer,
          extra weight is given to the point j. This edge correction method is
          only appropriate for square or rectangular shaped study areas.
      Study_Area_Method {String}:
          Specifies the region to use for the study area. The K Function is
          sensitive to changes in study area size so careful selection of this
          value is important.MINIMUM_ENCLOSING_RECTANGLE-Indicates that the
          smallest possible
          rectangle enclosing all of the points will be
          used.USER_PROVIDED_STUDY_AREA_FEATURE_CLASS-Indicates that a feature
          class
          defining the study area will be provided in the Study Area Feature
          Class parameter.
      Study_Area_Feature_Class {Feature Layer}:
          Feature class that delineates the area over which the input feature
          class should be analyzed. Only specified if Study_Area_Method =
          "USER_PROVIDED_STUDY_AREA_FEATURE_CLASS".

     OUTPUTS:
      Output_Table (Table):
          The table to which the results of the analysis will be written.

        """