import requests
import os
import json
import pygame
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar
from PySide6.QtCore import QFile, QEventLoop
from ui_mainwindow import Ui_MainWindow

import boto3
import json
import time

def download_and_play_audio(download_url, save_as='downloaded_audio.mp3'):
    window.stackedWidget.setCurrentIndex(1)
    QApplication.processEvents(QEventLoop.AllEvents)

    try:
        # Remove the existing file if it exists
        if os.path.exists(save_as):
            os.remove(save_as)
            print(f"Removed existing file: {save_as}")

        # Download the audio file
        response = requests.get(download_url)
        response.raise_for_status()  # Raise an error for bad responses

        # Save the file to the local system
        with open(save_as, 'wb') as audio_file:
            audio_file.write(response.content)
        
        print(f"Audio downloaded and saved as {save_as}. Playing audio...")

        # Initialize pygame mixer
        pygame.mixer.init()
        pygame.mixer.music.load(save_as)
        pygame.mixer.music.play()
        window.stackedWidget.setCurrentIndex(2)

    except Exception as e:
        print(f"Error downloading the audio file: {e}")
        window.statusBar().showMessage((str)(e))
    
    window.stackedWidget.setCurrentIndex(2)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Set up the UI
        self.setup_connections()

    def setup_connections(self):
        # Connect the button's clicked signal to the slot
        self.pushButton.clicked.connect(self.on_button_back_click)
        self.pushButton_openfile.clicked.connect(self.on_button_file_click)
        self.pushButton_trans.clicked.connect(self.on_button_trans_click)
        self.pushButton_zwischenablage.clicked.connect(self.on_button_clib_click)

    def on_button_clib_click(self):
        # Define what happens when the button is clicked
        clipboard = QApplication.clipboard()  # Access the clipboard
        text = clipboard.text() 
        window.plainTextEdit.setPlainText(text)

    def on_button_trans_click(self):

        # Define what happens when the button is clicked
        try:
            # Initialize a session using your AWS credentials
            session = boto3.Session(
                aws_access_key_id='YOUR_AWS_ACCESS_KEY',   # Replace with your access key
                aws_secret_access_key='YOUR_AWS_SECRET_KEY',  # Replace with your secret key
                region_name='eu-central-1'  # Replace with your region
            )

            # Create a Lambda client
            lambda_client = session.client('lambda')

            # Define the input event for the Lambda function
            input_event = {
                "text": window.plainTextEdit.toPlainText(),
                "source_language": "de-de",  # Deutsch
                "target_language": "en-US",
                "voice": ""
            }

            # Invoke the Lambda function
            response = lambda_client.invoke(
                FunctionName='team-translingo-casehackathon-20241025-muc-bucket',  # Replace with your Lambda function name
                InvocationType='RequestResponse',  # Synchronous invocation
                Payload=json.dumps(input_event)  # Convert the input event to a JSON string
            )

            # Read the response from the Lambda function
            response_payload = json.loads(response['Payload'].read())

            # Print the response
            print(json.dumps(response_payload, indent=4))
        except Exception as e:
            window.statusBar().showMessage((str)(e))
            return
        download_and_play_audio(response_payload["downloadUrl"], "file.mp3")


    def on_button_back_click(self):
        # Define what happens when the button is clicked
        window.stackedWidget.setCurrentIndex(0)

    def on_button_file_click(self):
        # Define what happens when the button is clicked
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())