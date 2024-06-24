# Generated documentation for module arcpy.parcel


class AddParcelType(object):
    """
    Adds a parcel type to a parcel fabric. A parcel type is defined by a separate polygon and line feature class. Parcel type feature classes are controlled by the parcel fabric dataset.
    """

    @property
    def description(self) -> str:
        return """

        AddParcelType_parcel(in_parcel_fabric, name, {administrative_polygon})

        Adds a parcel type to a parcel fabric. A parcel type is defined by a
        separate polygon and line feature class. Parcel type feature classes
        are controlled by the parcel fabric dataset.

     INPUTS:
      in_parcel_fabric (Parcel Layer):
          The parcel fabric to which the parcel type will be added. The parcel
          fabric can be from a file, enterprise, or mobile geodatabase.
      name (String):
          The name of the parcel type. The name will be assigned to the output
          polygon and line feature classes.
      administrative_polygon {Boolean}:
          Specifies whether the parcel type will be used to store parcels with
          administrative boundaries or regular boundaries. Administrative
          boundaries are used for very large parcels such as country parcels or
          state parcels. The parcel type polygon feature class will not
          participate in the parcel fabric topology.ADMINISTRATIVE_POLYGON-The
          parcel type will be used to store
          administrative boundaries. The parcel type polygon feature class will
          not participate in the parcel fabric topology.TOPOLOGY_POLYGON-The
          parcel type will not be used to store
          administrative boundaries. The parcel type polygon feature class will
          participate in the parcel fabric topology. This is the default.

        """