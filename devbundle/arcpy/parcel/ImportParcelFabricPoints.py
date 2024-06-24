# Generated documentation for module arcpy.parcel


class ImportParcelFabricPoints(object):
    """
    Imports point data from a source point feature class into the parcel fabric points feature class. Parcel fabric points that match or lie within a proximity tolerance of the source points can be updated with the imported point data. If the source points layer has a selection, only the selected point information will be imported.
    """

    @property
    def description(self) -> str:
        return """

        ImportParcelFabricPoints_parcel(source_points, target_parcel_fabric, match_point_method, search_distance, update_type, {record_name}, {match_field}, {conflicts_table}, {update_create_option}, {target_points}, {where_clause})

        Imports point data from a source point feature class into the parcel
        fabric points feature class. Parcel fabric points that match or lie
        within a proximity tolerance of the source points can be updated with
        the imported point data. If the source points layer has a selection,
        only the selected point information will be imported.

     INPUTS:
      source_points (Feature Layer):
          The source point feature class that will be used to create or update
          points in the target parcel fabric.
      target_parcel_fabric (Parcel Layer):
          The target parcel fabric in which points will be updated or created.
          The target parcel fabric can be from a file geodatabase, an enterprise
          geodatabase connected to the default version, a mobile geodatabase, or
          a feature service.
      match_point_method (String):
          Specifies the method that will be used to find existing parcel fabric
          points that match the source points.PROXIMITY-Parcel fabric points
          that lie within the proximity tolerance
          of the source points will be matched to the source points and updated.
          This is the default.NAME_AND_PROXIMITY-Parcel fabric points that lie
          within the proximity
          tolerance and have the same name as the source points will be matched
          to the source points and updated.
          GLOBALID_AND_PROXIMITY-Parcel fabric points that lie within
          the proximity tolerance and have the same Global ID as the source
          points will be matched to the source points and updated. Global IDs
          are stored in thefield of the parcel fabric points feature class and
          in a specifiedfield of the source feature class. Global
          IDGlobal ID
      search_distance (Linear Unit):
          The distance that will be used to search for parcel fabric points that
          lie within the proximity of the source points.
      update_type (String):
          Specifies the type of update that will be applied to parcel fabric
          points that match source points.ALL-The geometry (x,y,z) and matching
          attribute fields of parcel
          fabric points will be updated. If the geometry of parcel fabric points
          is updated, coincident parcel features will be updated as well. This
          is the default.GEOMETRY_XYZ-Only the geometry (x,y,z) of the parcel
          fabric points
          will be updated. If the geometry of parcel fabric points is updated,
          coincident parcel features will be updated as well.
          RETIRE_AND_REPLACE-Source points will be imported as new
          parcel fabric points. Any matching parcel fabric points will be
          retired as historic. Thefield of each matching parcel fabric point
          will be populated with the Global ID of the record specified in
          theparameter. Retired By RecordRecord Name
      record_name {String}:
          The name of the record that will be associated with the new imported
          points.If the record exists in the target parcel fabric, the new
          points will
          be associated with the record. If the record does not exist, a record
          will be created. If new points replace existing points, and
          update_type is RETIRE_AND_REPLACE, the record will be used to retire
          the points as historic.
      match_field {Field}:
          The field that will be used to match source points to parcel fabric
          points when NAME_AND_PROXIMITY or GLOBALID_AND_PROXIMITY is used for
          the match_point_method parameter. When searching by name, the field in
          the source point feature class should be of type Text. When searching
          by Global ID, the field in the source point feature class should be of
          type GUID.
      update_create_option {String}:
          Specifies whether points will be updated, created, or both. When
          specifying the UPDATE_AND_CREATE or UPDATE_ONLY option, optional
          parameters are available to filter the matching target parcel fabric
          points. Existing points will not be updated if theirfield is
          set to
          Yes. IsFixedUPDATE_AND_CREATE-Points will be created if no
          matching points are
          found using the search criteria. If matching points are found using
          the search criteria, they will be updated. Matching points in the
          target parcel fabric can optionally be filtered using an SQL
          expression. This is the default.CREATE_ONLY-Points will be created
          only if no matching points are
          found using the search criteria. If matching points are found using
          the search criteria, they will remain unchanged and no points will be
          created.UPDATE_ONLY-Points will be updated if matching points are
          found using
          the search criteria. Matching points in the target parcel fabric can
          optionally be filtered using an SQL expression. If no matching points
          are found, points will not be updated.
      target_points {Feature Layer}:
          The parcel fabric points layer that will be filtered by an SQL
          expression.
      where_clause {SQL Expression}:
          An SQL expression that filters the matching points found in the target
          parcel fabric points layer. For example, only update matching points
          that are not retired as historic (RetiredByRecord IS NULL).

     OUTPUTS:
      conflicts_table {Table}:
          The path and name of the output table that will store conflicts. If
          more than one parcel fabric point is found within the search tolerance
          of a source point, the Object IDs of the source points and parcel
          fabric points will be reported in the conflicts table.

        """