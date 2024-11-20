import streamlit as st
import pandas as pd
from datetime import timedelta
from lib.controllers import add_set


def simulator():
  if 'plant_sets' not in st.session_state:
    st.session_state.plant_sets = []

  if 'show_add_set' not in st.session_state:
    st.session_state.show_add_set = False
  
  st.title('Simulador de Janela de Polinização')

  st.write('Este simulador foi desenvolvido para ajudar a idealizar cenários de grupos de plantas com diferentes datas de plantio para redução de grandes picos de polinização, o que pode ser útil para a planejamento de mão-de-obra e equipamentos.')
  
  st.markdown('### Adicionar grupo de plantas')
      
  st.button('Adicionar novo grupo de plantas', on_click=add_set)

  st.markdown('### Grupos de plantas adicionados')

  if len(st.session_state.plant_sets) == 0:
    st.write('Nenhum grupo de plantas foi adicionado.')
  else:
    for index, plant_set in enumerate(st.session_state.plant_sets):
      exp = st.expander(f'{index + 1}. {plant_set.set_name}')
      exp.write(f'**Data de plantio:** {plant_set.planting_date.strftime("%Y-%m-%d")}')
      exp.write(f'**Total de plantas:** {plant_set.total_plants}')
      exp.write(f'**Média de dias para floração:** {plant_set.average_flowering_day}')
      exp.write(f'**Desvio padrão de dias para floração:** {plant_set.standard_deviation_flowering_day}')
      exp.write(f'**Média de flores por planta:** {plant_set.average_flowers_per_plant}')
      exp.write(f'**Desvio padrão de flores por planta:** {plant_set.standard_deviation_flowers_per_plant}')
      if exp.button('Editar', key=index):
        st.session_state.show_add_set = True
        add_set(index)

  if st.button('Gerar simulação de janela de polinização', type='primary'):
    df_list = []
    for s in st.session_state.plant_sets:
      s.get_flowers_per_plant()
      s.get_flowering_days()
      s.get_flattened_flowering_days()
      s.get_flowering_days_counter()

      df = pd.DataFrame.from_dict(s.flowering_days_counter, orient='index', columns=['flower_count'])
      df['plant_set'] = s.set_name
      df['flowering_date'] = [(s.planting_date + timedelta(days=x)).date() for x in df.index]
      df_list.append(df.reset_index())
    
    df = pd.concat(df_list, axis=0)
    df = df.pivot(index='flowering_date', columns='plant_set', values='flower_count')

    st.bar_chart(df)

simulator_page = st.Page(page=simulator, title='Simulador', icon=':material/calculate:')