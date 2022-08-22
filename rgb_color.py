import streamlit as st

st.title('RGB Color')

st.markdown('Choose a Red Green Blue combination to get the resulting color:')
col1, col2, col3 = st.columns(3)

with col1:
	red_value=st.slider("Red",min_value=0,max_value=255, step=1)
with col2:
	green_value=st.slider("Green",min_value=0,max_value=255, step=1)
with col3:
	blue_value=st.slider("Blue",min_value=0,max_value=255, step=1)

rgb_value='('+str(red_value)+','+str(green_value)+','+str(blue_value)+')'
hex_value='#%02x%02x%02x' % (red_value,green_value,blue_value)

col4, col5, col6 = st.columns(3)
with col4:
	st.markdown('''<p  style="font-size: 14px;">Color</p>''', unsafe_allow_html=True)
	st.markdown(f'''<div style="width:px; height:40px; background-color:{hex_value};">
					</div>''', unsafe_allow_html=True)
with col5:
	st.metric('RGB',rgb_value)
with col6:	
	st.metric('HEX',hex_value.upper())
	
