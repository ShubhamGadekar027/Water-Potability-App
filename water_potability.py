import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import pickle



#################################################################    

Context = '''
1) pH value: PH is an important parameter in evaluating the acid–base balance of water. It is also the indicator of acidic or alkaline condition of water status. WHO has recommended maximum permissible limit of pH from 6.5 to 8.5. The current investigation ranges were 6.52–6.83 which are in the range of WHO standards.

2) Hardness: Hardness is mainly caused by calcium and magnesium salts. These salts are dissolved from geologic deposits through which water travels. The length of time water is in contact with hardness producing material helps determine how much hardness there is in raw water. Hardness was originally defined as the capacity of water to precipitate soap caused by Calcium and Magnesium.

3) Solids (Total dissolved solids - TDS): Water has the ability to dissolve a wide range of inorganic and some organic minerals or salts such as potassium, calcium, sodium, bicarbonates, chlorides, magnesium, sulfates etc. These minerals produced un-wanted taste and diluted color in appearance of water. This is the important parameter for the use of water. The water with high TDS value indicates that water is highly mineralized. Desirable limit for TDS is 500 mg/l and maximum limit is 1000 mg/l which prescribed for drinking purpose.

4) Chloramines: Chlorine and chloramine are the major disinfectants used in public water systems. Chloramines are most commonly formed when ammonia is added to chlorine to treat drinking water. Chlorine levels up to 4 milligrams per liter (mg/L or 4 parts per million (ppm)) are considered safe in drinking water.

5) Sulfate: Sulfates are naturally occurring substances that are found in minerals, soil, and rocks. They are present in ambient air, groundwater, plants, and food. The principal commercial use of sulfate is in the chemical industry. Sulfate concentration in seawater is about 2,700 milligrams per liter (mg/L). It ranges from 3 to 30 mg/L in most freshwater supplies, although much higher concentrations (1000 mg/L) are found in some geographic locations.

6) Conductivity: Pure water is not a good conductor of electric current rather’s a good insulator. Increase in ions concentration enhances the electrical conductivity of water. Generally, the amount of dissolved solids in water determines the electrical conductivity. Electrical conductivity (EC) actually measures the ionic process of a solution that enables it to transmit current. According to WHO standards, EC value should not exceeded 400 μS/cm.

7) Organic_carbon: Total Organic Carbon (TOC) in source waters comes from decaying natural organic matter (NOM) as well as synthetic sources. TOC is a measure of the total amount of carbon in organic compounds in pure water. According to US EPA < 2 mg/L as TOC in treated / drinking water, and < 4 mg/Lit in source water which is use for treatment.

9) Trihalomethanes: THMs are chemicals which may be found in water treated with chlorine. The concentration of THMs in drinking water varies according to the level of organic material in the water, the amount of chlorine required to treat the water, and the temperature of the water that is being treated. THM levels up to 80 ppm is considered safe in drinking water.

10) Turbidity: The turbidity of water depends on the quantity of solid matter present in the suspended state. It is a measure of light emitting properties of water and the test is used to indicate the quality of waste discharge with respect to colloidal matter. The mean turbidity value obtained for Wondo Genet Campus (0.98 NTU) is lower than the WHO recommended value of 5.00 NTU.

NOTE :

Potability: Indicates if water is safe for human consumption where 1 means Potable and 0 means Not potable.
'''

Img = Image.open('Water_Img.jpg')

# Get the Keys
def get_value(val,my_dict):
    for key ,value in my_dict.items():
        if val == key:
            return value

# Find the Key From Dictionary
def get_key(val,my_dict):
    for key ,value in my_dict.items():
        if val == value:
            return key



def main():
    st.title('Water Potability Prediction App')
    st.write('By : Shubham Gadekar')
    #Menu
    menu = ['Prediction', 'About']
    choice = st.sidebar.selectbox('Select Activities', menu)

    if choice == 'Prediction':
        st.image(Img, width=700)

        ph = st.slider('What is the ph of Water?', 0., 14.)
        Hardness = st.slider("What is the Hardness of Water",47.,323.)
        Solids = st.slider("What are the amount of Solids in Water?", 320., 61227.)
        Chloramines	    = st.slider("What is the amount of Chloramines in Water?", 0.3, 12.5)
        Sulfate     = st.slider('How much Sulphate content in Water?', 187., 476.)
        Conductivity  = st.slider("What is the Conductivity of Water",201., 753.)
        Organic_carbon  = st.slider('What is the Organic_carbon content of Water?',2., 28.)
        Trihalomethanes = st.slider('What is the Trihalomethanes content of Water?',0.7, 124.)
        Turbidity  = st.slider('What is the amount of Turbidity of Water?', 1.4, 6.7)


        #Data That Will Use For Prediction
        input_data = [ph, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes,    Turbidity]

        # Converted the input list to a DataFrame
        df_input_data = pd.DataFrame(input_data)

        input_for_model = np.array(df_input_data).reshape(1, -1)
    


        #Prediction
        if st.button("Predict!"):
            predictor = pickle.load(open("DT_Model.pkl", 'rb'))
            prediction = predictor.predict(input_for_model)

            #Converting array to String
            listToStr = ' '.join([str(element) for element in prediction]) 

            if listToStr == '0':
                st.error('The water is Not Safe for Human consumption!', icon="🚨")
            else:
                st.success('The water is Safe for Human consumption!', icon="✅")   


    
    if choice == 'About':
        st.header('About This Project')
        # st.image(img, width=700)
        st.write(Context)
   


if __name__ == '__main__':
    main()