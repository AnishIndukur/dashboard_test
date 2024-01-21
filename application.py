import os
import streamlit as st
import utils as utl
from PIL import Image
import time
def main():    
    # Settings
    st.set_page_config(layout="wide", page_title='Demo item')
    utl.set_page_title('Inshop Analytics tool')
    st.set_option('deprecation.showPyplotGlobalUse', False)
    # Loading CSS
    utl.local_css("frontend/css/streamlit.css")
    utl.remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
    # Logo
    dir_root = os.path.dirname(os.path.abspath(__file__))
    logo = Image.open(dir_root+'/logo.png')
    # Selecting a job
    # st.sidebar.image(logo)
    st.sidebar.selectbox('Select',('loren','Ipsum'))
    st.sidebar.button(st.markdown(
                                    <span class="text">Active</span><span class="text-2">Model 1<br /></span
                                    ><span class="text-3">Last Localized: 12.02.22</span>
                                    <div class="section">
                                        <div class="wrapper">
                                        <span class="text-4">0.##</span><span class="text-5">0.##</span
                                        ><span class="text-6">0.##</span>
                                        </div>
                                        <div class="wrapper-2">
                                        <span class="text-7">AUC</span><span class="text-8">Accuracy</span
                                        ><span class="text-9">FPR</span>
                                        </div>
                                    </div>
                                    <div class="group"></div>
                                  
                                  ))
                      
    st.sidebar.multiselect('Multi',('loren','Ipsum'))
    st.sidebar.date_input('Date')
    st.sidebar.text_input('Text')
    st.sidebar.slider('Slider',min_value=5,max_value=20)
    st.warning('Warning')
    st.info('Info')
    st.error('Error')
    
    with utl.stNotification('Sample notification, always on top and floats (spiner is optional)'):
        time.sleep(5)


if __name__ == '__main__':
    main()
