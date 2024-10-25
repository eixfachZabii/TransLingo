import boto3
import boto3
import os
import json
import logging

import uuid

# Logging einrichten
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# Clients für Polly und S3 initialisieren
polly_client = boto3.client('polly')
s3_client = boto3.client('s3')
# AWS Translate Client initialisieren
translate_client = boto3.client('translate')


def lambda_handler(event, context):
    # Text aus dem Event extrahieren
    text = event.get('text', 'Hallo, dies ist ein Standardtext für die Sprachsynthese.')
    source_language = event.get('source_language', 'de-DE')
    target_language = event.get('target_language', 'en-US')
    voice = event.get('voice', 'Joanna')

    bucket_name = os.environ['S3_BUCKET_NAME']
    unique_filename = f"output_{uuid.uuid4()}.mp3"

    
    try:
        # Übersetzung durchführen
        response = translate_client.translate_text(
            Text=text,
            SourceLanguageCode=source_language,
            TargetLanguageCode=target_language,
        )

        # Übersetzten Text ausgeben
        translated_text = response['TranslatedText']
        print(f"Übersetzter Text: {translated_text}")


        # Text in Sprache umwandeln
        response = polly_client.synthesize_speech(
            Text=translated_text,
            OutputFormat='mp3',
            VoiceID=voice,
            LanguageCode=target_language
        )
        

        # Audiodatei im S3-Bucket speichern
        s3_client.put_object(
            Bucket=bucket_name,
            Key=unique_filename,
            Body=response['AudioStream'].read()
        )

        # Generieren der vorab signierten URL zum Herunterladen
        download_url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': unique_filename},
            ExpiresIn=3600  # URL ist 1 Stunde gültig
        )


        return {
            'statusCode': 200,
            'message': 'Die Audiodatei wurde erfolgreich in S3 gespeichert.',
            'downloadUrl': download_url  # Vorab signierte URL zurückgeben
        }
        
    except Exception as e:
        logger.error(f"Fehler: {str(e)}")  # Fehler protokollieren
        return {
            'statusCode': 500,
            'error': str(e)
        }
    

