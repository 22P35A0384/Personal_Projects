from google.cloud import translate

def translate_text(text, target_language):
    # Create an instance of the translation client
    client = translate.TranslationServiceClient()

    # Specify the text to be translated and the target language
    parent = client.location_path("your_project_id", "global")
    response = client.translate_text(
        parent=parent,
        contents=[text],
        mime_type="text/plain",
        source_language_code="en-US",
        target_language_code=target_language,
    )

    # Retrieve the translated text
    translation = response.translations[0].translated_text
    return translation

# Example usage
text = "I love you"
target_language = "fr"  # Translate to French
translated_text = translate_text(text, target_language)
print(translated_text)
