from bs4 import BeautifulSoup

def parseFile(filename):
    with open(filename, 'r') as f:
        html_text = f.read()
    soup = BeautifulSoup(html_text, 'html.parser')

    words = []

    for s in soup.find_all("span", {"class": "collapseomatic"}):
        korean = s.previous_sibling.previous_sibling.text
        english = s.text
        c = s.parent.find("div", {'class': "collapseomatic_content"})
        if c == None:
            c = s.parent.next_sibling
        words.append({'korean': korean, 'english': english, 'examples': c.children})

    return words 


def printParse(words):
    for word in words:
        print(word["korean"], end="\t")
        print(word["english"], end="\t")
        for child in word["examples"]:
            print(str(child).replace('\n', ' ').replace('\r', '').replace('\t', ''), end="")
        print("")


def main():
    for i in range(1, 25+1):
        words = parseFile("./units/" + str(i) + ".html")
        printParse(words)

main()