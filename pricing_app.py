import streamlit as st
import pandas as pd

# Title of the Streamlit app
st.title("Data Consulting Pricing Calculator")

# Input section for resource types and costs
st.header("Input Resource Costs")

# Initialize lists to store resource names, hours, and costs
resource_names = []
resource_hours = []
resource_costs = []

# Function to add new resources
def add_resource():
    with st.form(key='add_resource_form'):
        resource_name = st.text_input("Resource Name", key='resource_name')
        hourly_rate = st.number_input("Hourly Rate", min_value=0.0, value=0.0, step=0.1, key='hourly_rate')
        hours = st.number_input("Hours Needed", min_value=0.0, value=0.0, step=0.1, key='hours')
        submit_button = st.form_submit_button(label='Add Resource')
        if submit_button:
            if resource_name and hourly_rate and hours:
                resource_names.append(resource_name)
                resource_costs.append(hourly_rate * hours)
                resource_hours.append(hours)
            else:
                st.error("Please fill out all fields")

# Call the function to add resources
add_resource()

# Show the resources added
if resource_names:
    st.subheader("Resources Added:")
    data = {'Resource Name': resource_names, 'Total Cost': resource_costs, 'Hours': resource_hours}
    df = pd.DataFrame(data)
    st.dataframe(df)

    # Calculate blended rate
    total_cost = sum(resource_costs)
    total_hours = sum(resource_hours)
    blended_rate = total_cost / total_hours if total_hours != 0 else 0

    # Show results
    st.subheader("Summary")
    st.write(f"Total Cost: ${total_cost:.2f}")
    st.write(f"Blended Rate: ${blended_rate:.2f} per hour")

else:
    st.write("No resources added yet.")
