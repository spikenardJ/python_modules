def mood_response(mood): # Implement your response logic here
    if mood == "Happy":
        return "\n😊 The best way to pay for a lovely moment is to enjoy it. \n- Richard Bach\n"
    elif mood == "Sad":
        return "\n😢 When you’re happy you enjoy the music, but when you’re sad you understand the lyrics. \n- Frank Ocean\n"
    elif mood == "Excited":
        return "\n🤩 Nothing great was ever achieved without enthusiasm. \n- Ralph Waldo Emerson\n"
    elif mood == "Exit":
        return "\n👋 Good Bye! 👋\n"
    else:
        return "Invalid response. Please try again with: 'Happy', 'Sad', or 'Excited'"