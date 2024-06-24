# Generated documentation for module arcpy.management


class AddRuleToTopology(object):
    """
    Adds a rule to a topology.
    """

    @property
    def description(self) -> str:
        return """

        AddRuleToTopology_management(in_topology, rule_type, in_featureclass, {subtype}, {in_featureclass2}, {subtype2})

        Adds a rule to a topology.

     INPUTS:
      in_topology (Topology Layer):
          The topology to which the new rule will be added.
      rule_type (String):
          Specifies the topology rule that will be added.Must Not Have Gaps
          (Area)-There must be no voids within a single
          polygon or between adjacent polygons. All polygons must form a
          continuous surface. An error will always exist on the perimeter of the
          surface. You can either ignore this error or mark it as an exception.
          Use this rule for data that must completely cover an area. For
          example, soil polygons cannot include gaps or form voids; they must
          cover an entire area.Must Not Overlap (Area)-The interior of polygons
          must not overlap.
          The polygons can share edges or vertices. This rule is used when an
          area cannot belong to two or more polygons. It is useful for modeling
          administrative boundaries, such as ZIP Codes or voting districts, and
          mutually exclusive area classifications, such as land cover or
          landform type.Must Be Covered By Feature Class Of (Area-Area)-A
          polygon in one
          feature class (or subtype) must share all of its area with polygons in
          another feature class (or subtype). An area in the first feature class
          that is not covered by polygons from the other feature class is an
          error. This rule is used when an area of one type, such as a state,
          should be completely covered by areas of another type, such as
          counties.Must Cover Each Other (Area-Area)-The polygons of one feature
          class
          (or subtype) must share all of their area with the polygons of another
          feature class (or subtype). Polygons may share edges or vertices. Any
          area defined in either feature class that is not shared with the other
          is an error. This rule is used when two systems of classification are
          used for the same geographic area, and any given point defined in one
          system must also be defined in the other. One such case occurs with
          nested hierarchical datasets, such as census blocks and block groups
          or small watersheds and large drainage basins. The rule can also be
          applied to nonhierarchically related polygon feature classes, such as
          soil type and slope class.Must Be Covered By (Area-Area)-The polygons
          of one feature class (or
          subtype) must be contained within polygons of another feature class
          (or subtype). Polygons may share edges or vertices. Any area defined
          in the contained feature class must be covered by an area in the
          covering feature class. This rule is used when area features of a
          given type must be located within features of another type. This rule
          is useful when modeling areas that are subsets of a larger surrounding
          area, such as management units within forests or blocks within block
          groups.Must Not Overlap With (Area-Area)-The interior of polygons in
          one
          feature class (or subtype) must not overlap with the interior of
          polygons in another feature class (or subtype). Polygons of the two
          feature classes can share edges or vertices or be completely
          disjointed. This rule is used when an area cannot belong to two
          separate feature classes. It is useful for combining two mutually
          exclusive systems of area classification, such as zoning and water
          body type, in which areas defined within the zoning class cannot also
          be defined in the water body class and vice versa.Must Be Covered By
          Boundary Of (Line-Area)-Lines must be covered by
          the boundaries of area features. This is useful for modeling lines,
          such as lot lines, that must coincide with the edge of polygon
          features, such as lots.Must Be Covered By Boundary Of (Point-
          Area)-Points must fall on the
          boundaries of area features. This is useful when the point features
          help support the boundary system, such as boundary markers, which must
          be found on the edges of certain areas.Must Be Properly Inside (Point-
          Area)-Points must fall within area
          features. This is useful when the point features are related to
          polygons, such as wells and well pads or address points and
          parcels.Must Not Overlap (Line)-Lines must not overlap with lines in
          the same
          feature class (or subtype). This rule is used when line segments
          should not be duplicated, for example, in a stream feature class.
          Lines can cross or intersect but cannot share segments.Must Not
          Intersect (Line)-Line features from the same feature class
          (or subtype) must not cross or overlap each other. Lines can share
          endpoints. This rule is used for contour lines that should never cross
          each other or when the intersection of lines should only occur at
          endpoints, such as street segments and intersections.Must Not Have
          Dangles (Line)-A line feature must touch lines from the
          same feature class (or subtype) at both endpoints. An endpoint that is
          not connected to another line is called a dangle. This rule is used
          when line features must form closed loops, such as when they are
          defining the boundaries of polygon features. It can also be used when
          lines typically connect to other lines, as with streets. In this case,
          exceptions can be used when the rule is occasionally violated, as with
          cul-de-sac or dead-end street segments.Must Not Have Pseudo-Nodes
          (Line)-A line must connect to at least two
          other lines at each endpoint. Lines that connect to one other line (or
          to themselves) are considered to have pseudo nodes. This rule is used
          when line features must form closed loops, such as when they define
          the boundaries of polygons or when line features logically must
          connect to two other line features at each end, as with segments in a
          stream network, with exceptions being marked for the originating ends
          of first-order streams.Must Be Covered By Feature Class Of (Line-
          Line)-Lines from one
          feature class (or subtype) must be covered by the lines in another
          feature class (or subtype). This is useful for modeling logically
          different but spatially coincident lines, such as routes and streets.
          For example, a bus route feature class must not depart from the
          streets defined in the street feature class.Must Not Overlap With
          (Line-Line)-A line from one feature class (or
          subtype) must not overlap with line features in another feature class
          (or subtype). This rule is used when line features cannot share the
          same space. For example, roads must not overlap with railroads, or
          depression subtypes of contour lines cannot overlap with other contour
          lines.Must Be Covered By (Point-Line)-Points in one feature class
          must be
          covered by lines in another feature class. It does not constrain the
          covering portion of the line to be an endpoint. This rule is useful
          for points that fall along a set of lines, such as highway signs along
          highways.Must Be Covered By Endpoint Of (Point-Line)-Points in one
          feature
          class must be covered by the endpoints of lines in another feature
          class. This rule is similar to the Endpoint Must Be Covered By line
          rule except that, in cases where the rule is violated, it is the point
          feature that is marked as an error rather than the line. Boundary
          corner markers may be constrained to be covered by the endpoints of
          boundary lines.Boundary Must Be Covered By (Area-Line)-Boundaries of
          polygon
          features must be covered by lines in another feature class. This rule
          is used when area features must have line features that mark the
          boundaries of the areas. This is usually when the areas have one set
          of attributes and their boundaries have other attributes. For example,
          parcels are stored in the geodatabase along with their boundaries.
          Each parcel is defined by one or more line features that store
          information about their length or the date surveyed, and every parcel
          must exactly match its boundaries.Boundary Must Be Covered By Boundary
          Of (Area-Area)-Boundaries of
          polygon features in one feature class (or subtype) must be covered by
          boundaries of polygon features in another feature class (or subtype).
          This is useful when polygon features in one feature class, such as
          subdivisions, are composed of multiple polygons in another class, such
          as parcels, and the shared boundaries must be aligned.Must Not Self-
          Overlap (Line)-Line features must not overlap
          themselves. They can cross or touch but must not have coincident
          segments. This rule is useful for features, such as streets, in which
          segments might touch in a loop but the same street must not follow the
          same course twice.Must Not Self-Intersect (Line)-Line features must
          not cross or overlap
          themselves. This rule is useful for lines, such as contour lines, that
          cannot cross themselves.Must Not Intersect Or Touch Interior (Line)-A
          line in one feature
          class (or subtype) must only touch other lines of the same feature
          class (or subtype) at endpoints. Any line segment in which features
          overlap or any intersection that is not at an endpoint is an error.
          This rule is useful when lines must only be connected at endpoints,
          such as lot lines, which must split (only connect to the endpoints of)
          back lot lines and cannot overlap each other.Endpoint Must Be Covered
          By (Line-Point)-The endpoints of line
          features must be covered by point features in another feature class.
          This is useful for modeling cases in which a fitting must connect two
          pipes, or a street intersection must be found at the junction of two
          streets.Contains Point (Area-Point)-A polygon in one feature class
          must
          contain at least one point from another feature class. Points must be
          within the polygon, not on the boundary. This is useful when every
          polygon must have at least one associated point, such as when parcels
          must have an address point.Must Be Single Part (Line)-Lines must have
          only one part. This rule is
          useful when line features, such as highways, may not have multiple
          parts.Must Coincide With (Point-Point)-Points in one feature class (or
          subtype) must be coincident with points in another feature class (or
          subtype). This is useful when points must be covered by other points,
          such as transformers that must coincide with power poles in electric
          distribution networks and observation points that must coincide with
          stations.Must Be Disjoint (Point)-Points must be separated spatially
          from other
          points in the same feature class (or subtype). Any points that overlap
          are errors. This is useful for ensuring that points are not coincident
          or duplicated in the same feature class, such as in layers of cities,
          parcel lot ID points, wells, or street lamp poles.Must Not Intersect
          With (Line-Line)-Line features from one feature
          class (or subtype) must not cross or overlap lines from another
          feature class (or subtype). Lines can share endpoints. This rule is
          used when lines from two layers should never cross each other or when
          the intersection of lines should only occur at endpoints, such as
          streets and railroads.Must Not Intersect or Touch Interior With (Line-
          Line)-A line in one
          feature class (or subtype) must only touch other lines of another
          feature class (or subtype) at endpoints. Any line segment in which
          features overlap or any intersection that is not at an endpoint is an
          error. This rule is useful when lines from two layers must only be
          connected at endpoints.Must Be Inside (Line-Area)-A line must be
          contained within the
          boundary of an area feature. This is useful when lines may partially
          or totally coincide with area boundaries but cannot extend beyond
          polygons, such as state highways that must be inside state borders and
          rivers that must be within watersheds.Contains One Point (Area-Point)-
          Each polygon must contain one point
          feature and each point feature must fall within a single polygon. This
          is used when there must be a one-to-one correspondence between
          features of a polygon feature class and features of a point feature
          class, such as administrative boundaries and their capital cities.
          Each point must be properly inside exactly one polygon and each
          polygon must properly contain exactly one point. Points must be within
          the polygon, not on the boundary.
      in_featureclass (Feature Layer):
          The input or origin feature class.
      subtype {String}:
          The subtype for the input or origin feature class. Provide the subtype
          description (not the code). If subtypes do not exist on the input
          feature class, or you want the rule to be applied to all subtypes in
          the feature class, leave this parameter blank.
      in_featureclass2 {Feature Layer}:
          The destination feature class for the topology rule.
      subtype2 {String}:
          The subtype for the destination feature class. Provide the subtype
          description (not the code). If subtypes do not exist on the origin
          feature class, or you want the rule to be applied to all subtypes in
          the feature class, leave this parameter blank.

        """