# pincode_app
This classifies the Drop Pincodes into 5 Standard Delivery Zones based on the Pickup Pincode. 
The logic used is :
1) INTRA CITY – When a courier company ships a parcel within the same city 
2) INTRA STATE – When a courier company picks up and delivers a parcel within the same state 
3) METRO TO METRO – When pick-up and delivery are done in metro cities. For example, if a courier company picks up a product 
                    from New Delhi and delivers it in Hyderabad, the shipping zone would fall under Zone C 
4)REST OF INDIA – When any or both pick-up and delivery is done in Rest of India except the North East and Jammu & Kashmir 
5)SPECIAL REGION – When any or both of pick-up and delivery is done in the North East region or Jammu and Kashmir or Kerala
