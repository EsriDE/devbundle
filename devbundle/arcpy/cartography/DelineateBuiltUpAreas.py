# Generated documentation for module arcpy.cartography


class DelineateBuiltUpAreas(object):
    """
    Creates polygons to represent built-up areas by delineating densely clustered arrangements of buildings on small-scale maps.
    """

    @property
    def description(self) -> str:
        return """

        DelineateBuiltUpAreas_cartography(in_buildings;in_buildings..., {identifier_field}, {edge_features;edge_features...}, grouping_distance, minimum_detail_size, out_feature_class, {minimum_building_count})

        Creates polygons to represent built-up areas by delineating densely
        clustered arrangements of buildings on small-scale maps.

     INPUTS:
      in_buildings (Feature Layer):
          The layers containing buildings with density and arrangement that are
          used to define appropriate output built-up polygons. Multiple building
          layers can be assessed simultaneously. Building features can be points
          or polygons.
      identifier_field {String}:
          A field in the input feature classes that will hold a status
          code indicating whether the input feature is part of the resulting
          built-up area . This field must be either short or long integer type
          and common to all input layers if multiple input layers are used.
          0-The building is not represented by an output built-up area
          polygon.1-The building is represented by an output built-up area
          polygon and
          is within the resulting polygon.2-The building is represented by an
          output built-up area polygon and
          is outside the resulting polygon.
      edge_features {Feature Layer}:
          The layers that will be used to define the edges of the built-up area
          polygons. Typically, these are roads, but other common examples are
          rivers, coastlines, and administrative areas. Built-up area polygons
          snap to an edge feature if one is generally aligned with the trend of
          the polygon edge and within the grouping distance away. Edge features
          can be lines or polygons.
      grouping_distance (Linear Unit):
          Buildings closer together than the grouping distance are considered
          collectively as candidates for representation by an output built-up
          area polygon. This distance is measured from the edges of polygon
          buildings and the centers of point buildings.
      minimum_detail_size (Linear Unit):
          The relative degree of detail in the output built-up area polygons.
          This is approximately to the minimum allowable diameter of a hole or
          cavity in the built-up area polygon. The actual size and shape of
          holes and cavities within the polygon is determined also by the
          arrangement of the input buildings, the grouping distance, and the
          presence of edge features if they are used.
      minimum_building_count {Long}:
          The minimum number of buildings that must be collectively considered
          for representation by an output built-up area polygon. The default
          value is 4. The minimum building count must be greater than or equal
          to 0.

     OUTPUTS:
      out_feature_class (Feature Class):
          The output feature class containing built-up area polygons
          representing clustered arrangements of input buildings.

        """