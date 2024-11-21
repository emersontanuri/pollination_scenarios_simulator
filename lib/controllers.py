import streamlit as st
from schemas.set import PlantSet

@st.dialog("Adicionar novo grupo de plantas")
def add_set(idx: int = None):
    if idx is not None:
        plant_set = st.session_state.plant_sets[idx]
        set_name = st.text_input('Nome do grupo de plantas', value=plant_set.set_name)
        planting_date = st.date_input('Data de plantio', value=plant_set.planting_date)
        total_plants = st.number_input('Total de plantas', value=plant_set.total_plants)
        average_flowering_day = st.number_input('Média de dias para floração', value=plant_set.average_flowering_day)
        standard_deviation_flowering_day = st.number_input('Desvio padrão de dias para floração', value=plant_set.standard_deviation_flowering_day)
        average_flowers_per_plant = st.number_input('Média de flores por planta', value=plant_set.average_flowers_per_plant)
        standard_deviation_flowers_per_plant = st.number_input('Desvio padrão de flores por planta', value=plant_set.standard_deviation_flowers_per_plant)
        button_label = "Salvar edição"
    else:
        set_name = st.text_input('Nome do grupo de plantas')
        planting_date = st.date_input('Data de plantio')
        total_plants = st.number_input('Total de plantas')
        average_flowering_day = st.number_input('Média de dias para floração')
        standard_deviation_flowering_day = st.number_input('Desvio padrão de dias para floração')
        average_flowers_per_plant = st.number_input('Média de flores por planta')
        standard_deviation_flowers_per_plant = st.number_input('Desvio padrão de flores por planta')
        button_label = "Adicionar"

    if st.button(button_label):
        new_plant_set = PlantSet(
            set_name=set_name,
            planting_date=planting_date,
            total_plants=total_plants,
            average_flowering_day=average_flowering_day,
            standard_deviation_flowering_day=standard_deviation_flowering_day,
            average_flowers_per_plant=average_flowers_per_plant,
            standard_deviation_flowers_per_plant=standard_deviation_flowers_per_plant
        )
        if idx is not None:
            st.session_state.plant_sets[idx] = new_plant_set
        else:
            st.session_state.plant_sets.append(new_plant_set)
        st.rerun()
