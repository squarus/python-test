import urllib.request
text = urllib.request.urlopen("http://www.textfiles.com/etext/AUTHORS/SHAKESPEARE/shakespeare-romeo-48.txt").read().decode('utf8')
sozluk = {
    "sword":text.count("sword"),
    "love":text.count("love"),
    "wench":text.count("wench"),
    "fool":text.count("fool")
}
print(sozluk)
