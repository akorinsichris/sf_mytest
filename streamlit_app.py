import streamlit as st


st.set_page_config(page_title="HPD Classification",page_icon="❄️")

# Add header and a subheader
st.header("Classification Heart Patient Data")

session = create_session_object()

with st.sidebar:
    option = option_menu("Snowpark Classification Demo", ["Load Data", "Analyze", "Train Model", "Model Catalog",
                                                            "Inference", "Inference Runs"],
                            icons=['upload','graph-up', 'play-circle','list-task', 'boxes', 'speedometer2'],
                            menu_icon="snow", default_index=0,
                            styles={
            "container": {"padding": "5!important", "background-color": "white","font-color": "#249dda"},
            "icon": {"color": "#31c0e7", "font-size": "25px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "white"},
            "nav-link-selected": {"background-color": "7734f9"},
        })
    
