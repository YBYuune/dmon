from html.parser import HTMLParser

# fileToRead = "./Html/NotDigitama.txt"
fileToRead = "./Html/Digitama.txt"

class DigiHTMLParser(HTMLParser):
	m_DigiList = []

	def handle_starttag(self, tag, attrs):
		if(tag == "img"):
			validCard = False
			tmpSrc = ""

			for attr in attrs:
				if (attr[0] == "src" and not "blank" in attr[1]):
					tmpSrc = attr[1]
				if (attr[0] == "draggable"):
					validCard = True

			if (validCard and tmpSrc):
				url = tmpSrc.split('/')
				imageName = url[-1]
				imageNameSplit = imageName.split(".")

				invalidPartPos = len(tmpSrc)
				if (len(imageNameSplit) > 2):
					invalidPartPos = tmpSrc.rfind(imageNameSplit[2]) - 1
				
				image = tmpSrc[:invalidPartPos]
				self.m_DigiList.append(image + "\n")

f = open(".\\" + fileToRead)
fileContents = f.read()

parser = DigiHTMLParser()
parser.feed(fileContents)
parser.m_DigiList.pop()

print("Num items: ", len(parser.m_DigiList))
#for card in parser.m_DigiList:
#		print(card)

f2 = open("cards.txt", "w")
f2.writelines(parser.m_DigiList)
f2.close()
