# Generated documentation for module arcpy.cartography


class AggregatePolygons(object):
    """
    Combines polygons that are within a specified distance of each other into new polygons.
    """

    @property
    def description(self) -> str:
        return """

        AggregatePolygons_cartography(in_features, out_feature_class, aggregation_distance, {minimum_area}, {minimum_hole_size}, {orthogonality_option}, {barrier_features;barrier_features...}, {out_table}, {aggregate_field})

        Combines polygons that are within a specified distance of each other
        into new polygons.

     INPUTS:
      in_features (Feature Layer):
          The polygon features to be aggregated. If this is a layer referencing
          a representation and shape overrides are present on the input
          features, the overridden shapes, not the feature shapes, will be
          considered in aggregation processing.
      aggregation_distance (Linear Unit):
          The distance to be satisfied between polygon boundaries for
          aggregation to occur. A distance must be specified, and it must be
          greater than zero. You can choose a preferred unit; the default is the
          feature unit.
      minimum_area {Areal Unit}:
          The minimum area for an aggregated polygon to be retained. The default
          value is zero, that is, to keep all polygons. You can specify a
          preferred unit; the default is the feature unit.
      minimum_hole_size {Areal Unit}:
          The minimum size of a polygon hole to be retained. The default value
          is zero, that is, to keep all polygon holes. You can specify a
          preferred unit; the default is the feature unit.
      orthogonality_option {Boolean}:
          Specifies the characteristic of the output features when constructing
          the aggregated boundaries.NON_ORTHOGONAL-Organically shaped output
          features will be created.
          This is suitable for natural features, such as vegetation or soil
          polygons. This is the default.ORTHOGONAL-Orthogonally shaped output
          features will be created. This
          is suitable for preserving the geometric characteristic of
          anthropogenic input features, such as building footprints.
      barrier_features {Feature Layer}:
          The layers containing the line or polygon features that are
          aggregation barriers for input features. Features will not be
          aggregated across barrier features. Barrier features that are in
          geometric conflict with input features will be ignored.
      aggregate_field {Field}:
          The field that contains attributes for aggregation. Features must
          share the same attribute value to be considered for aggregation. For
          example, use a building classification field as the aggregate field to
          prevent commercial buildings from aggregating with residential
          buildings.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class to be created.
      out_table {Table}:
          A one-to-many relationship table that links the aggregated
          polygons to their source polygon features. This table contains two
          fields,and, that store the aggregated feature IDs and their source
          feature IDs, respectively. Use this table to derive necessary
          attributes for the output features from their source features. The
          default name for this table is the name of the output feature class,
          appended with _tbl. The default path is the same as the output feature
          class. If the output features location is specified in a feature
          dataset, this table will be created one level higher, at the
          geodatabase level. No table is created when this parameter is left
          blank. OUTPUT_FIDINPUT_FID

        """