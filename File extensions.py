# extensions.py

def main():

    file_name = input("Enter the file name: ")

    file_name = file_name.strip().lower()

    media_type = get_media_type(file_name)

    # Print the result
    print(media_type)

def get_media_type(name):
    
    if name.endswith(".gif"):
        return "image/gif"
    elif name.endswith(".jpg") or name.endswith(".jpeg"):
        return "image/jpeg"
    elif name.endswith(".png"):
        return "image/png"
    elif name.endswith(".pdf"):
        return "application/pdf"
    elif name.endswith(".txt"):
        return "text/plain"
    elif name.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"

if __name__ == "__main__":
    main()
