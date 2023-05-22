import streamlit as st
import pandas as pd
from io import StringIO
import ezdxf
st.write("DXF bounding box Calculator!")
st.write("Upload DXF file bellow")



uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
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
