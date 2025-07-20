def main():
    text = input("What  is the answer to the Great Question of Life, the Universe and Everything? ").strip().lower()
    
    def question(string):
        if string == "42":
            return "Yes"
        elif string == "forty-two":
            return "Yes"
        elif string == "forty two":
            return "Yes"
        else:
            return "No"
        
    print(question(text))
    
if __name__ == "__main__":
    main()
    
        

    