from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
from PyQt5.uic import loadUi
import random
import sys
import datetime

class Room():
    def __init__(self):
        self._rname = None
        self._target_temp = None
        self._target_humid = None
        self._room_no = None
        self._hygrometer_id = None  # Initialisiere das Hygrometer-ID-Attribut
        self._thermometer_id = None  # Initialisiere das Thermometer-ID-Attribut
        self.current_time = None  # Initialisiere die aktuelle Zeit

    def get_rname(self):
        return self._rname
    
    def set_rname(self, rname):
        self._rname = rname

    def get_target_temp(self):
        return self._target_temp
    
    def set_target_temp(self, target_temp):
        self._target_temp = target_temp

    def get_target_humid(self):
        return self._target_humid
    
    def set_target_humid(self, target_humid):
        self._target_humid = target_humid
    
    def set_room_no(self):
        self._room_no = random.randint(1000, 9999)
    
    def get_room_no(self):
        return self._room_no
    
    def set_current_time(self):
        self.current_time = datetime.datetime.now()
        
    def get_current_time(self):
        return self.current_time
    
    def set_thermometer_id(self):
        self._thermometer_id = random.randint(1000, 9999)

    def get_thermometer_id(self):
        return self._thermometer_id
    
    def set_hygrometer_id(self):
        self._hygrometer_id = random.randint(1000, 9999)

    def get_hygrometer_id(self):
        return self._hygrometer_id


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("Übungsklasur/Luftfeuchtigkeit.ui", self)

        # Connect buttons to methods
        self.btn_create_room.clicked.connect(self.btn_create_room_clicked)

    def btn_create_room_clicked(self):
        # Create an instance of the Room data input dialog
        room_data_input = dlgRoomDataInput(self)

        # Show the dialog and get the status
        dlg_status = room_data_input.exec()  # Call exec() correctly

        if dlg_status == QDialog.Accepted:
            room1 = Room()
            room1.set_rname(room_data_input.le_name.text())  # Assuming le_name is the line edit for room name
            room1.set_target_humid(float(room_data_input.le_target_humidity.text()))  # Convert to float
            room1.set_target_temp(float(room_data_input.le_target_temp.text()))  # Convert to float
            room1.set_current_time()  # Set the current time
            room1.set_room_no()  # Set room number
            room1.set_hygrometer_id()  # Set hygrometer ID
            room1.set_thermometer_id()  # Set thermometer ID

            # Set label text with room details
            self.lbl_room_nr.setText(f"Raumnr: {room1.get_room_no()}")
            self.lbl_room_name.setText(f"Raumbezeichnung: {room1.get_rname()}")
            self.lbl_target_temp.setText(f"Temperatur (SOLL): {room1.get_target_temp()}")
            self.lbl_rel_humid.setText(f"rel. Luftfeuchtigkeit: {room1.get_target_humid()}")
            self.lbl_time.setText(f"Uhrzeit: {room1.get_current_time()}")
            self.lbl_hygro_id.setText(f"Hygrometer Id: {room1.get_hygrometer_id()}")
            self.lbl_therm_id.setText(f"Thermometer Id: {room1.get_thermometer_id()}")

            print(f"Room {room1.get_rname()} created with room number {room1.get_room_no()}.")
        else:
            pass  # If the dialog was canceled


class dlgRoomDataInput(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("Übungsklasur/dialog_raummanager.ui", self)

        # Connect buttons to accept/reject
        self.dlgBtn_set_room_data.clicked.connect(self.accept)  # Accept the dialog (OK button)
        self.dlgBtn_cancel.clicked.connect(self.reject)  # Reject the dialog (Cancel button)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_ui = MainWindow()
    main_ui.show()
    sys.exit(app.exec())
