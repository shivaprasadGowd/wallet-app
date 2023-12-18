from ._anvil_designer import report_analysisTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class report_analysis(report_analysisTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.plot_1.data = anvil.server.call('generate_transaction_trend_data')
    self.plot_1.x = 'transaction_type'
    self.plot_1.y = 'total_volume'
    self.plot_1.type = 'bar'