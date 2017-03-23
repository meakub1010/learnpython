import sys


def main(filename):
    f = open(filename, mode="rt", encoding="utf-8")
    for line in f:
        print(line) # print double space in between lines

    f.seek(0, 0)
    print("\n print with single space ... \n")

    for line in f:
        sys.stdout.write(line) # print single space in between lines

    f.close()
# run as from CMD : C:\GithubProjects\learnpython\Files>C:\Python\python.exe files.py file.txt
if __name__ == '__main__':
    main(sys.argv[1])