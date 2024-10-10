import os

def main():
    path = "/Users/mateo/Desktop/scrape_grailed/images"
    files = os.listdir(path)
    for index, file in enumerate(files,1):
        os.rename(os.path.join(path, file), os.path.join(path, ''.join(['p_img',str(index), '.png'])))
if __name__ == "__main__":
    main()
    print("done")