import streamlit as st

def releases():
  st.title('Simulador de Janela de Polinização')

  st.markdown('# ✨ Novidades ✨')

  st.markdown('### Versão 1.2.0')
  st.write('🛠️ Agora você pode definir a média de produtividade de uma mão-de-obra (por dia) para ter a distribuição de pessoas necessárias para o trabalho!')

  st.markdown('### Versão 1.1.0')
  st.write('⏱️ Otimização do tempo de geração de amostras de dados, tornando o processo mais rápido e eficiente.')
  st.write('🔄 Agora, somente o grupo de plantas que for editado terá uma nova simulação gerada, otimizando ainda mais o tempo.')

  st.markdown('### Versão 1.0.0')
  st.write('🚀 Lançamento do simulador de janela de polinização!')
  

releases_page = st.Page(page=releases, title='Atualizações', icon=':material/rocket_launch:')
