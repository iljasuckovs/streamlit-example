import streamlit as st
import ezdxf

def calculate_bounding_box(file):
    dxf = ezdxf.read(file)
    modelspace = dxf.modelspace()
    bbox = modelspace.bbox()
    return {
        'min_point': (bbox.min.x, bbox.min.y),
        'max_point': (bbox.max.x, bbox.max.y)
    }

def main():
    st.title('DXF File Upload')
    uploaded_file = st.file_uploader('Upload a DXF file', type=['dxf'])
    if uploaded_file:
        bounding_box = calculate_bounding_box(uploaded_file)
        st.header('Bounding Box')
        st.write('Min Point:', bounding_box['min_point'])
        st.write('Max Point:', bounding_box['max_point'])

if __name__ == '__main__':
    main()
