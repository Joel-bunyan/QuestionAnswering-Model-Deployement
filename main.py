from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):

    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run when the form opens.

    def primary_color_1_click(self, **event_args):
        # Access the values from the app 
        question_text = self.question_text.text
        context_text = self.input_text.text

        # Call the jupyter notebook uplink method
        result = anvil.server.call('answer_questions', question_text, context_text)

        # Show the result to the user
        self.answer_text.text = result

    def text_area_1_change(self, **event_args):
      """This method is called when the text in this text area is edited"""
      pass

    def outlined_button_1_click(self, **event_args):
      """This method is called when the button is clicked"""
      question_text = self.question_text.text
      input_text = self.input_text.text
      result = anvil.server.call('answer_questions', question_text, input_text)
      self.answer_text.text = result
