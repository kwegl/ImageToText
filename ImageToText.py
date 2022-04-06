from PIL import Image

def save_to_textfile(filepath, save_file, tolerance=255, darkMode=True, divide_resolution=1, contrast=1):
    img = Image.open(filepath, "r")
    w, h = img.size
    pixels = list(img.getdata())
    pixels = [pixels[i*w:(1+i)*w-1] for i in range(h)]

    chars = ("$","@","B","%","8","&","W","M","#","*","o","a","h","k","b","d","p","q","w","m","Z","O","0","Q","L","C","J","U","Y","X","z","c","v","u","n","x","r","j","f","t","/","\\","|","(",")","1","{","}","[","]","?","-","_","+","~","<",">","i","!","l","I",";",":",",","\"","^","`","'","."," ")
    maxBrightness = len(chars)-1

    f = open(str(save_file), "w")
    for i in range(0,h,divide_resolution):
        for j in range(0,w,divide_resolution):
            brightness = 0
            for l in range(divide_resolution):
                for k in range(divide_resolution):
                    brightness += int((((sum(pixels[i+l-divide_resolution][j+k-divide_resolution]) * maxBrightness)-127)*contrast+127) // (4*tolerance) // (divide_resolution*divide_resolution))

            if brightness > maxBrightness:
                brightness = maxBrightness
            elif brightness < 0:
                brightness = 0
            if darkMode:
                f.write(chars[maxBrightness-brightness]+" ")
            else:
                f.write(chars[brightness]+" ")
        f.write("\n")
    f.close()
