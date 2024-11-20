import streamlit as st
from views.simulator import simulator_page

def home():
  st.title('Simulador de Janela de Polinização')

  st.write('Este simulador foi desenvolvido para ajudar a idealizar cenários de grupos de plantas com diferentes datas de plantio para redução de grandes picos de polinização, o que pode ser útil para a planejamento de mão-de-obra e equipamentos.')
  
  st.markdown('### Pronto para começar?')
  if st.button('Ir para o simulador', type='primary'):
    st.switch_page(simulator_page)

  st.markdown('### Como funciona?')
  st.write('1. Adicione um grupo de plantas com as seguintes informações:')
  expander = st.expander('Detalhes do grupo de plantas')
  expander.write('   - Nome do grupo de plantas')
  expander.write('   - Data de plantio')
  expander.write('   - Total de plantas')
  expander.write('   - Média de dias para floração')
  expander.write('   - Desvio padrão de dias para floração')
  expander.write('   - Média de flores por planta')
  expander.write('   - Desvio padrão de flores por planta')
  st.write('2. Clique em "Adicionar" para adicionar o grupo de plantas.')
  st.write('3. Repita o passo 1 para adicionar mais grupos de plantas.')
  st.write('4. Clique em "Gerar simulação de janela de polinização" para visualizar a simulação.')
  st.markdown('### Como tudo é calculado?')
  st.write('1. Para cada planta, o número de flores é calculado usando uma distribuição normal com a média e o desvio padrão fornecidos.')
  st.write('2. Para cada flor, o dia de floração é calculado usando uma distribuição normal com a média e o desvio padrão fornecidos.')
  st.write('3. Geramos uma lista de dias de floração e contamos o número de flores em cada dia.')
  st.markdown('### O que é exibido na simulação?')
  st.write('A simulação exibe um gráfico de barras com o número de flores em cada dia de floração para cada grupo de plantas adicionado.')
  st.image('./assets/visualization.png')
  st.write('O eixo x representa a data de floração e o eixo y representa o número de flores.')

homepage = st.Page(page=home, title='Início', icon=':material/home:')
