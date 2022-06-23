from PIL import Image
import os
import concurrent.futures


def process(img_url, num):
    bg = Image.open('wtp.png').convert('RGBA').resize((480, 270), Image.LANCZOS)
    image = Image.open(img_url).convert('RGBA')
    w2, h2 = int((image.size[0]/image.size[1])*150), int((image.size[1]/image.size[0])*150)
    x2, y2 = 25+((250-w2)//2), 10+((250-h2)//2)
    if w2 > bg.size[0] or h2 > bg.size[1]:
        w2 *= .6
        h2 *= .6
        x2, y2 = 25+((250-w2)//2), 10+((250-h2)//2)
        errors.append(img_url)
    image = image.resize((int(w2), int(h2)), Image.LANCZOS)
    image1 = image.point(lambda i: 0 if 0 <= i <= 255 else 0)#remove for normal
    bg.paste(image1, (int(x2), int(y2)), image)#just image for normal
    bg.save(f'hidden/{img_url.replace(path, "")}')
    return num
    


def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(process, path+url, i) for i, url in enumerate(lst)]
        for future in concurrent.futures.as_completed(futures):
            print(f"{future.result()}/{len(lst)}")
            

if __name__ == "__main__":
    path = 'C:/Users/Asher/Images/pokemon/statics_pixels/normal/'
    lst = os.listdir(path)
    errors = []
    main()
    print(errors)
