from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import *
from Project1Logic import *


class MainWindow(QWidget):
   """This funuction sets up the window."""
   def __init__(self):
       super().__init__()
       self.setWindowTitle("Voting Ballot")
       self.voting = Voting()
       self.setupUi()


   def setupUi(self):
       """This function sets up the window interface."""
       layout = QVBoxLayout()
       title = QLabel("Voting Ballot")
       title.setFont(QFont("Arial", 15))
       title.setAlignment(Qt.AlignmentFlag.AlignCenter)
       layout.addWidget(title)


       id_layout = QHBoxLayout()
       id_label = QLabel("ID Number:")
       self.id_input = QLineEdit()
       id_layout.addWidget(id_label)
       id_layout.addWidget(self.id_input)
       layout.addLayout(id_layout)


       candidate_label = QLabel("Candidate Names")
       candidate_label.setFont(QFont("Arial", 12))
       candidate_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
       layout.addWidget(candidate_label)


       self.radio_group = QButtonGroup(self)
       self.radio1 = QRadioButton("John Smith")
       self.radio2 = QRadioButton("Jane Doe")
       self.radio_group.addButton(self.radio1)
       self.radio_group.addButton(self.radio2)


       layout.addWidget(self.radio1)
       layout.addWidget(self.radio2)


       self.submit_button = QPushButton("Submit Vote")
       self.submit_button.clicked.connect(self.submit_vote)
       layout.addWidget(self.submit_button)


       self.status_label = QLabel("")
       self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
       layout.addWidget(self.status_label)


       self.setLayout(layout)

   def submit_vote(self):
       """This function checks and submits the vote, displaying the error message if necessary."""
       voter_id = self.id_input.text()
       selected_button = self.radio_group.checkedButton()
       valid_vote, message = self.voting.voter_valid(voter_id)


       if valid_vote is False:
           self.status_label.setText(message)
           self.status_label.setStyleSheet("color: red;")
           return
       if selected_button is None:
           self.status_label.setText("Select a Candidate")
           self.status_label.setStyleSheet("color: red;")
           return
       not_voted, message = self.voting.check_vote(voter_id)
       if not_voted is False:
           self.status_label.setText(message)
           self.status_label.setStyleSheet("color: red;")
           return

       self.voting.append_id(voter_id, selected_button.text())
       self.status_label.setText("Voted")
       self.status_label.setStyleSheet("color:green;")
       self.id_input.clear()
       self.radio_group.setExclusive(False)
       self.radio1.setChecked(False)
       self.radio2.setChecked(False)
       self.radio_group.setExclusive(True)
