# Generated documentation for module arcpy.management


class CreateSpatialSamplingLocations(object):
    """
    Creates sample locations within a continuous study area using simple random, stratified, systematic (gridded), or cluster sampling designs.
    """

    @property
    def description(self) -> str:
        return """

        CreateSpatialSamplingLocations_management(in_study_area, out_features, {sampling_method}, {strata_id_field}, {strata_count_method}, {bin_shape}, {bin_size}, {h3_resolution}, {num_samples}, {num_samples_per_strata}, {population_field}, {geometry_type}, {min_distance}, {spatial_relationship})

        Creates sample locations within a continuous study area using simple
        random, stratified, systematic (gridded), or cluster sampling designs.

     INPUTS:
      in_study_area (Feature Layer / Raster Layer):
          The input study area where sample locations will be created. The study
          area must be polygons or an integer (categorical) raster. For rasters,
          cells with null values will not be included in the study area.
      sampling_method {String}:
          Specifies the sampling method that will be used to create the sample
          locations.RANDOM-Points will be randomly created in the study area,
          and all
          locations have the same likelihood of being sampled. All boundaries
          between individual polygons or raster regions will be ignored. This is
          the default.STRAT_POLY-Each polygon will be a different stratum, and
          points will
          be randomly and independently created in each polygon. The input study
          area must be polygons.STRAT_RAST-Each region of a categorical raster
          will be a stratum, and
          sample points will be randomly and independently created in each
          region. A raster region is a contiguous block of cells with the same
          value that are connected by shared cell edges. If two regions have the
          same value but are not connected by shared edges, they will be
          different strata. The input study area must be a raster.STRAT_ID-Each
          polygon or raster region with the same strata ID field
          value will be a stratum, and sample points will be randomly and
          independently created in each stratum. The polygons or raster cells
          are not required to be contiguous to be in the same
          stratum.SYSTEMATIC-Sample locations will be created using a gridded
          tessellation in the study area. The sample locations can be created as
          polygons or as points (centroids of the tessellated
          polygons).CLUSTER-Sample polygons will be created by randomly
          selecting polygons
          from a tessellation of the study area.
      strata_id_field {Field}:
          For stratified sampling by strata ID field, the strata ID field
          defining the strata.
      strata_count_method {String}:
          For stratified sampling, specifies the method that will be used to
          determine the number of sample locations that will be created in each
          stratum.EQUAL-The same number of sample locations will be created in
          each
          stratum. Provide the value in the num_samples_per_strata parameter.
          This is the default.PROP_AREA-The number of sample locations in each
          stratum will be
          proportional to the area of the stratum. Provide the total number of
          samples in the num_samples parameter.FIELD-The number of sample
          locations in each stratum will be equal to
          the values of a population field. Provide the field in the
          population_field parameter. This option is not available when
          stratifying by contiguous raster region.PROP_FIELD-The number of
          sample locations in each stratum will be
          proportional to the values of a population field. Provide the field in
          the population_field parameter and the total number of samples in the
          num_samples parameter. This option is not available when stratifying
          by contiguous raster region.
      bin_shape {String}:
          For systematic and cluster sampling, specifies the shape of each
          polygon in the gridded tessellation.HEXAGON-Hexagon-shaped features
          will be generated. The top and bottom
          side of each hexagon will be parallel with the x-axis of the
          coordinate system (the top and bottom are
          flat).TRANSVERSE_HEXAGON-Transverse hexagon-shaped features will be
          generated. The right and left side of each hexagon will be parallel
          with the y-axis of the dataset's coordinate system (the top and bottom
          are pointed).SQUARE-Square-shaped features will be generated. The top
          and bottom
          side of each square will be parallel with the x-axis of the coordinate
          system, and the right and left sides will be parallel with the y-axis
          of the coordinate system.DIAMOND-Diamond-shaped features will be
          generated. The sides of each
          polygon will be rotated 45 degrees away from the x-axis and y-axis of
          the coordinate system.TRIANGLE-Triangular-shaped features will be
          generated. Each triangle
          will be a regular three-sided equilateral polygon.H3_HEXAGON-Hexagon-
          shaped features will be generated based on the H3
          Hexagonal hierarchical geospatial indexing system.
      bin_size {Long / Areal Unit}:
          For systematic and cluster sampling, the size of each polygon in the
          tessellation. The value can be provided as a count (the total number
          of tessellated polygons created in the study area) or as an area (the
          area of each tessellated polygon). For count input, the default is
          100. For area input, a value must be provided.If a count is provided,
          the tool will attempt to create the specified
          number of sample locations. If the exact number cannot be created, a
          warning will be returned.
      h3_resolution {Long}:
          For systematic or cluster sampling with H3 hexagon bins, specifies the
          H3 resolution of the hexagons.With each increasing resolution value,
          the area of the polygons will
          be one seventh the size.0-Hexagons will be created at the H3
          resolution of 0, with an average
          area of 4,357,449.416078381 square kilometers.1-Hexagons will be
          created at the H3 resolution of 1, with an average
          area of 609,788.441794133 square kilometers.2-Hexagons will be created
          at the H3 resolution of 2, with an average
          area of 86,801.780398997 square kilometers.3-Hexagons will be created
          at the H3 resolution of 3, with an average
          area of 12,393.434655088 square kilometers.4-Hexagons will be created
          at the H3 resolution of 4, with an average
          area of 1,770.347654491 square kilometers.5-Hexagons will be created
          at the H3 resolution of 5, with an average
          area of 252.903858182 square kilometers.6-Hexagons will be created at
          the H3 resolution of 6, with an average
          area of 36.129062164 square kilometers.7-Hexagons will be created at
          the H3 resolution of 7, with an average
          area of 5.161293360 square kilometers. This is the default.8-Hexagons
          will be created at the H3 resolution of 8, with an average
          area of 0.737327598 square kilometers.9-Hexagons will be created at
          the H3 resolution of 9, with an average
          area of 0.105332513 square kilometers.10-Hexagons will be created at
          the H3 resolution of 10, with an
          average area of 0.015047502 square kilometers.11-Hexagons will be
          created at the H3 resolution of 11, with an
          average area of 0.002149643 square kilometers.12-Hexagons will be
          created at the H3 resolution of 12, with an
          average area of 0.000307092 square kilometers.13-Hexagons will be
          created at the H3 resolution of 13, with an
          average area of 0.000043870 square kilometers.14-Hexagons will be
          created at the H3 resolution of 14, with an
          average area of 0.000006267 square kilometers.15-Hexagons will be
          created at the H3 resolution of 15, with an
          average area of 0.000000895 square kilometers.
      num_samples {Long}:
          The number of sample locations that will be created. This parameter
          always applies to simple random and cluster sampling. For stratified
          sampling, this parameter applies when the sample count will be
          proportional to stratum area or proportional to a population field.
          For simple random and stratified sampling, the default is 100. For
          cluster sampling, the default is 10.
      num_samples_per_strata {Long}:
          For stratified sampling with equal sample count in each stratum, the
          number of sample locations created within each stratum. The total
          number of samples will be this value multiplied by the number of
          strata. The default is 100.
      population_field {Field}:
          The population field for stratified sampling when the sample count is
          equal or proportional to a population field.
      geometry_type {String}:
          For systematic sampling, specifies whether the sample locations will
          be tessellated polygons or centroids (points) of the tessellated
          polygons.POINT-Centroids of the tessellated polygons will be created
          as sample
          locations. This is the default.POLYGON-Tessellated polygons will be
          created as sampling locations.
      min_distance {Linear Unit}:
          For simple random and stratified sampling, the smallest allowed
          distance between sample locations. For simple random sampling, all
          points will be at least this distance apart. For stratified sampling,
          points within the same stratum will be at least this distance apart,
          but points in neighboring strata may be closer than this distance.For
          large distances, fewer sample locations than were expected may be
          created to keep the locations sufficiently far apart. In this case, a
          warning message will be returned.
      spatial_relationship {String}:
          Specifies which polygons from a background tessellation will be
          included as sampling locations. This parameter applies to cluster
          sampling and to systematic sampling when the output geometry type is
          polygon.HAVE_THEIR_CENTER_IN-The centroids of the polygons must be
          within the
          study area to be included. This is the default.COMPLETELY_WITHIN-The
          polygons must be completely within the study
          area to be included.INTERSECT-The polygons must intersect the study
          area to be included.

     OUTPUTS:
      out_features (Feature Class):
          The output features representing the sample locations. For simple
          random and stratified sampling, the output features will be points.
          For cluster sampling, the output will be polygons. For systematic
          sampling, the output can be points or polygons.

        """