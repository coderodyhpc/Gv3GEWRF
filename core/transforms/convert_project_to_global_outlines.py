# Gv3GEWRF Plugin
# Copyright (c) 2022 Odycloud.

from Gv3GEWRF.core.project import Project
from Gv3GEWRF.core.crs import BoundingBox2D
from Gv3GEWRF.core.util import export, ogr

@export
def convert_project_to_gdal_outlines(project: Project) -> ogr.DataSource:
    drv = ogr.GetDriverByName('Memory') # type: ogr.Driver
    ds = drv.CreateDataSource('') # type: ogr.DataSource
    add_domains_to_datasource(ds, project)
    return ds

def add_domains_to_datasource(ds: ogr.DataSource, project: Project) -> None:
    layer = ds.CreateLayer('domains', srs=project.projection.srs, geom_type=ogr.wkbPolygon) # type: ogr.Layer

    bboxes = project.bboxes

    feature_defn = layer.GetLayerDefn()
    for bbox in bboxes:
        geom = get_bbox_polygon(bbox)
        feature = ogr.Feature(feature_defn)
        feature.SetGeometry(geom)
        layer.CreateFeature(feature)

def get_bbox_polygon(bbox: BoundingBox2D) -> ogr.Geometry:
    ring = ogr.Geometry(ogr.wkbLinearRing)
    ring.AddPoint(bbox.minx, bbox.miny)
    ring.AddPoint(bbox.maxx, bbox.miny)
    ring.AddPoint(bbox.maxx, bbox.maxy)
    ring.AddPoint(bbox.minx, bbox.maxy)
    ring.AddPoint(bbox.minx, bbox.miny)

    poly = ogr.Geometry(ogr.wkbPolygon)
    poly.AddGeometry(ring)
    return poly
