from app.controllers.controller import BaseController
from flask import render_template

class OopPageController(BaseController):
    @staticmethod
    def get():
        return render_template('aaatesting.html')
