import streamlit as st
import pandas as pd
from datetime import datetime
from datetime import timedelta
from lib.controllers import add_set


def simulator():
  if 'plant_sets' not in st.session_state:
    st.session_state.plant_sets = []

  if 'show_add_set' not in st.session_state:
    st.session_state.show_add_set = False
  
  st.title('Simulador de Janela de Polinização')

  st.write('Este simulador foi desenvolvido para ajudar a idealizar cenários de grupos de plantas com diferentes datas de plantio para redução de grandes picos de polinização, o que pode ser útil para a planejamento de mão-de-obra e equipamentos.')
      

  st.markdown('### Grupos de plantas adicionados')
  st.button('Adicionar grupo de plantas', on_click=add_set, type='primary')

  if len(st.session_state.plant_sets) == 0:
    st.write('Nenhum grupo de plantas foi adicionado.')
  else:
    for index, plant_set in enumerate(st.session_state.plant_sets):
      exp = st.expander(f'{index + 1}. {plant_set.set_name}')
      exp.write(f'**Data de plantio:** {plant_set.planting_date.strftime("%Y-%m-%d")}')
      exp.write(f'**Total de plantas:** {plant_set.total_plants}')
      exp.write(f'**Média de dias para florescimento:** {plant_set.average_flowering_day}')
      exp.write(f'**Desvio padrão de dias para florescimento:** {plant_set.standard_deviation_flowering_day}')
      exp.write(f'**Média de flores por planta:** {plant_set.average_flowers_per_plant}')
      exp.write(f'**Desvio padrão de flores por planta:** {plant_set.standard_deviation_flowers_per_plant}')

      col1, col2 = exp.columns([1,9])
      if col1.button('Editar', key=str(index) + 'edit'):
        st.session_state.show_add_set = True
        add_set(index)

      # Adicionar botão para remover o grupo de plantas
      if col2.button(':material/delete:', key=str(index) + 'delete'):
        st.session_state.plant_sets = [s for i, s in enumerate(st.session_state.plant_sets) if i != index]
        st.rerun()

  # Selecionar se quer ver o gráfico de área ou de barras
  col1, col2 = st.columns(2)
  col1.markdown('### Tipo de gráfico')
  col1.write('O gráfico de área é ideal se selecionar a opção de visualização em camadas, pois permite melhor visualizar a sincronia de florescimento entre os grupos de plantas.')
  chart_type = col1.radio('Tipo de gráfico', ['Gráfico de barras', 'Gráfico de área'])

  # Selecionar se quer o gráfico empilhado ou em camadas
  col2.markdown('### Tipo de visualização')
  col2.write('O gráfico empilhado exibe o número total (somatório dos grupos) de flores em cada dia de florescimento, enquanto cria camadas separadas para cada grupo de plantas.')
  viz_type = col2.radio('Tipo de visualização', ['Empilhado', 'Camadas'])

  st.write('A depender da quantidade de dados gerados, o gráfico pode demorar um pouco para ser exibido.')
  time_container = st.container()
  if st.button('Gerar simulação', type='primary', disabled=len(st.session_state.plant_sets) == 0):
    start_time = datetime.now()
    df_list = []
    for s in st.session_state.plant_sets:
      # Verificar se o s.flowering_days_counter está vazio, se sim, chamar os métodos abaixo
      if s.flowering_days_counter is None:
        s.get_flowers_per_plant()
        s.get_flowering_days()
        s.get_flattened_flowering_days()
        s.get_flowering_days_counter()

      df = pd.DataFrame.from_dict(s.flowering_days_counter, orient='index', columns=['flower_count'])
      df['plant_set'] = s.set_name
      df['flowering_date'] = [(s.planting_date + timedelta(days=x)).strftime('%Y-%m-%d') for x in df.index]
      df_list.append(df.reset_index())
    
    df = pd.concat(df_list, axis=0)
    df = df.pivot(index='flowering_date', columns='plant_set', values='flower_count')

    if chart_type == 'Gráfico de barras':
      st.bar_chart(df, stack=True if viz_type == 'Empilhado' else 'layered', height=640)
    else:
      st.area_chart(df, stack=True if viz_type == 'Empilhado' else 'layered', height=640)

    expander = st.expander('Dados gerados')
    expander.write('Abaixo estão os dados gerados para cada grupo de plantas adicionado:')
    expander.dataframe(df)
    end_time = datetime.now()

    elapsed_time = (end_time - start_time).total_seconds()
    time_container.write(f'A simulação foi gerada em {elapsed_time:.2f} segundos.')

simulator_page = st.Page(page=simulator, title='Simulador', icon=':material/calculate:')