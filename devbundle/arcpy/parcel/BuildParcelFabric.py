# Generated documentation for module arcpy.parcel


class BuildParcelFabric(object):
    """
    Builds parcels in a parcel fabric. Parcels can be built from polygons or lines. If parcels are built from polygons, the tool creates parcel lines and parcel points. If parcels are built from lines, the tool creates the missing polygons and points. When building parcels from lines, parcel seeds are required.
    """

    @property
    def description(self) -> str:
        return """

        BuildParcelFabric_parcel(in_parcel_fabric, {extent}, {record_name})

        Builds parcels in a parcel fabric. Parcels can be built from polygons
        or lines. If parcels are built from polygons, the tool creates parcel
        lines and parcel points. If parcels are built from lines, the tool
        creates the missing polygons and points. When building parcels from
        lines, parcel seeds are required.

     INPUTS:
      in_parcel_fabric (Parcel Layer):
          The parcel fabric for which to parcels will be built. The parcel
          fabric can be from a file or mobile geodatabase, or from a feature
          service.
      extent {Extent}:
          The extent of the dataset to be processed. Only features that fall
          within the specified extent will be processed.MAXOF-The maximum extent
          of all inputs will be used.MINOF-The minimum
          area common to all inputs will be used.DISPLAY-The extent is equal to
          the visible display.Layer name-The extent of the specified layer will
          be used.Extent object-The extent of the specified object will be
          used.Space delimited string of coordinates-The extent of the specified
          string will be used. Coordinates are expressed in the order of x-min,
          y-min, x-max, y-max.
      record_name {String}:
          The name of the existing parcel record. Only parcels associated with
          this record will be built.

        """