from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import os
import ezdxf

def calculate_bounding_box(file_path):
    try:
        doc = ezdxf.readfile(file_path)
        modelspace = doc.modelspace()
        bounding_box = modelspace.boundary()
        return bounding_box
    except ezdxf.DXFError as e:
        st.error("Error reading DXF file: " + str(e))
        return None

def main():
    st.title("DXF Bounding Box")
    uploaded_file = st.file_uploader("Upload DXF file", type=["dxf"])

    if uploaded_file is not None:
        file_path = os.path.join("uploads", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("File uploaded successfully.")

        bounding_box = calculate_bounding_box(file_path)
        if bounding_box:
            st.header("Bounding Box")
            st.write("Min point:", bounding_box.min)
            st.write("Max point:", bounding_box.max)

if __name__ == "__main__":
    main()
