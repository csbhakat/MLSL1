# -*- coding: utf-8 -*-
"""
Created for MLSL1 assignment

@author: CSB
"""

# -*- coding: utf-8 -*-
"""
Created for MLSL1 assignment

@author: CSB
"""
import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("finalized_model.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(df):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict(df)
    print(prediction)
    return prediction



def main():
    st.sidebar.header('User Input Features')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Shipment Delay Predictor</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Source = st.sidebar.selectbox('Source', ('IAD', 'IND', 'ISP', 'JAN', 'JAX', 'LAS', 'LAX', 'LBB', 'LIT','MAF', 'MCI', 'MCO', 'MDW', 'MHT', 'MSY', 'OAK', 'OKC', 'OMA','ONT', 'ORF', 'PBI', 'PDX', 'PHL', 'PHX', 'PIT', 'PVD', 'RDU','RNO', 'RSW', 'SAN', 'SAT', 'SDF', 'SEA', 'SFO', 'SJC', 'SLC','SMF', 'SNA', 'STL', 'TPA', 'TUL', 'TUS', 'ABQ', 'ALB', 'AMA','AUS', 'BDL', 'BHM', 'BNA', 'BOI', 'BUF', 'BUR', 'BWI', 'CLE','CMH', 'CRP', 'DAL', 'DEN', 'DTW', 'ELP', 'FLL', 'GEG', 'HOU','HRL', 'ROC', 'DAY', 'ORD', 'EWR', 'SYR', 'IAH', 'LFT', 'MKE','CHS', 'LCH', 'CLT', 'BTR', 'CRW', 'FAT', 'COS', 'MRY', 'LGB','BFL', 'EUG', 'ICT', 'MEM', 'LGA', 'DCA', 'BTV', 'GRK', 'BRO','TYS', 'DSM', 'BPT', 'GPT', 'GRR', 'PWM', 'MSP', 'RIC', 'CVG','SAV', 'SRQ', 'GSO', 'CHA', 'XNA', 'GSP', 'LEX', 'MFE', 'ABE','MLU', 'MOB', 'LRD', 'SHV', 'TLH', 'CAE', 'AEX', 'ATL', 'DFW','BGR', 'AVL', 'BOS', 'MSN', 'HSV', 'MGM', 'MYR', 'VPS', 'CLL','PNS', 'MTJ', 'DAB', 'PSP', 'ASE', 'ATW', 'AVP', 'BMI', 'CAK','CID', 'CLD', 'COD', 'CPR', 'CWA', 'DRO', 'EGE', 'FLG', 'FSD','FWA', 'GJT', 'GRB', 'HDN', 'HNL', 'ILM', 'ITO', 'JFK', 'KOA','LAN', 'LIH', 'MBS', 'MDT', 'MFR', 'OGG', 'RAP', 'ROA', 'SBA','SBN', 'SBP', 'SPI', 'TEX', 'YUM', 'TVC', 'HPN', 'MIA', 'MLB','SGF', 'TRI', 'ACY', 'TWF', 'SUN', 'PIH', 'EKO', 'SGU', 'PSC','BTM', 'SLE', 'IDA', 'HLN', 'FCA', 'MSO', 'GTF', 'LWS', 'YKM','BZN', 'BIL', 'RDM', 'FAR', 'JAC', 'IYK', 'SMX', 'ACV', 'OXR','RDD', 'CEC', 'MOD', 'CIC', 'IPL', 'PIA', 'MLI', 'GUC', 'AZO','LNK', 'PMD', 'BIS', 'RFD', 'BLI', 'CDC', 'SJU', 'STT', 'ANC','STX', 'PHF', 'DHN', 'PFN', 'TOL', 'AGS', 'FAY', 'HHH', 'EVV', 'GNV', 'ABY', 'FNT', 'OAJ', 'BQK', 'SWF', 'EWN', 'MEI', 'GTR', 'LYH', 'FSM', 'EYW', 'VLD', 'CSG', 'MCN', 'CHO', 'TUP', 'FLO','SCE', 'TYR', 'LAW', 'SPS', 'ABI', 'GGG', 'ACT', 'SJT', 'TXK','CMI', 'ROW', 'RST', 'MQT', 'LSE', 'DBQ', 'GFK', 'MOT', 'DLH','SUX', 'PLN', 'BGM', 'ERI', 'ALO', 'CMX', 'RHI', 'ELM', 'JNU','KTN', 'ADQ', 'FAI', 'SIT', 'PSG', 'WRG', 'SCC', 'BET', 'CDV','OME', 'YAK', 'BRW', 'OTZ', 'ADK', 'BQN', 'PSE', 'GCC', 'RKS','MKG', 'DLG', 'AKN', 'LWB', 'ACK', 'WYS', 'BJI', 'INL', 'GST'))

    Destination = st.sidebar.selectbox('Destination', ('TPA', 'BWI', 'JAX', 'LAS', 'MCI', 'MCO', 'MDW', 'PHX', 'FLL','PBI', 'RSW', 'HOU', 'BHM', 'BNA', 'IND', 'ORF', 'PHL', 'ABQ','ALB', 'AMA', 'AUS', 'BDL', 'BOI', 'BUF', 'BUR', 'CLE', 'CMH','DEN', 'ELP', 'GEG', 'IAD', 'ISP', 'LAX', 'LBB', 'LIT', 'MAF','MHT', 'MSY', 'OAK', 'OKC', 'OMA', 'ONT', 'PDX', 'PIT', 'PVD','RDU', 'RNO', 'SAN', 'SAT', 'SDF', 'SEA', 'SFO', 'SJC', 'SLC','SMF', 'SNA', 'STL', 'TUL', 'TUS', 'DAL', 'DTW', 'JAN', 'HRL','CRP', 'EWR', 'IAH', 'XNA', 'DCA', 'GSO', 'ROC', 'MYR', 'SYR', 'ATL', 'SAV', 'RIC', 'COS', 'FAT', 'MRY', 'LGB', 'BFL', 'EUG','ICT', 'MSN', 'CAE', 'DAY', 'BTR', 'TLH', 'DFW', 'LFT', 'PWM','SHV', 'MKE', 'CHS', 'CRW', 'HSV', 'TYS', 'MTJ', 'MGM', 'MFE','MSP', 'GSP', 'GRR', 'MEM', 'BTV', 'CLT', 'BRO', 'CVG', 'LGA','VPS', 'LEX', 'BPT', 'PNS', 'ORD', 'ABE', 'LRD', 'BGR', 'GRK','SRQ', 'LCH', 'AEX', 'AVL', 'GPT', 'MLU', 'MOB', 'BOS', 'DSM','CHA', 'CLL', 'PSP', 'DAB', 'ILM', 'JFK', 'MDT', 'ASE', 'COD','CPR', 'DRO', 'EGE', 'GJT', 'HDN', 'RAP', 'ITO', 'KOA', 'LIH','OGG', 'ROA', 'SPI', 'HNL', 'MFR', 'SBA', 'SBP', 'YUM', 'ATW','AVP', 'BMI', 'CAK', 'CID', 'CWA', 'FSD', 'FWA', 'GRB', 'LAN','MBS', 'SBN', 'CLD', 'FLG', 'TEX', 'TVC', 'MLB', 'SGF', 'MIA','HPN', 'TRI', 'TWF', 'PIH', 'SUN', 'EKO', 'SGU', 'PSC', 'BTM','BIL', 'FAR', 'IDA', 'BZN', 'MSO', 'FCA', 'HLN', 'GTF', 'LWS','YKM', 'SLE', 'RDM', 'BLI', 'JAC', 'IYK', 'SMX', 'ACV', 'OXR','RDD', 'MOD', 'CEC', 'CIC', 'IPL', 'PIA', 'LNK', 'GUC', 'AZO','MLI', 'PMD', 'BIS', 'RFD', 'CDC', 'OGD', 'STT', 'SJU', 'ANC','STX', 'PHF', 'MCN', 'VLD', 'CSG', 'SWF', 'BQK', 'DHN', 'ABY','AGS', 'MEI', 'FAY', 'EWN', 'SCE', 'EYW', 'EVV', 'PFN', 'GNV','OAJ', 'FNT', 'CHO', 'FSM', 'FLO', 'HHH', 'TOL', 'LYH', 'GTR','TUP', 'ACY', 'LAW', 'TYR', 'ABI', 'TXK', 'ACT', 'SPS', 'SJT','GGG', 'CMI', 'ROW', 'MQT', 'RST', 'LSE', 'DBQ', 'DLH', 'GFK','MOT', 'RHI', 'SUX', 'CMX', 'BGM', 'PLN', 'ERI', 'ALO', 'ELM','FAI', 'KTN', 'SIT', 'JNU', 'WRG', 'PSG', 'CDV', 'BET', 'OTZ','YAK', 'OME', 'ADQ', 'BRW', 'SCC', 'ADK', 'PSE', 'BQN', 'GCC','RKS', 'CYS', 'MKG', 'AKN', 'DLG', 'LWB', 'ACK', 'WYS', 'INL','BJI', 'GST'))

    Month = st.sidebar.selectbox('Month', ('1', '2', '3', '4', '5','6','7', '8', '9', '10', '11','12'))
    DayofMonth = st.sidebar.selectbox("DayofMonth",('1', '2', '3', '4', '5','6','7', '8', '9', '10', '11','12','13', '14', '15', '16', '17','18','19','20', '21', '22', '23','24','25','26', '27', '28', '29', '30','31'))
    DayOfWeek = st.sidebar.selectbox("DayOfWeek",('1', '2', '3', '4', '5','6','7'))

    Actual_Shipment_Time = st.text_input("Actual_Shipment_Time","Type Here")
    Planned_Shipment_Time = st.text_input("Planned_Shipment_Time","Type Here")
    Planned_Delivery_Time = st.text_input("Planned_Delivery_Time","Type Here")
    Carrier_Name = st.text_input("Carrier_Name","Type Here")
    Carrier_Num = st.text_input("Carrier_Num","Type Here")
    Planned_TimeofTravel = st.text_input("Planned_TimeofTravel","Type Here")
    Distance = st.text_input("Distance","Type Here")
    Shipment_Delay = st.text_input("Shipment_Delay","Type Here")
    Year = st.text_input("Year","Type Here")
    result=""

    data = {
            'Year': Year,
            'Month': Month,
            'DayofMonth': DayofMonth,
            'DayOfWeek': DayOfWeek,
            'Actual_Shipment_Time': Actual_Shipment_Time,
            'Planned_Shipment_Time': Planned_Shipment_Time,
            'Planned_Delivery_Time': Planned_Delivery_Time,
            'Carrier_Name': Carrier_Name,
            'Carrier_Num': Carrier_Num,
            'Planned_TimeofTravel': Planned_TimeofTravel,
            'Shipment_Delay': Shipment_Delay,
            'Source': Source,
            'Destination': Destination,
            'Distance': Distance
            
            }
    input_df = pd.DataFrame(data, index=[0])
    
    df=pd.read_pickle("fedex.bz2")
    df=df.dropna()
    X = df.drop(['Delivery_Status'], axis = 1)
    df = pd.concat([input_df, X], axis=0)
    df=pd.get_dummies(df,columns=['Carrier_Name','Source','Destination'],sparse=True)
    df = df[:1]
    print(df)

    #Write out input selection
    st.subheader('User Input (Pandas DataFrame)')
    st.write(df)
    st.write(len(df.columns))

    if st.button("Predict"):
        result=predict_note_authentication(df)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    