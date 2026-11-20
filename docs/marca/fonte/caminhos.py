import os
HERE=os.path.dirname(os.path.abspath(__file__))
MARCA=os.path.dirname(HERE)                      # pasta marca/
TMP=os.environ.get('REPETECO_TMP','/tmp/repeteco-marca')  # fontes instanciadas e quadros temporários
os.makedirs(TMP,exist_ok=True)
