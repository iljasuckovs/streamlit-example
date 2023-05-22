import streamlit as st
import pandas as pd
from io import StringIO
st.write("DXF bounding box Calculator!")
st.write("Upload DXF file bellow")



uploaded_file = st.file_uploader("Choose a file")

##

from shapely.geometry import Polygon

def get_bounding_box_coordinates(filename):
    doc = ezdxf.readfile(filename)
    modelspace = doc.modelspace()

    points = []
    for entity in modelspace:
        if entity.dxftype() == 'LINE':
            points.extend(entity.get_points())

    polygon = Polygon(points)
    bounds = polygon.bounds

    return bounds

def main():
    st.title("DXF File Bounding Box")

    st.sidebar.title("Upload DXF File")
    uploaded_file = st.sidebar.file_uploader("Choose a DXF file", type=".dxf")

    if uploaded_file:
        bounds = get_bounding_box_coordinates(uploaded_file)

        st.header("Bounding Box Coordinates")
        st.write("Min X:", bounds[0])
        st.write("Min Y:", bounds[1])
        st.write("Max X:", bounds[2])
        st.write("Max Y:", bounds[3])

if __name__ == "__main__":
    main()
