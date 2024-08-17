from translate import Translator
import sys
import os


if __name__ == "__main__":
    language = input("Please provide a langeuage translation: ").lower()
    if language not in ["en", "ja", "fr", "zh"]:
        # Full name provided
        match language:
            case "english":
                language = "en"
            case "japanese":
                language = "ja"
            case "french":
                language = "fr"
            case "chinese":
                language = "zh"
            case _ :
                print("Language not found. Exiting")
                sys.exit()
    file = input("Please provide file for translation: ")
    try:
        with open(file, encoding="utf-8") as source_file:
            text = source_file.read()
            file_name = file.split(".")[0]
            with open(file_name+"_translation_"+language+"_.txt", mode="w", encoding="utf-8") as translation_file:
                translator = Translator(to_lang=language)
                translation = translator.translate(text)
                translation_file.write(translation)
                print("Translation complete")

    except FileExistsError:
        print("File does not exits. Exiting.")
        sys.exit()
    
            
            