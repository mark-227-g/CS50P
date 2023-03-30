###################
# CS50P Python
# Mark Edwards
# Lesson 1
##################

filename = input("Filename: ")
f = filename.split('.')
ext = f[len(f)-1]

match ext.strip().lower():
    case "gif":
        ftype="image/gif"
    case "jpg":
        ftype="image/jpeg"
    case "jpeg":
        ftype="image/jpeg"
    case "png":
        ftype="image/png"
    case "pdf":
        ftype="application/pdf"
    case "txt":
        ftype="text/plain"
    case "zip":
        ftype="application/zip"
    case _:
        ftype = "application/octet-stream"

print(ftype)