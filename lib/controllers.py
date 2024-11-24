import streamlit as st
from schemas.set import PlantSet

@st.dialog("Adicionar novo grupo de plantas")
def add_set(idx: int = None):
    if idx is not None:
        plant_set = st.session_state.plant_sets[idx]
        set_name = st.text_input('Nome do grupo de plantas', value=plant_set.set_name)
        planting_date = st.date_input('Data de plantio', value=plant_set.planting_date)
        total_plants = st.number_input('Total de plantas', value=plant_set.total_plants, min_value=1, step=1)
        average_flowering_day = st.number_input('Média de dias para florescimento', value=plant_set.average_flowering_day, min_value=1, step=1)
        standard_deviation_flowering_day = st.number_input('Desvio padrão de dias para florescimento', value=plant_set.standard_deviation_flowering_day, min_value=1, step=1)
        average_flowers_per_plant = st.number_input('Média de flores por planta', value=plant_set.average_flowers_per_plant, min_value=1, step=1)
        standard_deviation_flowers_per_plant = st.number_input('Desvio padrão de flores por planta', value=plant_set.standard_deviation_flowers_per_plant, min_value=1, step=1)
        button_label = "Salvar edição"
    else:
        set_name = st.text_input('Nome do grupo de plantas')
        planting_date = st.date_input('Data de plantio')
        total_plants = st.number_input('Total de plantas', min_value=1, step=1)
        average_flowering_day = st.number_input('Média de dias para florescimento', min_value=1, step=1)
        standard_deviation_flowering_day = st.number_input('Desvio padrão de dias para florescimento', min_value=1, step=1)
        average_flowers_per_plant = st.number_input('Média de flores por planta', min_value=1, step=1)
        standard_deviation_flowers_per_plant = st.number_input('Desvio padrão de flores por planta', min_value=1, step=1)
        button_label = "Adicionar"

    if st.button(button_label):
        if idx is not None:
            # Mudar os valores do set de plantas existente preenchendo com os novos valores e retornando flowers_per_plant, flowering_days, flattened_flowering_day e flowering_days_counter para o seu valor padrão
            plant_set.set_name = set_name
            plant_set.planting_date = planting_date
            plant_set.total_plants = total_plants
            plant_set.average_flowering_day = average_flowering_day
            plant_set.standard_deviation_flowering_day = standard_deviation_flowering_day
            plant_set.average_flowers_per_plant = average_flowers_per_plant
            plant_set.standard_deviation_flowers_per_plant = standard_deviation_flowers_per_plant
            plant_set.flowers_per_plant = []
            plant_set.flowering_days = []
            plant_set.flattened_flowering_days = []
            plant_set.flowering_days_counter = None
            st.session_state.plant_sets[idx] = plant_set

        else:
            new_plant_set = PlantSet(
                set_name=set_name,
                planting_date=planting_date,
                total_plants=total_plants,
                average_flowering_day=average_flowering_day,
                standard_deviation_flowering_day=standard_deviation_flowering_day,
                average_flowers_per_plant=average_flowers_per_plant,
                standard_deviation_flowers_per_plant=standard_deviation_flowers_per_plant
            )
            st.session_state.plant_sets.append(new_plant_set)
        st.rerun()
