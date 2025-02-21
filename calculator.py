import streamlit as st

def calculate_carbon_footprint(kwh, kilometers, gas):
    # Coefficients for carbon emissions (these are example values)
    # 0.92 kg CO2 per kWh for electricity
    # 0.21 kg CO2 per kilometer for car
    # 0.054 kg CO2 per cubic foot of natural gas
    electricity_emissions = kwh * 0.92
    car_emissions = kilometers * 0.21
    gas_emissions = gas * 0.054
    total_emissions = electricity_emissions + car_emissions + gas_emissions
    return total_emissions

st.title('Simple Carbon Footprint Calculator')

kwh = st.number_input('Enter your monthly electricity usage in kWh:', min_value=0.0, value=0.0)
kilometers = st.number_input('Enter your annual kilometers driven by car:', min_value=0.0, value=0.0)
gas = st.number_input('Enter your monthly natural gas usage in cubic feet:', min_value=0.0, value=0.0)

if st.button('Calculate Carbon Footprint'):
    total_emissions = calculate_carbon_footprint(kwh, kilometers, gas)
    st.write(f"Your estimated total carbon emissions are {total_emissions:.2f} kg CO2.")
